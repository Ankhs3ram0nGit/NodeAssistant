import pyautogui
import keyboard
import pyperclip
import time

text = ""
lines = []
result = []

def get_clipboard_text():
    """Returns the current clipboard text."""
    global text
    try:
        text = pyperclip.paste()
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def seperate_by_linebreak():
    """Separates the clipboard text by line breaks."""
    global lines
    if get_clipboard_text() == True:
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        print(f"Lines: {lines}")  # Debugging line

def process_code1():
    """Processes lines to replace '| string' with ' '."""
    global lines
    for i in range(len(lines)):
        line = lines[i]
        if "@" in line:
            lines[i] = line.replace("| string", " ' ")
    print(f"Processed Lines: {lines}")  # Debugging line

def process_code2():
    """Processes lines to split by single quotes and append parts to result."""
    global lines, result
    for line in lines:
        parts = line.split("'")
        for i in range(len(parts)):
            part = parts[i].strip()
            if part:
                result.append(part)
            if i < len(parts) - 1:
                result.append("'")
    print(f"Result: {result}")  # Debugging line

def paste_processed():
    """Simulates pasting each element from result."""
    global result
    pyautogui.click()  # Ensure the target application is in focus
    time.sleep(1)  # Allow time for focus

    for resultee in result:
        print(f"Pasting: {resultee}")  # Debugging line
        if resultee != "'":
            pyperclip.copy(resultee)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.keyDown('shift')
            pyautogui.press('enter')
            pyautogui.keyUp('shift')
        else:
            pyautogui.keyDown('shift')
            pyautogui.press('enter')
            pyautogui.keyUp('shift')
        time.sleep(0.5)  # Ensure each element is processed

def on_shortcut():
    """Handles the shortcut trigger."""
    get_clipboard_text()
    seperate_by_linebreak()
    process_code1()
    process_code2()
    paste_processed()

def main():
    """Main function to set up hotkeys and run the script."""
    shortcut = 'ctrl+alt+r'
    keyboard.add_hotkey(shortcut, on_shortcut)
    print(f"Listening for shortcut '{shortcut}'...")
    keyboard.wait('esc')

if __name__ == "__main__":
    main()
