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

while True:
    os.system('cls')
    moveBall()
    time.sleep(0.1/2)