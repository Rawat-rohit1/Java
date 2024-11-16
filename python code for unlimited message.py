import pyautogui
import time
count=0
p=input("enter the sentence you want to send to your friend : ")
t=int(input("enter how many times you want to send the message:"))
time.sleep(3)
while(count<=t):
    pyautogui.typewrite(p)
    pyautogui.press("enter")
    count=count+1