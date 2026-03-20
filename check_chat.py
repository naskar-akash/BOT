# Function to get last line from chat_history
def extract_last_message(chat_history):
    lines = chat_history.strip().split("\n")

    for line in reversed(lines):
        if "]" in line and ":" in line:
            return line
        


# Function to extract sender's name
def extract_sender(line):
    try:
        line_after_bracket = line.split("]", 1)[1]
        sender = line_after_bracket.split(":", 1)[0].strip()
        return sender
    except:
        return None
    
# Checking if last message from targeted user or not
def is_msg_from_target(chat_history, target_name):
    line = extract_last_message(chat_history)
    if line:
        sender = extract_sender(line)
        if sender == target_name:
            return True
        else: 
            return False
    else:
        return False
    