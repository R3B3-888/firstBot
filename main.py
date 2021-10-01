import sys
from scripts.line_following import line_following
from scripts.go_to import go_to_xya
from scripts import run_odometry
from scripts.drawing_the_map import draw_the_map
from constants import *


def get_chosen_goal(goal):
    if goal == '1':
        chosen_goal = "line following"
    elif goal == '2':
        chosen_goal = "go to"
    elif goal == '3':
        chosen_goal = "odometry"
    print("You have choose", chosen_goal)


def is_map_drawing_accepted():
    do_y_n = None
    while do_y_n not in ['y', 'n']:
        do_y_n = input("Do the map drawing at the end ? [y/n] ")
    if do_y_n == 'y':
        return True
    return False


def launch_chosen_goal(goal):
    if goal == '1':
        # goal = '4' if is_map_drawing_accepted() else "End"
        line_following()
    if goal == '2':
        go_to_xya(2, 4, 2)
    if goal == '3':
        print("Odometry is chosen")
        run_odometry()
    if goal == '4':
        draw_the_map()
    print("End of the ride")


def main(argc=len(sys.argv), argv=sys.argv):
    goal = None
    if argc == 1:
        goal = input("Pass a goal between 1 and 3 : ")
        while goal not in OPTIONS_AVAILABLE:
            print("Not an option available")
            goal = input("Pass a goal between 1 and 3 : ")
    else:
        goal = argv[1]
    get_chosen_goal(goal)
    launch_chosen_goal(goal)

if __name__ == "__main__":
        main()