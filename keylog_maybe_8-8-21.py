import keyboard 
import time
import random
import string

#function to disable loop on certain key press
def onkeypress(event):
    global stop
    if event.name == 'p':
        stop = True


string.ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890[]{}-_=+/?.><,\|!`¬'
i = 0
time.sleep(0.1)
stop = False

keyboard.on_press(onkeypress)

#begin loop
while True:

    #changes rep and random letter every loop
    i = i+1
    r = random.choice(string.ascii_letters)

    #selects a random letter and presses enter
    keyboard.write(str(i)+' - '+str(r))
    keyboard.press_and_release('enter')

    #prints to show "Number of reps - random gen"
    print(str(i)+' - '+r)
    if stop:
          print('Stopped')
          break


