# WhatsApp Auto Reply Bot

A Python-based automatic bot that opens whatsApp, reads the whatsApp messages from screen of the person with whom you are chatting and sends AI generated natural responses.

---

## Features

- Automaticalyy opens whatsApp tab
- Reads WhatsApp Web chat using screen selection
- Detects sender name from chat
- Generates replies using ChatGPT API
- Prevents duplicate replies
- Keyboard controls:
  - 🛑 `ESC` → Stop bot
  - ⏸️ `F9` → Pause / Resume bot

## Project Structure

- `main.py` # Entry point for the assistance
- `ai_model.py` # Generate response by interacting with chatGpt
- `check_chat.py` # Checks if the chat is fron the targeted person or not
- `send_response.py` # To type response to the chatbox and send it 
- `system_message.py` # Prompt for the machine
- `get_position.py` # To get the co-ordinates (initially used)
- `Readme.md`
- `.env`