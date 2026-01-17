# 3L-1C Username Generator
# By x9hg (Central)

import random
import pyperclip
import pyautogui
import time

letters = "abcdefghijklmnopqrstuvwxyz"
digits = "123456789"

print("The script will automatically replace the 3L-1C usernames (without pressing Enter).")
time.sleep(5)  # Time to place the cursor in the target field

while True:
    # Generate a 3L-1C username
    pseudo = ''.join(random.choices(letters, k=3)) + random.choice(digits)

    # Delete the old username (4 characters)
    pyautogui.press('backspace', presses=4)
    
    # Copy and paste the new username
    pyperclip.copy(pseudo)
    pyautogui.hotkey('ctrl', 'v')

    print(f"Pasted: {pseudo}")
    time.sleep(2)  # Pause between each username
