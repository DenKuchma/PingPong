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

def moveBall():
    global ballX, ballY, dirX, dirY
    if ballY > HEIGHT - 2 or ballY < 1:
        dirY *= -1 
    if ballX > WIDTH - 3\
            and ballY >= rocket2 \
            and ballY < rocket2 + rocketLength:
        dirX *= -1 
    elif ballX == WIDTH - 1:
        exit("Player 1 win")
    if ballX < 2 \
            and ballY >= rocket1 \
            and ballY < rocket1 + rocketLength:
        dirX *= -1
    if ballX < 0:
        dirX *= -1
    elif ballX == 0:
        exit("Player 2 win")
    
    ballX += dirX
    ballY += dirY

def draw():
    y = 0
    while y < HEIGHT:
        x = 0
        result = ''
        while x < WIDTH:
            if x == ballX and y == ballY:
                result += 'o'
            elif x == 0 \
                    and y >= rocket1 \
                    and y < rocket1 + rocketLength:
                result += '|'
            elif x == WIDTH - 1 \
                    and y >= rocket2 \
                    and y < rocket2 + rocketLength:
                result += '|'
            else:
                result += '-'
            x += 1
        print(result)
        y += 1

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
    draw()
    moveBall()
    time.sleep(0.1/2)