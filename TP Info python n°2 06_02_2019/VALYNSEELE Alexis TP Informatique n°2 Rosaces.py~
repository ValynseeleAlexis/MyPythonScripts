# Auteur : Valynseele Alexis
# Titre  : Rosaces - TP 2 

                                                                        #DEBUT DU TP#

#entête

from numpy import zeros, array
import matplotlib.pyplot as plt
from typing import Iterable

#definition des types :
class Personne:
    x=0
    y=0
    flash = None
    couleur = (0,0,0)
TabPersonnes = Iterable[Personne]
Couleur = (float, float, float)

#Fonction cree_personne : crée une "Personne" et lui affecte ses coordonnées et la retourne
def creer_personne(x:float, y:float)->Personne:
 
  p:Personne = Personne()
  p.x = x
  p.y = y
  return p
 
#Exercice 1

#Fonction ajouter_personne : crée une personne de coordonnées (x,y) et la stocke a la position n d'un tableau de personnes puis retourne n+1
def ajouter_personne(x:float, y:float, tab:TabPersonnes, n:int)->int:
 
 tab[int(n)] = creer_personne(x,y)
 return (n+1)
 
#Exercice 2

#Procedure flasher_personnes : procedure permettant a chaque personne d'un tableau de n personnes de "flasher" la personne suivante dans le tableau.
def flasher_personnes(tab:TabPersonnes, n:int) :
 
 for i in range (0,int(n-1)) :
     tab[i].flash = tab[(i+1)]
 tab[n-1].flash = tab[0]
 
#Exercice 3
 
#Procedure dessiner_regars : procedure qui trace une ligne entre une personne et son flash et ce pour chaque personne du tableau tab contenant n personnes

def dessiner_regards(tab:TabPersonnes, n:int):
 
 for i in range (0,int(n)) :
    plt.plot([tab[i].x,tab[i].flash.x],[tab[i].y,tab[i].flash.y])
 
#Exercice 4 / Methodes de test

def test_algos():
    
#creation d'un tableau pour 10 personnes  
 tab:TabPersonnes = zeros(10,Personne)
#ajout de 4 personnes
 n=0
 n = ajouter_personne(0,0,tab,n)
 n = ajouter_personne(10,0,tab,n)
 n = ajouter_personne(10,10,tab,n)
 n = ajouter_personne(0,10,tab,n)
#mise en relation des personnes
 flasher_personnes(tab,n)
#test du dessin
 dessiner_regards(tab, n)
#lancer l'affichage du graphique
 plt.show()
 
#Exercice 5
 
#Procedure avancer_personne : procedure qui fait avancer chaque personne du tableau tab de 5% vers les coordonnees de leur "flash" respectif.
def avancer_personne(tab:TabPersonnes, n:int):
 
 for i in range (0,int(n)) :
  tab[i].x += (5/100)*((tab[i].flash.x) - (tab[i].x))
  tab[i].y += (5/100)*((tab[i].flash.y) - (tab[i].y))
  
#Exercice 6 

#Procedure rosace : procedure dessinant une rosace à l'aide des fonctions et procédure définies auparavant
def rosace() :
 
#creation d'un tableau pour 10 personnes  
 tab:TabPersonnes = zeros(10,Personne)
#ajout de 4 personnes
 n=0
 n = ajouter_personne(0,0,tab,n)
 n = ajouter_personne(10,0,tab,n)
 n = ajouter_personne(10,10,tab,n)
 n = ajouter_personne(0,10,tab,n)
#mise en relation des personnes
 flasher_personnes(tab,n)
#boucle du dessin
 for i in range (0,100) : 
  dessiner_regards(tab, n)
  avancer_personne(tab, n)
#lancer l'affichage du graphique
 plt.show()
 
 
#Exercice 7 

#fonction dessiner_regards_colores : fonction ayant le même objectif que dessiner_regards mais en assignant une couleur particulière aux lignes tracées

def dessiner_regards_colores(tab:TabPersonnes, n:int) : 

  for i in range (0,int(n)) :
    plt.plot([tab[i].x,tab[i].flash.x],[tab[i].y,tab[i].flash.y], color=tab[i].couleur , linewidth = 0.5 )


#Exercice 8
 
#procedure rosace_coloree() : procedure ayant le même objectif que rosace() mais se servant de dessiner_regards_colores afin d'avoir une rosace de couleur précise
 
def rosace_coloree() : 

#creation d'un tableau pour 10 personnes  
 tab:TabPersonnes = zeros(10,Personne)
#ajout de 8 personnes
 n=0
 n = ajouter_personne(0,0,tab,n)
 n = ajouter_personne(5,0,tab,n)
 n = ajouter_personne(10,0,tab,n)
 n = ajouter_personne(10,5,tab,n)
 n = ajouter_personne(10,10,tab,n)
 n = ajouter_personne(5,10,tab,n)
 n = ajouter_personne(0,10,tab,n)
 n = ajouter_personne(0,5,tab,n)
#gestion des couleurs des personnes
 c:Couleur = (0,0,1) 
 tab[0].couleur = c # 100 % bleu pour la personne n°1
 for i in range (1,8) :
  c:Couleur = (0,0,c[2]-0.125)   #degradé de bleu allant jusqu'au noir pour les 7 personnes suivantes
  tab[i].couleur = c
#mise en relation des personnes
 flasher_personnes(tab,n)
#boucle du dessin
 for i in range (0,500) : 
  dessiner_regards_colores(tab, n)
  avancer_personne(tab, n)
#lancer l'affichage du graphique
 plt.show()
 
                                                                          #FIN DU TP#
 
 
 

#main / test
 
rosace_coloree()

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
