from random import randint
import time

print("wylosuj 6 aby zacząć gre")
time.sleep(2)
x = randint(1,100)
print(x)
if x != 6:
    print("dupa się zesrała")
else:
    print("WRZECIONO THE GAME")

