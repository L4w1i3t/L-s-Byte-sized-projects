import pyautogui
import time
import threading

def start_autoclicker(interval):
    """
    Starts the autoclicker with the specified interval between clicks.
    
    :param interval: Time interval between clicks in seconds.
    """
    print("Autoclicker started. Press Ctrl+C to stop.")
    try:
        while True:
            pyautogui.click()  # Simulates a mouse click
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nAutoclicker stopped.")

def main():
    print("Welcome to the Autoclicker!")
    
    # Get the interval from the user
    while True:
        try:
            interval = float(input("Enter the interval between clicks (in seconds): "))
            if interval <= 0:
                print("Interval must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Start the autoclicker in a new thread
    clicker_thread = threading.Thread(target=start_autoclicker, args=(interval,))
    clicker_thread.start()

if __name__ == "__main__":
    main()
