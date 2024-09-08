from setuptools import setup

APP = ['hotkey_script.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['pyautogui', 'pyperclip', 'pynput'],
    'plist': {
        'CFBundleName': 'HotkeyApp',
        'CFBundleIdentifier': 'com.yourname.hotkeyapp',
        'CFBundleVersion': '0.1.0',
        'CFBundleExecutable': 'HotkeyApp',
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
