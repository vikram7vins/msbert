import pyautogui, random, time

# Screen dimensions
screen_width, screen_height = pyautogui.size()


def move_mouse(pixel_distance, fixed_interval=None):
    """
    Moves the mouse at either fixed or random intervals.

    Parameters:
    pixel_distance (int): Number of pixels to move.
    fixed_interval (float or None): Time interval between movements (fixed or None for random between 0 to 4 mins).
    """
    while True:
        x, y = pyautogui.position()
        new_x = max(0, min(screen_width - 1, x + random.choice([-1, 1]) * pixel_distance))
        new_y = max(0, min(screen_height - 1, y + random.choice([-1, 1]) * pixel_distance))
        pyautogui.moveTo(new_x, new_y, duration=0.5)

        interval = fixed_interval if fixed_interval is not None else random.randint(0, 10)
        print(f"Mouse moved to ({new_x}, {new_y}), next move in {interval // 60} min {interval % 60} sec.")

        time.sleep(interval)


if __name__ == "__main__":
    # Example of fixed interval: 2 seconds, 50 pixels at a time
    #move_mouse(pixel_distance=50, fixed_interval=2)

    # Example of random interval: Random interval between 0 to 4 mins, 50 pixels at a time
     move_mouse(pixel_distance=50)
