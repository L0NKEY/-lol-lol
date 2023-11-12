import os
import pynput
import time
from pynput.keyboard import Key, Controller
poop = input('what do you want to send: ')
meme = int(input('How many times: '))
i = int(0)
os.system('open -a Messages')
time.sleep(3)
lol = True
while i <= meme:

    keyboard = Controller()
    keyboard.type(poop)  
    keyboard.press(Key.enter)
    time.sleep(0.5)
    i += 1
  


