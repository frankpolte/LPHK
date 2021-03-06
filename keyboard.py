from pynput.keyboard import Key, Controller, KeyCode

media_keys = {"vol_up" : 269025043, "vol_down" : 269025041, "mute" : 269025042, "play_pause" : 269025044, "prev_track" : 269025046, "next_track" : 269025047, "bright_down" : 269025027, "bright_up" : 269025026}

controller = Controller()

def sp(name):
    try:
        return getattr(Key, str(name))
    except:
        try:
            return KeyCode(media_keys[str(name)])
        except:
            return None

def press(key):
    controller.press(key)

def release(key):
    controller.release(key)

def tap(key):
    press(key)
    release(key)

