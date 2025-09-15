import pyautogui
import pyperclip
import time
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

# Securely access your API key
api_key = os.getenv("GEMINI")

# Now you can use it
genai.configure(api_key=api_key)

model = genai.GenerativeModel(
    'gemini-1.5-flash',
    system_instruction=
    """
    You are a person named Mayank who speaks English and Hindi, and enjoys cracking jokes while texting others. Analyze the chat history and respond like Mayank.
    just generate the last message to forward in chat.
    """
)
#AIzaSyBZ1BFc6nKOKFllAYc7CxtFKnMIeHjA9GU
# Function to check last message is from sender: 
def is_last_message_from(chat_log: str, sender: str) -> bool:
   
    lines = chat_log.strip().split("\n")

    last_sender = None
    last_message_lines = []

    for line in lines:
        if line.startswith("[") and "]" in line and ":" in line:
           
            try:
                sender_part = line.split("]")[1].strip()  
                current_sender = sender_part.split(":")[0].strip()
            except IndexError:
                continue

            last_sender = current_sender
            last_message_lines = [line]
        else:
            last_message_lines.append(line)

    return last_sender == sender

# Small delay so you can switch to the target window before script starts
time.sleep(3)

# Step 1: Click on the icon
pyautogui.click(1127, 1042)
time.sleep(1)
while True:
    # Step 2: Drag to select text
    pyautogui.moveTo(672, 200)
    pyautogui.dragTo(1884, 920, duration=1, button='left')
    time.sleep(1)

    # Step 3: Copy to clipboard (Ctrl+C)
    pyautogui.hotkey("ctrl", "c")
    time.sleep(1)
    pyautogui.click(1884, 920)

    # Step 4: Retrieve from clipboard
    chat_history = pyperclip.paste()
    print("Copied text:")
    print(chat_history) 
    
    # Step 5: check if the last message from the sender
    if is_last_message_from(chat_history, "Hardik"):

        response = model.generate_content(chat_history)

        pyautogui.click(1683, 975)
        time.sleep(0.5)
        text = response.text
        print(response.text)
        pyperclip.copy(text)

        # Step 6: Paste the text and press Enter
        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(1)
