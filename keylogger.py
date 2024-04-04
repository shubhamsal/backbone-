import pynput.keyboard as keyboard

def press(key):
    print("this is the game")
    print(f"special key {key}")

def release(key):
    print(f"key {key} released")
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=press, on_release=release) as listener:
    listener.join()
