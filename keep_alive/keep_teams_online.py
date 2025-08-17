import time
import pyautogui

# Move the mouse slightly every 4 minutes to keep Teams online
interval = 240  # seconds (4 minutes)

print("Keep Teams Online script started. Press Ctrl+C to stop.")

try:
    while True:
        x, y = pyautogui.position()
        pyautogui.moveTo(x+1, y+1, duration=0.1)
        pyautogui.moveTo(x, y, duration=0.1)
        time.sleep(interval)
except KeyboardInterrupt:
    print("Script stopped.")
