"""Odometry
Robot will be moved (using "passive wheels" mode) on the round.

After some time, you will indicate where the robot is located relative to its initial position ($$x, y, \theta$), using only the motor encoders.
"""
import pypot.dynamixel as dyn
import time
import math

class Odometry :

    xn=0
    yn=0
    tetan=0

    IDLEFT = 2
    IDRIGHT = 5

    DT = 0.05
    RADIUS_WHEEL=0.026
    ROBOT_WIDTH = 0.166

    
    def direct_kinematics(vl, vr):
        #vl & vr in m/s
        xpoint=(vr+vl)/2
        tetapoint=(vr-vl)/ROBOT_WIDTH
        return xpoint, tetapoint

    def odom(xpoint,tetapoint,dt):
        dteta=tetapoint*dt
        l=xpoint*dt
        try:
            r=l/dteta
        except ZeroDivisionError:
            r=0
            dy=0
            dx=l
            dteta=0

        else:
            dx=r*math.sin(dteta)
            dy=r*(1-math.cos(dteta))
        return dx,dy,dteta


    def tick_odom(xminusone,yminusone, tetaminusone, xpoint, tetapoint, dt):
        dx,dy,dteta=odom(xpoint,tetapoint,dt)
        tetan=tetaminusone+dteta
        xn=xminusone+dx*math.cos(tetaminusone)-dy*math.sin(tetaminusone)
        yn=yminusone+dx*math.sin(tetaminusone)+dy*math.cos(tetaminusone)
        return xn,yn,tetan

    

    def run_odometry():
        x0 = 0
        y0 = 0
        teta0 = 0
        xminusone = x0
        yminusone = y0
        tetaminusone = teta0
        next_update = time.time()
  

        while (1):
            
            vl, vr = dxl_io.get_present_speed([IDLEFT, IDRIGHT])

            vl=(vl*math.pi/180)*(RADIUS_WHEEL)#m/s
            vr=-(vr*math.pi/180)*(RADIUS_WHEEL)#m/s

            xpoint, tetapoint = direct_kinematics(vl, vr)
            
            r,dx, dy, dteta = odom(xpoint, tetapoint, DT,vl,vr)
            xn, yn, tetan = tick_odom(xminusone,yminusone, tetaminusone, xpoint, tetapoint, DT,vr,vl) 
                
            xminusone = xn
            yminusone = yn
            tetaminusone = tetan
            # print("vr {},vl {}".format(vr,vl))

            # print("r :",r)
            # print("tetapoint {}, xpoint {}".format(tetapoint, xpoint))
            # print("------------------")

            # print("dx {}, dy {}, dteta{}".format(dx,dy,dteta) )
            # print("------------------")


            # print("tetan : ", tetan)
            # print("xn : ", xn)
            # print("yn : ", yn)
            # print("------------------\n------------------")

            next_update += DT
            while time.time() < next_update:
                time.sleep(0.001) 


        print("je suis odometry")
