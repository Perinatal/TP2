#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Question 1 en simple programme
            
print("les nombres divisibles par 7 mais non multiples de 5, entre 2000 et 3200 (les deux inclus)")
print("\n")
liste1 = []
for i in range(2000, 3200):
    if ((i%7==0)&(i%5!=0)):
        liste1.append(i)
print(liste1)
print("\n")

                # Question 1 en fonction
def div7():
    print("les nombres divisibles par 7 mais non multiples de 5, entre 2000 et 3200 (les deux inclus)")
    print("\n")
    liste =  []
    for i in range(2000, 3200):
        if ((i % 7 == 0) & (i % 5 != 0)):
            liste.append(i)
    return liste
print(div7())
print("\n")

              # Question 2 en simple programme
              # La factorielle d'un nombre donné
a=5
x=1
while a>0:
    x = a*x
    a -= 1
print(x)

def factorielle(a, x=1):
    while a>0:
        x = a*x
        a -= 1
    return x
print(factorielle(7))

              # Question 3 en simple programme
              # Dictionnaire contenant des clés entier et valeurs carés de l'entier comprise entre un et N
n=8
dico = {}
for i in range(1, n+1):
    dico[i]=i*i    
print(dico)
              
def mondico(n):
    dico={}
    for i in range(1, n+1):
        dico[i]=i*i
    return dico
print(mondico(8))
              
              # Question 4 en simple programme
              # Dictionnaire contenant des clés entier et valeurs carés de l'entier comprise entre un et N
ch = input("donner une chaine : ")
x=len(ch)
mess="Donner un chiffre compris entre {} et {} ".format(0, x-1)
n=int(input(mess))
chaine = list(ch)
print("Voici votre chaine initiale:\n \n",chaine) 
chaine.pop(n)
print("\n Aprés suppression du caractére à la ", n, "éme place, voici la nouvelle chaine:\n \n", chaine)

              # Question 5 en simple programme
              # Dictionnaire contenant des clés entier et valeurs carés de l'entier comprise entre un et N
import numpy as np

tab = np.array([[1,2,3], [4,5,6], [7, 8, 9]])
print(tab)
liste2 = tab.tolist()
print(liste2)

               # Question 6 en simple programme
               # La matrice de covariance de deux tableaux 
matri1 = np.array([0, 1, 2])
matri2 = np.array([2, 1, 0])
print(matri1)
print(matri2)
matri_conv = np.cov(matri1, matri2)
print(matri_conv)

               # Question 7 en simple programme
               # Q = Racine carrée de [(2 * C * D)/H] 
D=[]
l=[]
C=50
H=30
nombre = int ( input("Donner un premier nombre compris entre 100 et 180: ") )
while (nombre < 100 or 180 < nombre) :
    nombre = int ( input("Ce nombre doit être compris entre 100 et 180: ") )
D.append(nombre)
nombre = int ( input("Donner un deuxiéme nombre compris entre 100 et 180: ") )
while (nombre < 100 or 180 < nombre) :
    nombre = int ( input("Ce nombre doit être compris entre 100 et 180: ") )
D.append(nombre)
nombre = int ( input("Donner un troisiéme nombre compris entre 100 et 180: ") )
while (nombre < 100 or 180 < nombre) :
    nombre = int ( input("Ce nombre doit être compris entre 100 et 180: ") )
D.append(nombre)
print("Tu as donné des nombres suivant :", D)
print("\n")
print('Si nous appliquons la formule Q=√((2*50*D)/30) avec D qui represente les valeurS que tu viens de donner et √ = racine carré')
print("\n")
z=0
while z<=2:
    x1 = ((2 * C * int(D[z]))/H)
    z+=1
    l.append(int(np.sqrt(x1)))
print("Nous aurons les resultats suivants:\t", l)


# In[ ]:




