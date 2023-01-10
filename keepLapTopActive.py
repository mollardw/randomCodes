import time
import random
import pyautogui

#this will run for about an hour
num=0
while(num != 515):
    num1=random.randint(100,500)
    num2=random.randint(100,500)
    print(num1)
    print(num2)
    pyautogui.moveTo(num1,num2)
    time.sleep(7)
    num+1
