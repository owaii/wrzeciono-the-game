from random import randint
import time
import sys
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

#-----------Zadymiarze------------

#---------------------------------
def zadyma(hpk,mk,hp):
    zadymiarz = 3
    if zadymiarz == (1):
        print('zadymiarz grzesio | hp = 5/5 | moc = 2')
        
    elif zadymiarz == (2):
        
        print('zadymiarz najlepszy | hp = 7/7 | moc = 5')
        
    elif zadymiarz == (4):
        
        print('zadymiarz kaśka | hp = 1/1 | moc = 1')
        print('                               _.._')
        print('                             .'    '.')
        print('                            (____/`\ |')
        print('                           (  |' ' )  )')
        print('                           )  _\= _/  (')
        print('                 __..---.(`_.  ` \    )')
        print('                `;-""-._(_( .      `; (')
        print('                /       `-```--     ;  )')
        print('               /    /  .    ( .  ,| |(')
        print('_.-` ---...__,     /-,..___.- -- _| |_)')
        print(' - `` -.._       ,   |   / ......... ')
        print('          ``;--"`;   |   `-`')
        print('             ``..__.`')
        
    elif zadymiarz == (3):
       
        print('zadymiarz kacper | hp = 3/3 | moc = 2')
        
        while hpk > 0: 
            
#------------------------------

#----------Walka i napisy------

#------------------------------

            print('a) biję')
            print('b) uciekam')
            walkarespond = input('')
            if walkarespond == ('a'):
                hpk -= moc
                time.sleep(1)
                print("zadajesz " ,moc, " damage i zostaje mu ", hpk, " hp")
                if hpk <=0 :
                    time.sleep(0.5)
                    print('                                                 ')
                    print(' _ _ _  __ __  _____  _____  _____  _____  _____ ')
                    print('| | | ||  |  ||   __|| __  ||  _  ||   | ||  _  |')
                    print('| | | ||_   _||  |  ||    -||     || | | ||     |')
                    print('|_____|  |_|  |_____||__|__||__|__||_|___||__|__|')
                    print('                                                 ')

                
                else: 
                    hp -= mk
                    time.sleep(2)
                    print("dostajesz ",mk, " damage i zostaje ci ", hp, " hp")
                    time.sleep(1)
                    print('                                          ')
                    print('                        //                ')
                    print(' _____  _____  _   _  _____ ______  ______')
                    print('|_   _|/  __ \| | | ||  _  || ___ \|___  /')
                    print('  | |  | /  \/| |_| || | | || |_/ /   / / ')
                    print('  | |  | |    |  _  || | | ||    /   / /  ')
                    print('  | |  | \__/\| | | |\ \_/ /| |\ \ ./ /___')
                    print('  \_/   \____/\_| |_/ \___/ \_| \_|\_____/')
                    print('                                          ')
                
#---------------------------------

#----------Lokalizacja1-----------

#---------------------------------

def lok1():
    print("-------OKRĄGLAK-------")
    print('a) szukam zadymy')
    print('b) idę do żabki')  #-----żabka=śmierć----
    print('c) spierdalam')      #-----tchórz=śmierć-----
    respond = input('')
    if respond == "a":
        zadyma(hpk,mk,hp)

    
    elif respond == "b":
        print('Wybierz produkt')
        print('a) Baton mocy')
        print('b) Kustosz mocne')
        print('c) Woda')
        respond = input('')
        if respond == "b":
            print('Chlejesz Kustosza i zdychasz, bo w twoim organizmie jest 6 promili piwa')
            time.sleep(4)
            sys.exit("GAME OVER")
        
        elif respond == "c":
            print("Na Wrzecionie nie pije się wody ty śmieciu")
            time.sleep(2)
            sys.exit("GAME OVER")
            
        elif respond == "a":
            print('Mmmm smaczne...')
            time.sleep(2)
            print("O kurde ja..ja..EUHGHGHGHG")
            time.sleep(2)
            print("Sprzedawca: O sory niechcący dałem ci Jad kiełbasiany. Zdychaj LOL")
            time.sleep(4)
            sys.exit("GAME OVER")
    
    
    elif respond == "c"
        print('                                          ')
        print('                        //                ')
        print(' _____  _____  _   _  _____ ______  ______')
        print('|_   _|/  __ \| | | ||  _  || ___ \|___  /')
        print('  | |  | /  \/| |_| || | | || |_/ /   / / ')
        print('  | |  | |    |  _  || | | ||    /   / /  ')
        print('  | |  | \__/\| | | |\ \_/ /| |\ \ ./ /___')
        print('  \_/   \____/\_| |_/ \___/ \_| \_|\_____/')
        print('                                          ') 
        time.sleep(4)
        sys.exit("GAME OVER")
        
#---------------------------------

#----------Lokalizacja2-----------

#---------------------------------

def lok2():
    print("-------METRO MŁOCINY-------")
            
   
#-----------------------------------

#-----------Mapa-------------------

#-----------------------------------
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

#---------------------Poruszanie się-------------------------------------------

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
#--------------------------------------------------------------

#----------------------Napis ( Logo )-------------------------

#--------------------------------------------------------------
print(' /$$      /$$ /$$$$$$$  /$$$$$$$$ /$$$$$$$$  /$$$$$$  /$$$$$$  /$$$$$$  /$$   /$$  /$$$$$$ ')
print('| $$  /$ | $$| $$__  $$|_____ $$ | $$_____/ /$$__  $$|_  $$_/ /$$__  $$| $$$ | $$ /$$__  $$')
print('| $$ /$$$| $$| $$  \ $$     /$$/ | $$      | $$  \__/  | $$  | $$  \ $$| $$$$| $$| $$  \ $$')
print('| $$/$$ $$ $$| $$$$$$$/    /$$/  | $$$$$   | $$        | $$  | $$  | $$| $$ $$ $$| $$  | $$')
print('| $$$$_  $$$$| $$__  $$   /$$/   | $$__/   | $$        | $$  | $$  | $$| $$  $$$$| $$  | $$')
print('| $$$/ \  $$$| $$  \ $$  /$$/    | $$      | $$    $$  | $$  | $$  | $$| $$\  $$$| $$  | $$')
print('| $$/   \  $$| $$  | $$ /$$$$$$$$| $$$$$$$$|  $$$$$$/ /$$$$$$|  $$$$$$/| $$ \  $$|  $$$$$$/')    
print('|__/     \__/|__/  |__/|________/|________/ \______/ |______/ \______/ |__/  \__/ \______/ ')              
print('                           /$$$$$$$$ /$$   /$$ /$$$$$$$$')              
print('                          |__  $$__/| $$  | $$| $$_____/')
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
