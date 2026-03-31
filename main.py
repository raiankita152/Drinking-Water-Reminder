import time
from turtle import title
from plyer import notification


while True:
    print("drink some water")
    notification.notify(title="Please Drink Water", message="You need to drink some water ")
    time.sleep(60*60)
