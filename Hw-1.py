from random import random
from statistics import mean
from statistics import pstdev

break_points = [0, 0, 0, 0, 0, 0, 0]

for i in range(7):
    step = 1/6
    break_points[i] = step*i

Dice = [0, 0, 0, 0, 0, 0]

N_throws = int(input("How many dice you want us to throw?"))

for i in range(N_throws):
    rand_val = random()
    for j in range(6):
        if (rand_val >= break_points[j]) and (rand_val < break_points[j+1]):
            Dice[j] += 1
            break

dice_probability = [0, 0, 0, 0, 0, 0]
for i in range(6):
    dice_probability[i] = Dice[i]/N_throws



print(f"The probability set is: {dice_probability}")

RMS = pstdev(dice_probability)

print(f"The Root-Mean-Square is: {RMS}")

validation = RMS < (N_throws**(-0.5))

print(f"Dose this RMS agree with Fluctuation-dissipation theorem? : {validation}")






















