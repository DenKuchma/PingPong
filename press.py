
import time
import os
import pynput

WIDTH = 30
HEIGHT = 10
ballX = 5
ballY = 1
rocket1 = 0
rocket2 = 6
rocketLength = 2
dirX = 1
dirY = 1

def on_press(key):
    global rocket2, rocket1
    if key == pynput.keyboard.Key.up and rocket2 > 0 and rocket2 <= 8:
        rocket2 -= 1
    if key == pynput.keyboard.Key.down and rocket2 >= 0 and rocket2 < 8:
        rocket2 += 1
    if key == pynput.keyboard.KeyCode.from_char('w') and rocket1 > 0 and rocket1 <= 8:
        rocket1 -= 1
    if key == pynput.keyboard.KeyCode.from_char('s') and rocket1 >= 0 and rocket1 < 8:
        rocket1 += 1
    
def on_release(key):
    pass
    
pynput.keyboard.Listener(
    on_press = on_press,
    on_release = on_release
).start()

while True:
    os.system('cls')
    time.sleep(0.1/2)