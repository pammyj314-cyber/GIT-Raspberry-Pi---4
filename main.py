#Reaction game 

TOTAL_ROUNDS = 3

import random
import time
from importlib import import_module

try:
    SenseHat = import_module("sense_hat").SenseHat
except ImportError as error:
    raise SystemExit(
        "The sense_hat package is required. Install it with: "
        "python -m pip install sense-hat"
    ) from error

print("Game is starting!")

sense = SenseHat() 


# Generate a random direction for the joystick
directions = random.choice([
    "⬆",
    "⬇", 
    "⬅", 
    "➡"
])

TIME_LIMIT = 2.0
TOTAL_ROUNDS = 3

for round_number in range(1, TOTAL_ROUNDS + 1):
    
    print(f"\n--- Round {round_number} ---")

    target_direction = random.choice(directions)

    start_time = time.monotonic()

    joystick_direction = None

    while joystick_direction is None:

        for event in sense.stick.get_events():

            if event.action == "pressed":

                if event.direction in directions:
                    joystick_direction = event.direction
                    break

        if time.monotonic() - start_time > TIME_LIMIT:
            break

        time.sleep(0.01)

    reaction_time = time.monotonic() - start_time

    print(f"Your reaction time: {reaction_time:.2f} seconds")

    if reaction_time > TIME_LIMIT:
        print("Too slow! You lose!")

    elif joystick_direction == target_direction:
        print("Correct direction!")
        print("You win!")

    else:
        print("Wrong direction!")
        print("You lose!")

    time.sleep(1)

print("\nGame over!")






