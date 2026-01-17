# 4C Username Generator
# By x9hg (Central)

import random
import pyperclip
import pyautogui
import time

letters = "abcdefghijklmnopqrstuvwxyz"
digits = "1234567894"

# Generation of 4-character combinations
combos = [a + b + c + d for a in letters for b in digits for c in letters for d in digits]
random.shuffle(combos)

print("The script will automatically replace the 4-character usernames (without pressing Enter).")
time.sleep(5)  # Time to place the cursor in the target field

i = 0
while True:
    if i >= len(combos):
        random.shuffle(combos)  # Shuffle again and restart
        i = 0

    pseudo = combos[i]

    # Delete the old username (4 characters)
    pyautogui.press('backspace', presses=4)
    
    # Copy and paste the new username
    pyperclip.copy(pseudo)
    pyautogui.hotkey('ctrl', 'v')

    print(f"Pasted: {pseudo}")
    i += 1
    time.sleep(2)  # Pause between each username