import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
# from numpy import asarray
import time

def click(key):
    pyautogui.keyDown(key)
    return

def isCollision(data):
# Check colison for birds
    for i in range(520,550):
        for j in range(300, 390):
            if data[i, j] < 100:
                click("down")
                return
 # Check colison for cactus
    for i in range(520, 550):
        for j in range(400, 490):
            if data[i, j] < 100:
                click("up")
                return
    return

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(3)
    click('up') 
    
    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isCollision(data)
        
        # # Draw the rectangle for cactus
        # for i in range(520, 550):
        #     for j in range(400, 490):
        #          data[i, j] = 0
        
        # # Draw the rectangle for birds
        # for i in range(520, 550):
        #     for j in range(300, 390):
        #         data[i, j] = 171

        # image.show()
        # break