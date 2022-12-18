from random import randint
import time
#---------------------------------
x = 0
z = 0
hajs = 0
hp = randint(1,10)
moc = randint(1,10)
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
        print('----------------------------------------------------------------------------------')
        print(heros,"  KOORDYNATY: ", 'x=', x, "z=", z , "|| hajs: ", hajs, "zł || hp: ", hp,"/",hp, "|| moc: ", moc)
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
print(' __          __ _____   ______ ______  _____  _____  ____   _   _   ____  ')
print(' \ \        / /|  __ \ |___  /|  ____|/ ____||_   _|/ __ \ | \ | | / __ \ ')
print('  \ \  /\  / / | |__) |   / / | |__  | |       | | | |  | ||  \| || |  | |')
print('   \ \/  \/ /  |  _  /   / /  |  __| | |       | | | |  | || . ` || |  | |')
print('    \  /\  /   | | \ \  / /__ | |____| |____  _| |_| |__| || |\  || |__| |')
print('  ___\/__\/_   |_| _\_\/_____||______|\_____||_____|\____/_|_| \_| \____/ ')
print(' |__   __|| |  | ||  ____|  / ____|    /\    |  \/  ||  ____|')             
print('    | |   | |__| || |__    | |  __    /  \   | \  / || |__  ')              
print('    | |   |  __  ||  __|   | | |_ |  / /\ \  | |\/| ||  __| ')              
print('    | |   | |  | || |____  | |__| | / ____ \ | |  | || |____ ')
print('    |_|   |_|  |_||______|  \_____|/_/    \_\|_|  |_||______|')
print('---------------------------------------------')


         
time.sleep(2)
print('jak nazywa się twój menel: ')
heros = input('')
move(x,z)
