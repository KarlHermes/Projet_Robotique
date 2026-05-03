import numpy as np 

# les variables :::::::::::::::::::::::::: 1
a = 1 # une variable de type entier 2
b = 2 # une duxieme variable de type entier 3
c = 3.2 # une variable de type reel ( float ) 4
text = " Chaine de caracteres " # une variable de type chaine de caracteres 5
bool_var1 = None # une variable booleenne 6
bool_var2 = True 
print ( " Variables : " ,a ,b ,c , text , "\n " )

# operateurs ::::::::::::::::::::::::::::::
addition = a + b
soustraction = b - a 
produit = a * b 
division = a / b 
division2 = a / c 
puissance = b ** b 

print ( "Operateurs :\n" ) 
print ( " Addition : " , addition , "\n" ) 
print ( " Soustraction : " , soustraction , "\n" ) 
print ( " Produit : " , produit , "\n" ) 
print ( " Division ( floor division ) : " , division , "\n" ) 
print ( " Division2 : " , division2 , "\n" ) 
print ( " puisssance X ^ Y : " , puissance , "\n" )

#Matrice
matrice_zeros = np . zeros ((3 ,4)) # matrice nulle 3 x4 5
matrice_ones = np . ones ((2 ,5)) # matrice unitaire 2 x5 6
identite = np . eye (3) # matrice identite
print (matrice_zeros,"\n" ) 
print (matrice_ones,"\n" ) 
print (identite,"\n" ) 

print(matrice_zeros.size,"\n")
print(matrice_zeros.shape,"\n")

# Structure de controle 
x = int(raw_input(" Please enter an integer : " )) 
if x < 0: 
    x = 0 
    print ("Negative to Zero") 
elif x == 0: 
    print ( "Zero") 
elif x == 1: 
    print ("single") 
else : 
    print ("More")


