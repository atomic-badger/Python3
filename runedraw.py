import random
#by dwayne brock 1.29.2022

# program to perform random rune draws

aett_1 = ['Fehu','Uruz','Thurisaz','Ansuz','Raido','Kenaz','Gebo','Wunjo']
aett_2 = ['Hagalaz','Nauthiz','Isa','Jera','Eiwaz','Perthro','Algiz','Sowilo']
aett_3 = ['Tiwaz','Berkana','Ehwaz','Mannaz','Laguz','Ingwaz','Othala', 'Dagaz']

def runedraw():
    print("\nThis program is an electronic rune Oracle.\n")
    print("\tThe first rune is for the events of the past.")
    print("\tThe second rune is for the events of the present.")
    print("\tThe third rune is for the events that are Becoming.\n")

# FIRST DRAW
    draw_1 = random.choice(aett_1 + aett_2 + aett_3)
    print(f"RESULT FOR FIRST DRAW:\t\t\t{draw_1}")
    
# SECOND DRAW      
    draw_2 = random.choice(aett_1 + aett_2 + aett_3) 
    if draw_1 == draw_2:
        draw_2 = random.choice(aett_1 + aett_2 + aett_3)
        print(f"RESULT FOR SECOND DRAW:\t\t\t{draw_2}")  
    else:
        print(f"RESULT FOR SECOND DRAW:\t\t\t{draw_2}")  
        
# THIRD DRAW 
    draw_3 = random.choice(aett_1 + aett_2 + aett_3)     
    if draw_3 == draw_2 or draw_3 == draw_1:
        draw_3 = random.choice(aett_1 + aett_2 + aett_3)
        print(f"RESULT FOR THIRD DRAW:\t\t\t{draw_3}")   
    else:
        print(f"RESULT FOR THIRD DRAW:\t\t\t{draw_3}")  

    print("\nThis concludes the Rune Oracle.\n")  
         
runedraw()
            

