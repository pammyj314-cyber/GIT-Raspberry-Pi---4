from sense_hat import SenseHat 
import random 
import time 
 
sense = SenseHat() 
 
# ----------------------------- 
# GAME SETTINGS 
# ----------------------------- 
 
MAX_ROUNDS = 5 
MAX_LIVES = 3 
TIME_LIMIT = 2 
 
 
# ----------------------------- 
# COLOURS 
# ----------------------------- 
 
RED = (255, 0, 0) 
GREEN = (0, 255, 0) 
WHITE = (255, 255, 255) 
BLACK = (0, 0, 0) 
 
 
# ----------------------------- 
# ARROW DESIGNS 
# ----------------------------- 
 
ARROWS = { 
 
    "up": [ 
        BLACK, BLACK, BLACK, WHITE, BLACK, BLACK, BLACK, BLACK, 
        BLACK, BLACK, WHITE, WHITE, WHITE, BLACK, BLACK, BLACK, 
        BLACK, WHITE, WHITE, WHITE, WHITE, WHITE, BLACK, BLACK, 
        WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, BLACK, 
        BLACK, BLACK, BLACK, WHITE, BLACK, BLACK, BLACK, BLACK, 
        BLACK, BLACK, BLACK, WHITE, BLACK, BLACK, BLACK, BLACK, 
        BLACK, BLACK, BLACK, WHITE, BLACK, BLACK, BLACK, BLACK, 
        BLACK, BLACK, BLACK, WHITE, BLACK, BLACK, BLACK, BLACK 
    ], 
 
    "down": [ 
        BLACK, BLACK, BLACK, WHITE, BLACK, BLACK, BLACK, BLACK, 
        BLACK, BLACK, BLACK, WHITE, BLACK, BLACK, BLACK, BLACK, 
        BLACK, BLACK, BLACK, WHITE, BLACK, BLACK, BLACK, BLACK, 
        BLACK, BLACK, BLACK, WHITE, BLACK, BLACK, BLACK, BLACK, 
        WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, BLACK, 
        BLACK, WHITE, WHITE, WHITE, WHITE, WHITE, BLACK, BLACK, 
        BLACK, BLACK, WHITE, WHITE, WHITE, BLACK, BLACK, BLACK, 
        BLACK, BLACK, BLACK, WHITE, BLACK, BLACK, BLACK, BLACK 
    ], 
 
    "left": [ 
        BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, 
        BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, 
        BLACK, BLACK, WHITE, BLACK, BLACK, BLACK, BLACK, BLACK, 
        BLACK, WHITE, WHITE, WHITE, WHITE, BLACK, BLACK, BLACK, 
        WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, 
        BLACK, WHITE, WHITE, WHITE, WHITE, BLACK, BLACK, BLACK, 
        BLACK, BLACK, WHITE, BLACK, BLACK, BLACK, BLACK, BLACK, 
        BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK 
    ], 
 
    "right": [ 
        BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, 
        BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, 
        BLACK, BLACK, BLACK, BLACK, WHITE, BLACK, BLACK, BLACK, 
        BLACK, BLACK, BLACK, WHITE, WHITE, WHITE, BLACK, BLACK, 
        WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, 
        BLACK, BLACK, BLACK, WHITE, WHITE, WHITE, BLACK, BLACK, 
        BLACK, BLACK, BLACK, BLACK, WHITE, BLACK, BLACK, BLACK, 
        BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK 
    ] 
} 
 
 
# ----------------------------- 
# SHOW ARROW 
# ----------------------------- 
 
def show_arrow(direction): 
    sense.set_pixels(ARROWS[direction]) 
 
 
# ----------------------------- 
# CLEAR LED 
# ----------------------------- 
 
def clear_screen(): 
    sense.clear() 
 
 
# ----------------------------- 
# SHOW LIVES 
# ----------------------------- 
 
def show_lives(lives): 
 
    sense.clear() 
 
    # Each heart is represented by a simple pattern. 
    # We use the bottom part of the LED matrix. 
 
    heart = [ 
        BLACK, RED, RED, BLACK, RED, RED, BLACK, BLACK, 
        RED, RED, RED, RED, RED, RED, RED, BLACK, 
        RED, RED, RED, RED, RED, RED, RED, BLACK, 
        BLACK, RED, RED, RED, RED, RED, BLACK, BLACK, 
        BLACK, BLACK, RED, RED, RED, BLACK, BLACK, BLACK, 
        BLACK, BLACK, BLACK, RED, BLACK, BLACK, BLACK, BLACK 
    ] 
 
    # Display hearts next to each other 
    # according to the number of lives. 
 
    for life in range(lives): 
 
        start_x = life * 3 
 
        for y in range(6): 
            for x in range(2): 
 
                pixel_x = start_x + x 
 
                if pixel_x < 8: 
                    index = y * 8 + pixel_x 
 
                    if index < len(heart) and heart[index] != BLACK: 
                        sense.set_pixel(pixel_x, y, RED) 
 
 
# ----------------------------- 
# RAINBOW GAME OVER EFFECT 
# ----------------------------- 
 
def rainbow_flash(): 
 
    rainbow = [ 
        (255, 0, 0),       # Red 
        (255, 127, 0),     # Orange 
        (255, 255, 0),     # Yellow 
        (0, 255, 0),       # Green 
        (0, 0, 255),       # Blue 
        (75, 0, 130),      # Indigo 
        (148, 0, 211)      # Violet 
    ] 
 
    for colour in rainbow: 
 
        sense.clear(colour) 
 
        time.sleep(0.15) 
 
    sense.clear() 
 
 
# ----------------------------- 
# GAME OVER 
# ----------------------------- 
 
def game_over(score): 
 
    sense.clear() 
 
    print("GAME OVER!") 
    print("Final Score:", score) 
 
    # Flash rainbow lights 
    for i in range(3): 
        rainbow_flash() 
 
    # Display final score in the terminal 
    print("Final Score:", score) 
 
    time.sleep(2) 
 
    sense.clear() 
 
 
# ----------------------------- 
# MAIN GAME 
# ----------------------------- 
 
def play_game(): 
 
    score = 0 
    lives = MAX_LIVES 
 
    print("-----------------------------") 
    print("      ARROW REACTION GAME") 
    print("-----------------------------") 
    print("You have", lives, "lives.") 
    print("You have", MAX_ROUNDS, "rounds.") 
    print() 
 
    # Show starting lives 
    show_lives(lives) 
    time.sleep(1) 
 
    clear_screen() 
 
    # ------------------------- 
    # GAME LOOP 
    # ------------------------- 
 
    for round_number in range(1, MAX_ROUNDS + 1): 
 
        print("Round", round_number) 
 
        # Randomly choose an arrow 
        direction = random.choice( 
            ["up", "down", "left", "right"] 
        ) 
 
        # Show the arrow 
        show_arrow(direction) 
 
        # Record the time when arrow appears 
        start_time = time.time() 
 
        # Wait for joystick input 
        event = sense.stick.wait_for_event() 
 
        # Calculate reaction time 
        reaction_time = time.time() - start_time 
 
        # Check what direction the player moved 
        player_direction = event.direction 
 
        print("Arrow:", direction) 
        print("Player:", player_direction) 
        print("Reaction time:", round(reaction_time, 2), "seconds") 
 
        # ------------------------- 
        # CHECK ANSWER 
        # ------------------------- 
 
        if ( 
            event.action == "pressed" 
            and player_direction == direction 
            and reaction_time <= TIME_LIMIT 
        ): 
 
            # CORRECT 
            score += 1 
 
            print("CORRECT!") 
            print("Score:", score) 
 
            sense.clear(GREEN) 
            time.sleep(0.3) 
 
        else: 
 
            # WRONG / TOO SLOW 
            lives -= 1 
 
            print("WRONG!") 
            print("Lives remaining:", lives) 
 
            sense.clear(RED) 
            time.sleep(0.3) 
 
            # Check if player has lost all lives 
            if lives <= 0: 
                game_over(score) 
                return 
 
        # Clear screen before next round 
        clear_screen() 
 
        # Short pause 
        time.sleep(0.3) 
 
    # ----------------------------- 
    # PLAYER SURVIVED ALL 5 ROUNDS 
    # ----------------------------- 
 
    clear_screen() 
 
    print("-----------------------------") 
    print("       YOU FINISHED!") 
    print("-----------------------------") 
    print("Final Score:", score) 
 
    # Display a green success screen 
    sense.clear(GREEN) 
 
    time.sleep(2) 
 
    clear_screen() 
 
 
# ----------------------------- 
# START GAME 
# ----------------------------- 
 
try: 
    play_game() 
 
except KeyboardInterrupt: 
 
    # Allow Ctrl + C to safely stop the program 
    sense.clear() 
 
    print() 
    print("Game stopped.") 
 
finally: 
 
    sense.clear()
