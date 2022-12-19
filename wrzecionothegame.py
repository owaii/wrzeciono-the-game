from random import randint
import time
#---------------------------------
x = 0
z = 0
hajs = 0
hp = 5
maxhp = randint(5,10)
moc = randint(2,5)
#---
hpg = 5
mg = 2
#---
hpm = 7
mm = 5
#---
hpk = 3
mk = 2

#---------------------------------
#---------------------------------
def zadyma(hpk,mk,hp):
    zadymiarz = 3
    if zadymiarz == (1):
        print('zadymiarz grzesio | hp = 5/5 | moc = 2')
        
    elif zadymiarz == (2):
        
        print('zadymiarz najlepszy | hp = 7/7 | moc = 5')
        
    elif zadymiarz == (3):
       
        print('zadymiarz kacper | hp = 3/3 | moc = 2')
        
        while hpk > 0: 
            
            print('a) biję')
            print('b) uciekam')
            walkarespond = input('')
            if walkarespond == ('a'):
                hpk -= moc
                time.sleep(1)
                print("zadajesz " ,moc, " damage i zostaje mu ", hpk, " hp")
                if hpk <=0 :
                    time.sleep(0.5)
                    print('wygrywasz')
                
                else: 
                    hp -= mk
                    time.sleep(2)
                    print("dostajesz ",mk, " damage i zostaje ci ", hp, " hp")
                
#---------------------------------
def lok1():
    print("-------OKRĄGLAK-------")
    print('a) szukam zadymy')
    print('b) idę do żabki')
    print('c) spierdalam')
    respond = input('')
    if respond == "a":
        zadyma(hpk,mk,hp)
#---------------------------------
def mapa():
    print("------------------------")
    print('okrąglak x = 50 z = 10')
    print('metro młociny x = -80 z = 20')
    print('las bielański x = 20 z = -40')
    print('szpital bielański x = -30 z = -10')
    print('Kościół Niepokalanego Poczęcia Najświętszej Maryi Panny x = 70 z = 10')
    print("------------------------")

    time.sleep(12)
    move(x,z)
#------------------------------------------------------------------------------
def move(x,z):
    while True:
        if (x==50) and (z == 10):
            lok1()
        print('----------------------------------------------------------------------------------')
        print(heros,"  KOORDYNATY: ", 'x=', x, "z=", z , "|| hajs: ", hajs, "zł || hp: ", hp,"/",maxhp, "|| moc: ", moc)
        print('----------------------------------------------------------------------------------')
        
        print("a) Północ")
        print("b) Południe")
        print("c) Zachód")
        print("d) Wschód")
        print("e) Mapa")
        respond = input('')
        if respond == "a":
            x += 10
        elif respond == "b":
            x -= 10
        elif respond == "c":
            z -= 10
        elif respond == "d":
            z += 10
        elif respond == "e":
            mapa()
#---------------------------------
print(' /$$      /$$ /$$$$$$$  /$$$$$$$$ /$$$$$$$$  /$$$$$$  /$$$$$$  /$$$$$$  /$$   /$$  /$$$$$$ ')
print('| $$  /$ | $$| $$__  $$|_____ $$ | $$_____/ /$$__  $$|_  $$_/ /$$__  $$| $$$ | $$ /$$__  $$')
print('| $$ /$$$| $$| $$  \ $$     /$$/ | $$      | $$  \__/  | $$  | $$  \ $$| $$$$| $$| $$  \ $$')
print('| $$/$$ $$ $$| $$$$$$$/    /$$/  | $$$$$   | $$        | $$  | $$  | $$| $$ $$ $$| $$  | $$')
print('| $$$$_  $$$$| $$__  $$   /$$/   | $$__/   | $$        | $$  | $$  | $$| $$  $$$$| $$  | $$')
print('| $$$/ \  $$$| $$  \ $$  /$$/    | $$      | $$    $$  | $$  | $$  | $$| $$\  $$$| $$  | $$')
print('| $$/   \  $$| $$  | $$ /$$$$$$$$| $$$$$$$$|  $$$$$$/ /$$$$$$|  $$$$$$/| $$ \  $$|  $$$$$$/')    
print('|__/     \__/|__/  |__/|________/|________/ \______/ |______/ \______/ |__/  \__/ \______/ ')              
print('                             /$$$$$$$$ /$$   /$$ /$$$$$$$$')              
print('                             |__  $$__/| $$  | $$| $$_____/')
print('                             | $$   | $$  | $$| $$      ')
print('                             | $$   | $$$$$$$$| $$$$$   ')
print('                             | $$   | $$__  $$| $$__/   ')
print('                             | $$   | $$  | $$| $$      ')
print('                             | $$   | $$  | $$| $$$$$$$$')
print('                             |__/   |__/  |__/|________/')
print('                      /$$$$$$   /$$$$$$  /$$      /$$ /$$$$$$$$')
print('                      /$$__  $$ /$$__  $$| $$$    /$$$| $$_____/')
print('                     | $$  \__/| $$  \ $$| $$$$  /$$$$| $$      ')
print('                     | $$ /$$$$| $$$$$$$$| $$ $$/$$ $$| $$$$$   ')
print('                     | $$|_  $$| $$__  $$| $$  $$$| $$| $$__/   ')
print('                     | $$  \ $$| $$  | $$| $$\  $ | $$| $$      ')
print('                     |  $$$$$$/| $$  | $$| $$ \/  | $$| $$$$$$$$')
print('                      \______/ |__/  |__/|__/     |__/|________/')
print('------------------------------------------------------------------------------------------')



         
time.sleep(2)
print('jak nazywa się twój menel: ')
heros = input('')
move(x,z)
