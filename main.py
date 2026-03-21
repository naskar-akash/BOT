import pyautogui
import pyperclip
import time
import keyboard
from send_response import Response
from check_chat import is_msg_from_target 

# global variable
running = True

# Function to stop function
def stop_bot():
    global running
    print("Stopping BOT....")
    running = False

# Moves mouse to top-left corner, program crashes instantly as it just slam your mouse to (0,0) → instant stop
pyautogui.FAILSAFE = True
# Key to stop BOT
keyboard.add_hotkey('esc', stop_bot)


if __name__ == "__main__":

    # --- SET YOUR COORDINATES AND VARIABLES HERE ---
    icon_x, icon_y = 1400, 1050    # coordinate of chrome icon
    start_x, start_y = 980, 275   # Starting point of selection
    end_x, end_y = 1380, 940       # Ending point of selection
    deselect_x, deselect_y = 1742, 896   # deselecting selected text
    TARGET_NAME = "My Home"
    last_message = ""
    

    # click on the chrome icon
    pyautogui.click(icon_x, icon_y)

    while running:
        time.sleep(2.0)

        # Move to start position, drag upto end and click
        pyautogui.moveTo(start_x, start_y, duration=0.5)
        pyautogui.dragTo(end_x, end_y, duration=1.5, button='left')
        time.sleep(0.5)

        # Copy selected text
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5)
        pyautogui.click(deselect_x, deselect_y)

        # Get clipboard data
        chat_history = pyperclip.paste()

        # ✅ Only respond if message is from target
        if chat_history != last_message and is_msg_from_target(chat_history, TARGET_NAME):
            Response(chat_history)
            last_message = chat_history