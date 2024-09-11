import pyautogui
import keyboard
import pyperclip
import time

text = ""
lines = []

def get_clipboard_text():
    """Returns the current clipboard text."""
    global text
    try:
        text = pyperclip.paste()
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def add_delimiters():
    """Processes the clipboard text and adds delimiters after each line."""
    global lines
    if get_clipboard_text():
        # Separate the clipboard text by line breaks and process each line
        lines = []
        split_lines = [line.strip() for line in text.splitlines() if line.strip()]
        
        # Add delimiters between each line and handle multiple line breaks
        for i, line in enumerate(split_lines):
            processed_line = line
            if "@" in processed_line:
                processed_line = processed_line.replace("| string", "'")
            
            # Add a delimiter after each line except the last one
            if i < len(split_lines) - 1:
                processed_line += " ' , '  ' " if line.endswith(",") else " ' . '  ' "
            
            lines.append(processed_line)

        print(f"Processed Lines: {lines}")  # Debugging line


def process():
    for line in lines:
        print(line)

def paste():
    """Handles the pasting of each processed line with delimiters."""
    for line in lines:
        if "@" in line:
            pyperclip.copy(line)
            pyautogui.hotkey('ctrl', 'v')  # Paste the text
            pyautogui.keyDown('shift')
            pyautogui.press('enter')  # Simulate a line break
            pyautogui.keyUp('shift')
            pyautogui.press('backspace')
        elif line == "'": # Paste the text
            pyautogui.keyDown('shift')
            pyautogui.press('enter')  # Simulate a line break
            pyautogui.keyUp('shift')
        else:
            pyperclip.copy(line)
            pyautogui.hotkey('ctrl', 'v')  # Paste the text
            pyautogui.keyDown('shift')
            pyautogui.press('enter')  # Simulate a line break
            pyautogui.keyUp('shift')




def on_shortcut():
    """Handles the shortcut trigger."""
    get_clipboard_text()
    add_delimiters()
    process()


def main():
    """Main function to set up hotkeys and run the script."""
    shortcut = 'ctrl+alt+r'
    keyboard.add_hotkey(shortcut, on_shortcut)
    print(f"Listening for shortcut '{shortcut}'...")
    keyboard.wait('esc')

def remove_delimiters():
    """Removes the delimiters from the elements and keeps them in the same order."""



if __name__ == "__main__":
    main()
