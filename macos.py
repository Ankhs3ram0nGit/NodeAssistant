import pyautogui
import pyperclip
import time
from pynput import keyboard  # Importing pynput for hotkey handling

# Global variables to store SMS and Email text
sms = []
email = []

def format_and_print(text_list):
    """Formats and prints the text from the given list."""
    for text in text_list:
        print(text)
        time.sleep(0.1)  # Optional: small delay to simulate typing

def simulate_keypress(text_list):
    """Simulates keypress for the given list of texts."""
    time.sleep(0.5)  # Ensure the target application is in focus

    for text in text_list:
        pyperclip.copy(text)
        pyautogui.hotkey('cmd', 'v')  # Paste the text using Cmd+V on macOS
        pyautogui.keyDown('shift')
        pyautogui.press('enter')
        pyautogui.keyUp('shift')

        # Check if '@' is in the text
        if "@" in text:
            pyautogui.press('backspace')

        time.sleep(0.2)  # Small delay to ensure Shift + Enter is processed

def on_sms_shortcut():
    """Handles the SMS input shortcut"""
    print("SMS shortcut triggered. Simulating keypress...")
    simulate_keypress(sms)

def on_email_shortcut():
    """Handles the Email input shortcut"""
    print("Email shortcut triggered. Simulating keypress...")
    simulate_keypress(email)

def get_user_input():
    """Collects SMS and Email inputs from the user"""
    global sms, email

    print("(use ' for line breaks ' ' for multiple line breaks. Eg: Dear representative of @applicantName ' , ' ' Contents of the message.)")
    print("Enter text for SMS: ")
    sms_text = input()
    sms = [element.strip() for element in sms_text.split("'")]

    print("Enter text for Email: ")
    email_text = input()
    email = [element.strip() for element in email_text.split("'")]

def main():
    # Collect user input before starting to listen for shortcuts
    get_user_input()

    # Define the shortcut key combinations
    sms_shortcut = '<cmd>+<alt>+r'
    email_shortcut = '<cmd>+<alt>+f'

    # Define a listener for the keyboard shortcuts
    with keyboard.GlobalHotKeys({
        sms_shortcut: on_sms_shortcut,
        email_shortcut: on_email_shortcut
    }) as hotkey_listener:
        print(f"Listening for SMS shortcut '{sms_shortcut}' and Email shortcut '{email_shortcut}'...")
        hotkey_listener.join()  # Keep listening for hotkeys

if __name__ == "__main__":
    main()
