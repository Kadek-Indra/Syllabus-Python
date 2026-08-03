# For and while loop
import time

second = int(input("Enter the time in seconds : "))

while second > 0:
    seconds = second % 60
    minutes = (second // 60) % 60
    hours = (second // 3600)
    print (f"{hours:02}:{minutes:02}:{seconds:02}")
    second -=1
    time.sleep(1)
    if second <= 10:
        break

for x in range(second, 0, -1):
    print(f"00:00:{x:02} seconds left!")
    time.sleep(1)

print ("Time's Up!")
