# By x9hg // Central

import random
import pyperclip
import pyautogui
import time
from colorama import Fore, init
import shutil

init(autoreset=True)

# Terminal width for centering
term_width = shutil.get_terminal_size().columns

def center_text(text, width=term_width):
    """Center text for terminal display"""
    return text.center(width)

# Custom eagle ASCII formatted for centering
custom_eagle = r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⠟⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⡿⠁⠀⢹⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡟⢿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡿⠁⠀⠀⠘⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⡟⠀⠀⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣴⣿⣧⠀⠀⠀⠀⢀⣿⣿⠁⠀⠀⠀⠀⢻⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⠏⠀⠀⠀⠈⢿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣼⣿⠋⢿⣷⡀⠀⠀⣸⣿⡇⠀⠀⠀⠀⠀⠀⠹⣿⣷⣤⣤⣤⣤⣤⣴⣶⣶⣶⣦⣤⣤⣄⣀⣀⠀⠀⠀⠀⢀⣠⣾⡟⠁⠀⠀⠀⠀⠀⢸⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢰⣿⠏⠀⠈⢿⣷⠀⢠⣿⣿⠀⠀⠀⢀⣠⣴⣶⣿⡿⠿⠛⠉⠉⠉⠉⠉⠀⠀⠉⠉⠉⠉⠛⠿⠿⣿⣶⣦⣴⣾⠿⠉⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠
⢸⣿⠀⠀⠀⠈⢿⣧⢸⣿⡇⠀⣠⣶⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣾⣿
⣾⣿⠀⠀⠀⠀⠘⣿⣾⣿⣧⣾⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣦⡀⠀⠀⠀⠀⢰⣿⣿⠀⠀⢀⣠⣤⣶⣿⡿⠟⠋⣼⣿
⢿⣿⠀⠀⠀⠀⠀⠘⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣦⡀⠀⠀⢸⣿⣏⣠⣶⣿⡿⠟⠋⠁⠀⠀⢠⣿⡇
⢸⣿⠀⡆⠀⠀⠀⠀⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣄⢀⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⣾⣿⠁
⢸⣿⡀⢷⠀⠀⠀⣼⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣾⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⠃⠀
⠀⣿⣷⠸⡆⠀⢰⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⡏⠀⠀⠀⡀⠀⠀⠀⢀⣼⣿⠏⠀⠀
⠀⠹⣿⡆⢹⡆⣾⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⡇⢠⡴⠊⠁⠀⠀⢀⣾⣿⠏⠀⠀⠀
⠀⠀⢻⣿⡄⠻⣿⣿⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⡟⠀⠀⠀⠀⣠⣿⡿⠃⠀⠀⠀⠀
⠀⠀⠀⢿⣷⣼⣿⠛⣿⡿⢿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣴⣶⣶⡾⠃⠀⠀⠀⣿⣿⠀⠀⠀⢠⣾⣿⠟⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠈⣻⣿⠟⠀⢿⣇⠀⠈⠙⠻⢷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣶⣶⠾⠿⠿⠛⠋⠉⣹⣿⠇⠀⠀⠀⠀⢸⣿⠀⣠⣶⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣴⣿⠋⠀⠀⠸⣿⣆⠀⠀⠀⠀⠈⠙⠻⣷⣄⡇⠀⠀⣇⣀⣤⣤⣶⣾⡿⠟⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⣰⣿⡏⠀⠀⠀⠀⠀⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣸⣿⠇⠀⠀⠀⠀⠘⢿⣦⡀⠀⠀⠀⠀⢀⣿⠉⠉⠀⠀⠛⠹⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⢏⡰⠋⠀⠀⠀⢠⣿⡿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠘⠻⢿⣶⣦⣤⣴⡿⠏⠀⠀⠀⠀⠀⠀⠘⢿⣷⣦⣀⡀⠀⠀⠀⠀⠀⢀⣀⣤⣶⣿⣿⠗⠋⠀⠀⠀⠀⢀⣼⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠹⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⢿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⣼⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠙⣿⣧⣀⠀⠀⠀⠀⠀⠀⣠⣶⡄⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠻⣿⣶⣄⠀⠀⠀⠼⠋⢸⣇⢀⣴⠟⠛⣷⠀⠀⣠⡶⢶⡀⠀⢠⣷⡀⠀⠀⣠⠾⢦⡀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠛⠿⣿⣦⣄⠀⠀⠀⠻⠟⠁⠀⠀⢸⣷⠞⠋⠀⠈⢷⣤⠟⠘⢧⣤⠞⠁⠀⠀⠙⢄⠀⠀⠀⠀⣀⣴⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠈⠋⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⢁⣠⣤⣾⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣶⣦⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣴⣶⣾⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣶⣤⣀⡀⠉⠙⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⠟⠛⢿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣾⡿⢛⣁⡀⠉⠛⠛⠿⠿⠿⠿⠿⠛⠀⠀⠀⡀⠀⠀⠀⠀⢀⣾⡿⠃⠀⠀⢠⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣧⡿⠻⣿⡿⠷⠂⠀⠀⠀⠀⠀⠀⣠⣤⣀⣹⣦⠀⢀⣠⣾⡟⠁⠀⠀⢀⣿⣿⣿⣄⣠⣴⣶⣿⣿⣿⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⠁⣼⡿⢡⣴⣤⣤⣤⣤⣤⣤⣾⣟⡙⠛⠻⠿⠿⠿⠛⠉⠀⠀⠀⣰⣿⡟⠁⢻⣿⡟⠋⣁⣤⣤⣀⠉⠻⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣷⣿⠋⠉⠉⠛⠛⠛⢻⣿⠟⣻⣷⠄⠀⠀⠀⣀⣀⣀⣤⣾⡿⠋⠀⠀⢸⣿⣷⡿⠛⠋⠙⠻⣷⡀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠁⠀⠀⠀⠀⠀⠀⠈⠃⣴⣿⢁⣴⣶⣿⠿⠿⠿⠟⠛⠉⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⢹⣷⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⣆⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠈⣿⡄⣿⣿⡀⠀⢀⣠⣴⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣟⠁⢤⣤⣤⣤⣤⣄⣀⣹⣷⣄⠀⠀⠈⠛⠻⣿⣦⡀⠀⢠⣰⣿⡇⠘⠻⠿⠿⠟⣻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣷⡄⠀⠈⠉⢻⣿⠛⠛⠛⢿⣦⠀⠀⣀⣀⡈⣿⣧⡀⠘⣿⣯⡁⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠟⠁⠀⠀⠀⠀⢀⣴⣿⠟⠀⠀⠀⠈⠻⣿⣿⡛⠁⠀⠈⢿⣷⡀⠈⠻⢿⣶⣤⡀⠀⢀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⣿⣧⣤⣤⣤⣀⣀⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠈⣻⣿⡆⠀⠀⠈⠛⢿⣦⣼⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢉⠉⠉⠛⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡷⠿⠿⠿⠿⠟⠛⠋⠀⠀⠀⠀⠀⠙⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

# Print custom eagle in red
for line in custom_eagle.splitlines():
    print(center_text(Fore.RED + line))

# Letters and digits
letters = "abcdefghijklmnopqrstuvwxyz"
digits = "123456789"

# Mode selection centered and red
separator = "="*60
print(Fore.RED + center_text(separator))
print(Fore.RED + center_text("SELECT USERNAME MODE"))
print(Fore.RED + center_text(separator))
print(Fore.RED + center_text("1 - 3 Letters + 1 Digit (3L-1C)"))
print(Fore.RED + center_text("2 - 4 Characters (4C)"))
print(Fore.RED + center_text("-"*60))

mode = input(Fore.RED + center_text("Enter 1 or 2: "))

# Pause before starting
print(Fore.RED + center_text("Place your cursor in the target field. The script will start in 5 seconds..."))
time.sleep(5)

# Pause between usernames
pause_time = 2

i = 0
combos_4c = []

# Generate 4C combos once if needed
if mode == "2":
    combos_4c = [a + b + c + d for a in letters for b in digits for c in letters for d in digits]
    random.shuffle(combos_4c)

while True:
    if mode == "1":
        # 3L-1C generation with digit at random position
        chars = random.choices(letters, k=3)
        digit = random.choice(digits)
        pos = random.randint(0, 3)
        chars.insert(pos, digit)
        username = ''.join(chars)
    elif mode == "2":
        # 4C generation from precomputed list
        if i >= len(combos_4c):
            random.shuffle(combos_4c)
            i = 0
        username = combos_4c[i]
        i += 1
    else:
        print(Fore.RED + center_text("Invalid mode! Exiting..."))
        break

    # Delete old username (4 chars for safety)
    pyautogui.press('backspace', presses=4)

    # Copy and paste
    pyperclip.copy(username)
    pyautogui.hotkey('ctrl', 'v')

    print(Fore.RED + center_text(f"Pasted: {username}"))
    time.sleep(pause_time)
