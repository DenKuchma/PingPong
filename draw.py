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

while True:
    os.system('cls')
    draw()
    time.sleep(0.1/2)