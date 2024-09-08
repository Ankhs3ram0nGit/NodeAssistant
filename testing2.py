import pyautogui
import pyperclip
import time
from pynput import keyboard
from AppKit import NSPasteboard, NSPasteboardTypeString

# Global variables to store SMS and Email text
sms = []
email = []

def format_and_print(text_list):
    """ Formats and prints the text from the given list. """
    for text in text_list:
        print(text)
        time.sleep(0.1)  # Optional: small delay to simulate typing

def simulate_keypress(text_list):
    """ Simulates keypress for the given list of texts. """
    time.sleep(0.5)  # Ensure the target application is in focus

    for text in text_list:
        pyperclip.copy(text)
        pyautogui.hotkey('command', 'v')  # Paste the text using Command+V on macOS
        pyautogui.keyDown('shift')
        pyautogui.press('enter')
        pyautogui.keyUp('shift')
        time.sleep(0.2)  # Ensure Shift + Enter is processed

def on_sms_shortcut():
    """ Handles the SMS input shortcut """
    print("SMS shortcut triggered. Simulating keypress...")
    simulate_keypress(sms)

def on_email_shortcut():
    """ Handles the Email input shortcut """
    print("Email shortcut triggered. Simulating keypress...")
    simulate_keypress(email)

def get_user_input():
    """ Collects SMS and Email inputs from the user """
    global sms, email

    print("(use ' for line breaks ' ' for multiple line breaks. Eg: Dear represantative of @applicantName ' , ' ' Contents of the meesage.)")
    print("Enter text for SMS: ")
    sms_text = input()
    sms = [element.strip() for element in sms_text.split("'")]

    print("Enter text for Email: ")
    email_text = input()
    email = [element.strip() for element in email_text.split("'")]

def on_press(key):
    """ Handles key press events for shortcuts """
    if key == keyboard.Key.ctrl_l and keyboard.Key.alt_l in current_keys:
        if keyboard.KeyCode.from_char('r') in current_keys:
            on_sms_shortcut()
        elif keyboard.KeyCode.from_char('f') in current_keys:
            on_email_shortcut()

def on_release(key):
    """ Handles key release events """
    if key in current_keys:
        current_keys.remove(key)

def main():
    global current_keys
    current_keys = set()

    # Collect user input before starting to listen for shortcuts
    get_user_input()

    # Set up hotkey listeners for the defined shortcuts
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        print("Listening for SMS and Email shortcuts...")
        listener.join()

if __name__ == "__main__":
    main()
