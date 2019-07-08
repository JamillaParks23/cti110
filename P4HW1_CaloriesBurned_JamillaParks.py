# Writing a program that shows how many calories are burned.
# July 6, 2019
# CTI-110 P4HW1 - Calories Burned
# Jamilla Parks
#
#if 1 minute = 5 calories
# then 20 minutes = 100 calories
# then 35 minutes = 175 calories
# then 45 minutes = 225 calories

caloriesburnedperminute = 5
for numberOfMinutes in range(5,55, 15):
    numberOfCaloriesBurned = (numberOfMinutes / 1)* caloriesburnedperminute
    print('You will burn', numberOfCaloriesBurned,'in',numberOfMinutes)

