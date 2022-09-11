# Ejercicio de juego : Piedra, papel y tijera
import random
print("----------------------------------")
print("-------PIEDRA-PAPEL-TIJERA--------")
print("----------------------------------")

print("+________________________________+")
print("|       Bienvenido jugador       |")
print("|                                |")
print("|   Vas a luchar contra windows  |")
print("|     _______________________    |")
print("|     |     _          _     |   |")
print("|     |     O          O     |   |")
print("|     |           V          |   |")
print("|     |         /////        |   |")
print("|     |______________________|   |")
print("+________________________________+")

# intput

print("\n¡Elija una opcion para atacar!\n")
#se despliega el menu para seleccionar la opcion : 
print("1. Piedra")
print("2. Papel")
print("3. tijera")


usuario = int(input("\nAtaque: "))

win = random.randint(1,3)

#procesing
if(usuario == win ):
    print("-----------------------")
    print("--------EMPATE---------")
    print("-----------------------")

elif (usuario ==1 and win == 2):

   
    r = print("Elegistes piedra y Windows papel")
    r = print("--------PERDISTE---------")
   

elif (usuario ==1 and win == 3):
    r = print("Elegistes piedra y Windows tijeras")
    r = print("--------VICTORIA---------")

elif (usuario ==2 and win == 3):
    r = print("Elegistes papel y Windows tijeras")
    r = print("--------PERDISTE---------")

elif (usuario ==2 and win == 1):
    r = print("Elegistes papel y Windows piedra")
    r = print("--------VICTORIA---------")

elif (usuario ==3 and win == 1):
    r = print("Elegistes tijeras y Windows piedra")
    r = print("--------PERDISTE---------")

elif (usuario ==3 and win == 2):
    r = print("Elegistes tijeras y Windows papel")
    r = print("--------VICTORIA---------")

    
    #print("         ___             ")
    #print("_________|  |__________")
    #print("             __________|")
    #print("             __________|")
    #print("          _____________|")
    #print("___________________|")

   
    
    




    

    