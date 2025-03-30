import time
#How to see how many days, hours, minutes and seconds we have.(Digital Clock)

my_time = int(input("Enter time in seconds:"))
for x in range(my_time, 0, -1):    # Counting down per second
    seconds = x %60
    min = int(x/60) %60
    hrs = int(x/3600) %24
    days = int(x/86400)
    print(f"{days:02}:{hrs:02}:{min:02}:{seconds:02}")
    time.sleep(1)  

print("Time's Up!")


