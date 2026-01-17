# Username Generator for Android
# By x9hg (Central)
# Works on Termux or Pydroid 3

import random
import time

letters = "abcdefghijklmnopqrstuvwxyz"
digits = "123456789"

# Mode selection
print("Select mode:")
print("1 - 3 Letters + 1 Digit (3L-1C)")
print("2 - 4 Characters (4C)")
mode = input("Enter 1 or 2: ")

# Pause time between usernames
pause_time = 1.5

while True:
    if mode == "1":
        # Generate 3L-1C username
        username = ''.join(random.choices(letters, k=3)) + random.choice(digits)
    elif mode == "2":
        # Generate 4C username (letters and digits)
        username = ''.join(random.choices(letters + digits, k=4))
    else:
        print("Invalid mode. Exiting.")
        break

    print(username)  # Print username for Android terminal
    time.sleep(pause_time)
