#Reaction game 


import random
from sense_hat import SenseHat
import time

sense = SenseHat()

print("Game is starting!")


# Generate a random direction for the joystick
directions = random.choice([
    "⬆",
    "⬇", 
    "⬅", 
    "➡"
])

target_direction = directions

start_time = time.monotonic()


joystick_direction = None
while joystick_direction is None:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "up":
                joystick_direction = "⬆"
            elif event.direction == "down":
                joystick_direction = "⬇"
            elif event.direction == "left":
                joystick_direction = "⬅"
            elif event.direction == "right":
                joystick_direction = "➡"
                break

#Reaction time

TIME_LIMIT = 2.0

reaction_time = time.monotonic() - start_time

if joystick_direction is None:

    print("Too slow!")
    print(f"Your reaction time: {reaction_time:.2f} seconds")
    print("You lose!")

elif joystick_direction == target_direction:
    print("Correct direction!")
    print(f"Your reaction time: {reaction_time:.2f} seconds")
    print("You win!")

else:
    print("Wrong direction!")
    print(f"Your move: {joystick_direction}")
    print(f"Target direction: {target_direction}")
    print(f"Your reaction time: {reaction_time:.2f} seconds")
    print("You lose!")







