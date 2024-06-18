from pynput import keyboard

def on_press(key):
    try:
        #print('alphanumeric key {0} pressed'.format(key.char))
        pass
    except AttributeError:
        print('special key {0} pressed'.format(key))

def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

print ("\n Pess 1 or 2 or 3 to execute\n\n 1 - USB_allow_read_write_execute\n 2 - USB_deny_read_write_execute\n Esc - exit")

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
