import pyautogui
import pyperclip
import time
from send_response import Response
from check_chat import is_msg_from_target


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

    while True:
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
        print(chat_history)

        # ✅ Only respond if message is from target
        if chat_history != last_message and is_msg_from_target(chat_history, TARGET_NAME):
            Response(chat_history)
            last_message = chat_history