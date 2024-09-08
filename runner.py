import pyautogui
import keyboard
import pyperclip
import time

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
        pyautogui.hotkey('ctrl', 'v')  # Paste the text
        pyautogui.keyDown('shift')
        pyautogui.press('enter')
        pyautogui.keyUp('shift')

        # Handle the case where the text contains '@'
        if "@" in text:
            # Gets index of next element
            current_index = text_list.index(text)
            if current_index + 1 < len(text_list):
                next_text = text_list[current_index + 1]
                if next_text and next_text[0] in {",", "."}:
                    # Process additional actions for special characters
                    pyautogui.press('backspace')
        
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
    sms_shortcut = 'ctrl+alt+r'
    email_shortcut = 'ctrl+alt+f'

    # Set up hotkey listeners for the defined shortcuts
    keyboard.add_hotkey(sms_shortcut, on_sms_shortcut)
    keyboard.add_hotkey(email_shortcut, on_email_shortcut)

    print(f"Listening for SMS shortcut '{sms_shortcut}' and Email shortcut '{email_shortcut}'...")

    # Block the script to keep it running and listening for key events
    keyboard.wait('esc')

if __name__ == "__main__":
    main()
