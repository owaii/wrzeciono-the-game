from random import randint
import time
#---------------------------------
x = 0
z = 0
#---------------------------------
def move(x,z):
    while True:
        print("KOORDYNATY: ", 'x=', x, "z=", z)
        print("a) Północ")
        print("b) Południe")
        print("c) Zachód")
        print("d) Wschód")
        respond = input('')
        if respond == "a":
            x += 10
        elif respond == "b":
            x -= 10
        elif respond == "c":
            z -= 10
        elif respond == "d":
            z += 10
#---------------------------------
print("WRZECIONO THE GAME")
time.sleep(2)
move(x,z)
