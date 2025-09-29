# log_script.py
import datetime
import random
import os

LOG_FILE = "log.txt"

# List of motivational quotes
QUOTES = [
    "The best way to predict the future is to create it.",
    "Believe you can and you're halfway there.",
    "The only way to do great work is to love what you do.",
    "Strive not to be a success, but rather to be of value.",
    "Don't watch the clock; do what it does. Keep going."
]

def generate_log_entry():
    """Generates a formatted log entry."""
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    quote = random.choice(QUOTES)
    
    log_entry = (
        f"--- New Container Run ---\n"
        f"Timestamp: {now}\n"
        f"Quote: {quote}\n"
        f"Container execution completed.\n"
        f"-------------------------\n"
    )
    return log_entry

def append_to_log(log_entry):
    """Appends the log entry to the log file."""
    try:
        # 'a' mode means append
        with open(LOG_FILE, 'a') as f:
            f.write(log_entry + "\n")
        print(f"Log entry successfully appended to {LOG_FILE}")
        print(log_entry)
    except IOError as e:
        print(f"Error writing to file {LOG_FILE}: {e}")

if __name__ == "__main__":
    entry = generate_log_entry()
    append_to_log(entry)