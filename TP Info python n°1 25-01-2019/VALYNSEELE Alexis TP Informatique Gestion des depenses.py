# Auteur : Valynseele Alexis
# Titre  : Gestion des depenses-TP1

                                                                   #DEBUT DU TP#

#Exercice 1 / entête

from numpy import zeros, array
from typing import Iterable, TypeVar


TabReels = TypeVar(Iterable[float])
MatReels = TypeVar(Iterable[TabReels])
MAXPRODUITS = 100


# Exercice 2

#saisir_produit : procedure permettant d'entrer le prix et la note d'un produit donné puis de stocker ces valeurs dans tabPrixNotes

def saisir_produit(no:int, tabPrixNotes:float) : 
 print("Quel est le prix du produit n° %s" % no)
 prix = input()
 tabPrixNotes [0][int(no)] = prix
 print("Quel est la note du produit n° %s" % no)
 note = input()
 tabPrixNotes [1][int(no)] = note
 
 
#Exercice 3

# saisir_produits : procedure permettant d'entrer le prix et la note d'un nombre "nb" de produits donnés puis de stocker ces valeurs dans tabPrixNotes

def saisir_produits(nb:int, tabPrixNotes:float) :
 i = 0
 for i in range (0,int(nb)) :
  saisir_produit(i,tabPrixNotes)
  

#Exercice 4

# afficher_detail_produit : procedure permettant d'afficher le numéro,le prix et la note d'un produit en particulier ayant ses informations stockés dans "tabPrixNotes"

def afficher_detail_produit(no:int, tabPrixNotes:float) :
  print("Concernant le produit n° %s : \n" % no)
  print("n°   : %s" % no)
  print("prix : %s euros" % tabPrixNotes[0][int(no)])
  print("note : %s\n" % tabPrixNotes[1][int(no)])
  
#Exercice 5
 
#afficher_produits : procedure permettant d'afficher le numéro,le prix et la note d'un nombre "nb" de produits ayant leurs informations stockés dans "tabPrixNotes"

def afficher_produits(nb:int, tabPrixNotes:float) :
 i = 0
 for i in range (0,int(nb)) :
  afficher_detail_produit(i,tabPrixNotes)


#Exercice 6 

#max_tab : fonction retournant la valeur maximun sur "nb" indices d'un tableau simple "tab" à une dimension 

def max_tab(nb:int, tab:float)->float:
 i = 0
 max = tab[0]
 for i in range (0,int(nb)) :
   if max < tab[int(i)]:
    max = tab[int(i)]
 return float(max)


#Exercice 7

#min_tab : fonction retournant la valeur min sur "nb" indices d'un tableau simple "tab" à une dimension 

def min_tab(nb:int, tab:float)->float:
 i = 0
 min = tab[0]
 for i in range (0,int(nb)) :
   if min > tab[int(i)]:
    min = tab[int(i)]
 return float(min)


#Exercice 8

#afficher_moins_chers : procedure qui parcourt nb produits stockés dans "tabPrixNotes" et affiche les détails (à l'aide de "afficher_detail_produit") des produits les moins chers

def afficher_moins_chers(nb:int, tabPrixNotes:float) : 
 minPrix = min_tab(nb, tabPrixNotes[0]) 
 i = 0
 print("Voici les informations concernant les produits les moins chers : \n")
 for i in range (0,int(nb)) :
  if minPrix == tabPrixNotes[0] [int(i)] : 
   afficher_detail_produit(i,tabPrixNotes)
 
 
#Exercice 9 
 
# afficher_mieux_notes : procedure qui parcourt nb produits stockés dans "tabPrixNotes" et affiche les détails (à l'aide de "afficher_detail_produit") des produits les mieux notés

def afficher_mieux_notes(nb:int, tabPrixNotes:float) : 
 maxNote = max_tab(nb, tabPrixNotes[1]) 
 i = 0
 print("Voici les informations concernant les produits les mieux notés : \n")
 for i in range (0,int(nb)) :
  if maxNote == tabPrixNotes[1] [int(i)] : 
   afficher_detail_produit(i,tabPrixNotes)
   
   
#Exercice 10

#remplir_tab_norme : procedure qui normalisent (ramènent tout les valeurs sur un interval [0,1] en divisant chaque valeur par la valeur max) les "nb" valeurs d'un tableau simple passé en entrée et place les valeurs normalisée dans un nouveau tableau simple recuperé en sortie

def remplir_tab_norme(nb:int, tab:float, tabNorm:float) :
 maxTab = max_tab(nb,tab)
 i = 0
 for i in range (0,int(nb)) :
  tabNorm[int(i)] = (tab[int(i)]/maxTab)


#Exercice 11
   
#trouver_compromis : procedure qui crée deux tableaux simple ‘tabNormPrix’ et ‘tabNormNotes’ à partir du tableau à 2 dimensions passé en entrée et de la procédure "remplir_tab_norme", ces deux tableaux contiennent respectivement les valeurs normalisées des prix et des notes des produits contenu dans "tabPrixNotes", puis la procédure crée un troisième tableau simple ‘tabMixe’ qui contient des valeurs mixant l'intérêt pour une note élevée et un prix bas, enfin elle affiche le ou les produits dont l'intérêt est le plus élevé à l'aide de "max_tab" et de "afficher_detail_produit"

def trouver_compromis(nb:int, tabPrixNotes:float):
 tabPrix = zeros(MAXPRODUITS, float) #VARIABLES
 tabNotes = zeros(MAXPRODUITS, float)
 tabNormPrix = zeros(MAXPRODUITS, float)
 tabNormNotes = zeros(MAXPRODUITS, float)
 tabMixe = zeros(MAXPRODUITS, float)
 i = 0
 
 for i in range (0,int(nb)) :
  tabPrix[int(i)] = tabPrixNotes [0] [int(i)]
  tabNotes[int(i)] = tabPrixNotes [1] [int(i)]
 remplir_tab_norme(nb,tabPrix,tabNormPrix)
 remplir_tab_norme(nb,tabNotes,tabNormNotes) #fin du 1)
 
 for i in range (0,int(nb)) :
  tabMixe[int(i)] = (tabNormNotes[int(i)]*(1-tabNormPrix[int(i)]*0.9)) #fin du 2)    
 maxCompromis = max_tab(nb,tabMixe) 
 
 print("Voici les informations concernant les produits avec le meilleur compromis : \n")
 for i in range (0,int(nb)) :
  if maxCompromis == tabMixe [int(i)] : 
   afficher_detail_produit(i,tabPrixNotes) #fin du 3)
 
   
#Exercice 12

#moyenne : fonction retournant la moyenne des valeurs contenu dans un tableau simple "tab" à une dimension sur "nb" indices

def moyenne(nb:int, tab:float)->float:
 i=0
 somme=0
 compteur=0
 for i in range (0,int(nb)) :
   somme = somme + tab[i]
   compteur = compteur + 1
   
 return (somme/compteur)

#Exercice 13

#test_TP1 : procedure testant les différentes procedures et fonctions codées auparavant avec diverses valeurs 

def test_TP1():
 prix:float = array([81,72,85,71,66,104,91,87])
 notes:float = array([2,4,5,3,2,0,2,5])
 prixNotes:float = array([prix, notes])
 nb:int = len(prix)
 afficher_moins_chers(nb, prixNotes)
 afficher_mieux_notes(nb, prixNotes)
 trouver_compromis(nb, prixNotes)
 print("Moyenne des prix : " + str(moyenne(nb, prix)))
 print("Moyenne des notes : " + str(moyenne(nb, notes)))

#Resultats : 

#Produit le moins cher : "produit n°4"
#Produits les mieux notés : "produit n°2" et "produit n°7"
#Produit avec le meilleur compromis : "produit n°1 "
#Moyenne des prix : 82.125 euros
#Moyenne des notes : 2.875 / 10

                                                                     #FIN DU TP#





#main / test

tabPrixNotes = zeros((2,MAXPRODUITS), float) #j'ai utilisé un type float car j'ai une erreur "data type not understood" avec TabReels
tab = zeros(MAXPRODUITS, float)
tabNorm = zeros(MAXPRODUITS, float) 

print("Combien de produits voulez entrer ? : ")
nb = input()
saisir_produits(nb, tabPrixNotes)
afficher_moins_chers(nb, tabPrixNotes)
afficher_mieux_notes(nb ,tabPrixNotes)
trouver_compromis(nb, tabPrixNotes)













































