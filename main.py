# Programmers:  Caitlin Burns, Leif LaBianca
# Course:  CS151, Prof. Zelalem
# Due Date: Oct. 3, 12:15
# Programming Assignment:  Lab03
# Problem Statement:  Calculates the distance travelled and points earned by a long jumper in a normal or long event given the speed of said jumper
# Data In: Jump height, points per meter, par distance, jumper speed
# Data Out:  Time in the air, jumper forward distance, jumper points awarded
# Credits:  All original code

# imports python's built-in math module
import math

# requests a normal or large jump query from the user
normal_or_large = str.lower(input("Are you performing a normal or large jump? "))

# sets jump height, points per meter, or par distance according to user input
# outputs an error message if something other than "normal" or "large" is input
if normal_or_large == "normal":
    jump_height = 46
    points_per_meter = 2
    par_distance = 90
elif normal_or_large == "large":
    jump_height = 70
    points_per_meter = 1.8
    par_distance = 120
else:
    print('This value is not accepted. Run the program again and type either "normal" or "large"')

# calculates the total time the jumper spends in the air
time_in_air = math.sqrt((2*jump_height)/9.8)

# requests the speed of the jumper from the user
jumper_speed = float(input("How fast are you going during the jump? "))

# calculates the forward distance travelled by the jumper
jumper_distance = jumper_speed * time_in_air

# calculates the points earned by the jumper
jumper_points = 60 + (jumper_distance - par_distance) * points_per_meter

# outputs the distance jumped forward and the points awarded
print(f'You jumped forward {jumper_distance} units and earned {jumper_points} points')

# outputs an approving, confused, or consoling phrase given the point count
if jumper_points > 60:
    print('Great job for doing better than par!')
elif jumper_points < 10:
    print('What happened??')
else:
    print("Sorry you didn't go very far")
