import pyautogui
import pyperclip
import time
from ai_model import ask_chatgpt


if __name__ == "__main__":

    # --- SET YOUR COORDINATES HERE ---
    icon_x, icon_y = 1400, 1050    # coordinate of chrome icon
    start_x, start_y = 1000, 310   # Starting point of selection
    end_x, end_y = 1380, 940       # Ending point of selection
    deselect_x, deselect_y = 1742, 896   # deselecting selected text

    # click on the chrome icon
    pyautogui.click(icon_x, icon_y)
    time.sleep(2.0)

    # Move to start position, drag upto end and click
    pyautogui.moveTo(start_x, start_y, duration=0.5)
    pyautogui.dragTo(end_x, end_y, duration=1.5, button='left')
    time.sleep(0.5)

    # Copy selected text
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1.0)
    pyautogui.click(deselect_x, deselect_y)

    # Get clipboard data
    text = pyperclip.paste()

    # provide this text to chatgpt and getting response from there
    response = ask_chatgpt(text)

    # Print result
    print("\nCopied Text:\n")
    print(text)
    print("\n response: \n")
    print(response)