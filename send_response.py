import pyautogui
import pyperclip
from ai_model import ask_chatgpt
import time

chat_x, chat_y = 1360, 974    # click to write response

def Response(text):

    # provide this text to chatgpt and getting response from there
    response = ask_chatgpt(text)
    pyperclip.copy(response)

        # click to the chat box
    pyautogui.click(chat_x,chat_y)
    time.sleep(0.5)

        # Paste response to the chatbox
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2.0)

        # press enter
    pyautogui.press('enter')

    