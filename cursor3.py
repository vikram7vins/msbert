import ctypes, random, time

# Constants for screen width and height
user32 = ctypes.windll.user32
screen_width, screen_height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

def smooth_move_mouse(start_x, start_y, end_x, end_y, duration):
    """
    Smoothly moves the mouse from the current position to the new (end_x, end_y) over a fixed duration.

    Parameters:
    start_x (int): Starting X position of the mouse.
    start_y (int): Starting Y position of the mouse.
    end_x (int): Target X position of the mouse.
    end_y (int): Target Y position of the mouse.
    duration (float): Total duration for the movement (in seconds).
    """
    steps = 100  # Number of steps to move smoothly
    step_delay = duration / steps
    x_step = (end_x - start_x) / steps
    y_step = (end_y - start_y) / steps

    for i in range(steps):
        new_x = int(start_x + x_step * i)
        new_y = int(start_y + y_step * i)
        ctypes.windll.user32.SetCursorPos(new_x, new_y)
        time.sleep(step_delay)  # Small delay to make movement smoother

def move_mouse(pixel_distance, fixed_interval=None):
    """
    Moves the mouse at either fixed or random intervals with smooth movement.

    Parameters:
    pixel_distance (int): Number of pixels to move.
    fixed_interval (float or None): Time interval between movements (fixed or None for random between 0 to 4 mins).
    """
    while True:
        # Get current mouse position
        current_x, current_y = ctypes.c_long(), ctypes.c_long()
        ctypes.windll.user32.GetCursorPos(ctypes.byref(current_x), ctypes.byref(current_y))

        # Calculate new position with boundaries
        new_x = max(0, min(screen_width - 1, current_x.value + random.choice([-1, 1]) * pixel_distance))
        new_y = max(0, min(screen_height - 1, current_y.value + random.choice([-1, 1]) * pixel_distance))

        # Smoothly move the mouse to the new position
        duration = 0.5  # Time in seconds for smooth movement (can be adjusted)
        smooth_move_mouse(current_x.value, current_y.value, new_x, new_y, duration)

        # Determine the time interval (fixed or random)
        interval = fixed_interval if fixed_interval is not None else random.randint(0, 10)
        print(f"Mouse moved to ({new_x}, {new_y}), next move in {interval//60} min {interval%60} sec.")

        # Sleep for the determined interval
        time.sleep(interval)

if __name__ == "__main__":
    # Example of fixed interval: Move mouse every 2 seconds, 50 pixels at a time
    #move_mouse(pixel_distance=50, fixed_interval=5)

    # Example of random interval: Move mouse by 50 pixels at random intervals between 0 to 4 minutes
    move_mouse(pixel_distance=150)
