"""Go To
Robot will be put on a known initial position (for example a cross marked on the ground),
we will then provide a goal position and orientation (using international system units which are meters and radians).
The robot should move to reach this position/orientation.
"""

import pypot.dynamixel as dyn
import time
import math


try:
    from odometry import *
except ImportError:
    sys.path.append(sys.path[0] + '/..')
    from odometry import *

radius_wheel = 2.6 #in cm
radius_between_wheels = 16.6 #in cm

idLeft = 2
idRight = 5
v = 360 

#rotate an clockwise angle
#recives the angle in radians
def rotate_angle_clockwise(angle):
    angle = angle*180/math.pi
    #move the left wheel but not the right
    perimeter_circunference_robot = 2*math.pi*radius_between_wheels
    perimeter_circunference_wheel = 2*math.pi*radius_wheel
    distance_rotation = (angle*perimeter_circunference_robot)/360
    #we need the speed of the wheel
    v_rad = v*math.pi/180
    speed = v_rad * radius_wheel
    distance_rotation /= 2
    times = distance_rotation/speed
    print(perimeter_circunference_robot,distance_rotation,times, speed)
    #set the timer
    dxl_io.set_moving_speed({idLeft: v,idRight: v})
    time.sleep(times)
    dxl_io.set_moving_speed({idLeft: 0, idRight: 0})
    
# #rotate an anticlockwise angle
# #recives the angle in radians
def rotate_angle_anticlockwise(angle):
    angle = angle*180/math.pi
    #move the left wheel but not the right
    perimeter_circunference_robot = 2*math.pi*radius_between_wheels
    perimeter_circunference_wheel = 2*math.pi*radius_wheel
    distance_rotation = (angle*perimeter_circunference_robot)/360
    #we need the speed of the wheel
    v_rad = v*math.pi/180
    speed = v_rad * radius_wheel
    distance_rotation /= 2
    times = distance_rotation/speed
    print(perimeter_circunference_robot,distance_rotation,times, speed)
    #set the timer
    dxl_io.set_moving_speed({idLeft: -v,idRight: -v})
    time.sleep(times)
    dxl_io.set_moving_speed({idLeft: 0, idRight: 0})

# #we tell the robot to rotate an specific angle from his currently position
# def go_to_yxa(x,y,teta):
# 	#x in m, y in m
# 	#teta in rad from optometry

# 	#center the robot to 0 rad
#     x_opto =
#     y_opto =
# 	teta_optometry = 
# 	rotate_angle_clockwise(teta_optometry)

# 	#v_rad = v*math.pi/180
# 	#radius_wheel = radius_wheel/100 #radius in m
#     #speed = v_rad * radius_wheel
# 	#distance_x = x/speed
# 	#time_x = distance_x/speed
# 	#distance_y = y/speed
# 	#time_y = distance_y/speed

# 	if(x>x_opto and y>y_opto):
#         while(x != x_opto):
#     	   motors.set_moving_speed({idLeft: v, idRight: -v})
#     	motors.set_moving_speed({idLeft:0, idRight:0})
    	
#         rotate_angle_anticlockwise(90)
#         while(y != y_opto):
#     	   motors.set_moving_speed({idLeft: v, idRight: -v})
#     	motors.set_moving_speed({idLeft:0, idRight:0})

#     	rotate(teta_optometry, teta)

#     if(x>x_opto and y<y_opto):
#     	 while(x != x_opto):
#            motors.set_moving_speed({idLeft: v, idRight: -v})
#         motors.set_moving_speed({idLeft:0, idRight:0})
        
#         rotate_angle_clockwise(90)
#         while(y != y_opto):
#            motors.set_moving_speed({idLeft: v, idRight: -v})
#         motors.set_moving_speed({idLeft:0, idRight:0})

#         rotate(teta_optometry, teta)

#     if(x<x_opto and y>y_opto):
#         rotate_angle_clockwise(180)
#     	 while(x != x_opto):
#            motors.set_moving_speed({idLeft: v, idRight: -v})
#         motors.set_moving_speed({idLeft:0, idRight:0})
        
#         rotate_angle_clockwise(90)
#         while(y != y_opto):
#            motors.set_moving_speed({idLeft: v, idRight: -v})
#         motors.set_moving_speed({idLeft:0, idRight:0})

#         rotate(teta_optometry, teta)

#    	if(x<x_opto and y<y_opto):
#         rotate_angle_clockwise(180)
#    		 while(x != x_opto):
#            motors.set_moving_speed({idLeft: v, idRight: -v})
#         motors.set_moving_speed({idLeft:0, idRight:0})
        
#         rotate_angle_anticlockwise(90)
#         while(y != y_opto):
#            motors.set_moving_speed({idLeft: v, idRight: -v})
#         motors.set_moving_speed({idLeft:0, idRight:0})

#         rotate(teta_optometry, teta)


# def rotate(inicial_angle, final_angle):
#     if(final_angle > inicial_angle):
#         angle= final_angle - inicial_angle
#         rotate_angle_anticlockwise(angle)

#     if(inicial_angle > final_angle):
#         angle = inicial_angle - final_angle
#         rotate_angle_clockwise(angle)

def inverse_kinematics(xpoint,tetapoint):
    vl=xpoint-(tetapoint*Odometry.ROBOT_WIDTH/2)
    vr=xpoint+tetapoint*Odometry.ROBOT_WIDTH/2
    return vl, vr

def go_to_xya(x,y,teta,dxl_io : dyn.DxlIO):
    x0=Odometry.xn
    y0=Odometry.yn
    teta0=5/3*math.pi

    tetapoint=360

    dteta=teta0-teta
    #print("dteta : {}, teta0 {}, tetan : {}".format(dteta,teta0,teta))
    if(dteta>0):
        rotate_angle_anticlockwise(dteta)
        #vl,vr=inverse_kinematics(0,tetapoint)
    else:
        rotate_angle_clockwise(abs(dteta))
        #vl,vr=-inverse_kinematics(0,tetapoint)

    #dt_rotation=dteta/tetapoint

    d=math.sqrt((x-Odometry.xn)**2+(y-Odometry.xn)**2)
    xpoint=0.1
    vl,vr=inverse_kinematics(xpoint,0)
    vl=(vl*180)/(math.pi*Odometry.RADIUS_WHEEL)
    vr=(vr*180)/(math.pi*Odometry.RADIUS_WHEEL)
    dt_linear=d/xpoint
    print("vl : {}, vr : {}".format(vl,vr))
    dxl_io.set_moving_speed({idLeft: vl,idRight: -vr})
    time.sleep(dt_linear)
    dxl_io.set_moving_speed({idLeft: 0, idRight: 0})


ports = dyn.get_available_ports()
if not ports:
    exit('No port')

dxl_io = dyn.DxlIO(ports[0])
dxl_io.set_wheel_mode([5, 2])
#while 1:
#    print(dxl_io.get_present_position([idLeft,ifRight]))
#dxl_io.set_moving_speed({idLeft: v, idRight: -v})
#time.sleep(2)
#rotate_angle_clockwise(math.pi)
go_to_xya(0.5,0.5,180*math.pi/180)
#stop()
