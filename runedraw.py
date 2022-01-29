import random

# program to perform random rune draws

aett_1 = ['Fehu','Uruz','Thurisaz','Ansuz','Raido','Kenaz','Gebo','Wunjo']
aett_2 = ['Hagalaz','Nauthiz','Isa','Jera','Eiwaz','Perthro','Elhaz','Sowilo']
aett_3 = ['Tiwaz','Berkana','Ehwaz','Mannaz','Laguz','Ingwaz','Othala', 'Dagaz']

def runedraw():
    print("\nThis program is an electronic rune Oracle.\n")
    print("\tThe first rune is for the events of the past.")
    print("\tThe second rune is for the events of the present.")
    print("\tThe third rune is for the events that are Becoming.\n")

# FIRST DRAW
    draw_1 = random.choice(aett_1 + aett_2 + aett_3)
    print(f"\n\tRESULT FOR FIRST DRAW:\t\t\t{draw_1}")
    
# SECOND DRAW      
    draw_2 = random.choice(aett_1 + aett_2 + aett_3) 
    if draw_1 == draw_2:
        draw_2 = random.choice(aett_1 + aett_2 + aett_3)
        print(f"\n\tRESULT FOR SECOND DRAW:\t\t\t{draw_2}")  
    else:
        print(f"\n\tRESULT FOR SECOND DRAW:\t\t\t{draw_2}")  
        
# THIRD DRAW 
    draw_3 = random.choice(aett_1 + aett_2 + aett_3)     
    if draw_3 == draw_2 or draw_3 == draw_1:
        draw_3 = random.choice(aett_1 + aett_2 + aett_3)
        print(f"\n\tRESULT FOR THIRD DRAW:\t\t\t{draw_3}")   
    else:
        print(f"\n\tRESULT FOR THIRD DRAW:\t\t\t{draw_3}")  

    print("\n\nThis concludes the Rune Oracle.\n")  
         
runedraw()
print("\nRUNE MEANINGS:\n")   
print("\nThe following meanings of the Elder Futhark Runes will help your interpretation.\n")        
print("\nFehu = 'mobile wealth'")  
print("Uruz = 'charging bull, territory'")  
print("Thurisaz = 'giant, opposer'")  
print("Ansuz = 'divine force', 'Asgard'")  
print("Raido = 'movement'")  
print("Kenaz = 'torch'")  
print("Gebo = 'gift'")  
print("Wunjo = 'joy'")  
print("Hagalaz = 'hailstorm'")  
print("Nauthiz = 'needfire'")  
print("Isa = 'ice'")  
print("Jera = 'season, cycle'")  
print("Eiwaz = 'yew-tree'")  
print("Perthro = 'well, fate'")  
print("Elhaz = warning")  
print("Sowilo = 'sunlight'")  
print("Tiwaz = 'spear, court'")  
print("Berkana = 'Birch tree', 'growth'")  
print("Ehwaz = 'horse'")  
print("Mannaz = 'mind, memory'")  
print("Laguz = lake, depths")  
print("Ingwaz = 'growth, expansion'")  
print("Othala = 'inheritance'")  
print("Dagaz = 'day'\n")  




            

