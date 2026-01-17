Parfait ! Voici une version **complète pour GitHub**, incluant l’installation des dépendances et la possibilité d’utiliser **4C ou 3L+1C** :

---

# 🔤 4C / 3L-1C Username Generator

A simple and efficient **username generator**, developed by me (x9hg).
It can generate **4-character usernames (4C)** or **3 letters + 1 digit usernames (3L-1C)**.

This project creates short, clean, and unique usernames, combining selected letters and digits to produce compact, hard-to-guess names.

### Designed for:

* Gaming usernames 🎮
* Social media accounts 📱
* Automation and testing 🤖
* Username availability checks

### Features

* Random **4-character username generation (4C)**
* Random **3 letters + 1 digit username generation (3L-1C)**
* Uses custom letter and digit sets
* Automatic clipboard copy
* Optional auto-paste and replace functionality
* Infinite generation loop
* Lightweight and easy to use

### Installation

This project requires the following Python packages:

```bash
pip install pyperclip pyautogui
```

### Usage

1. Run the script:

```bash
python username_generator.py
```

2. Place your cursor in the target field.
3. The script will automatically generate and paste usernames.
4. Press **Ctrl+C** to stop the script.

### Notes

* For **4C usernames**, the script generates combinations of letters and digits like `a7b4`.
* For **3L-1C usernames**, the script generates usernames like `abc4`.
* You can adjust the speed by modifying `time.sleep()` in the script
