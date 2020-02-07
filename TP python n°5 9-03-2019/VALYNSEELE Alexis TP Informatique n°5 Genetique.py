###################################
# Auteur : Valynseele Alexis      #
# Titre  :  Génétique - TP 5      #
# L1 INFO S2 - ISTV               #
###################################
                                                                        #DEBUT DU TP#


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from numpy import  array,zeros
from typing import Iterable
from random import randint
from multiprocessing import Pool
from math import sqrt
#nb d'objets possibles
NBOBJETS = 8
#nb se sacs dans la population
NBSACS = 40
  
##Les Types et Constantes
Tabint = Iterable[int]
TabReels = Iterable[float]

#un sac contient un tableau d'entiers entre 0 et 1 indiquant la présence ou non d'un produit
 #et contient également un poids */
class Sac:
    genome:Tabint = None
    poids:float=0.0
    interet:float=0.0
    note:float = 0.0
  
#tableau de sacs
TabPopulation = Iterable[Sac]


#les poids des 8  différents produits
POIDS:TabReels = array([10.4, 1.4, 5.4, 8.4, 1.4, 6.8, 6.3, 1.1])
#les interets des 8  différents produits
INTERETS:TabReels = array([8,4,4,6,5,3,7, 2])

##Les fonctions

#crée le contenu d'un sac et permet de saisir les valeurs 
def creerSac(sac:Sac):
    sac.genome = zeros(NBOBJETS, int)
    for i in range(0,NBOBJETS):
        sac.genome[i] = randint(0,1)

#calcul le poids, l'interet et la note d'un sac
def calculProprietes(sac:Sac):
    sommePoids:float = 0.0
    sommeinteret:float = 0.0
    for i in range (0,NBOBJETS):
            if sac.genome[i] == 1 : 
                 sommePoids = sommePoids + POIDS[i]
                 sommeinteret = sommeinteret + INTERETS[i]   
    sac.poids = sommePoids
    sac.interet = sommeinteret
    sac.note = sommeinteret - sommePoids

#créer NBSACS sacs et les place dans le tableau population
def creerPopulation(population:TabPopulation):
    for i in range(0, NBSACS):
        s:Sac  = Sac()
        creerSac(s)
        calculProprietes(s)
        population[i] = s

#affiche les no des produits contenu dans un sac, ainsi que son poids, son interet et sa note*/
def afficheSac(sac:Sac):
    print("\n=========================================================================\n")
    print("Contenu du sac : ")
    for i in range(0, NBOBJETS):
        if(sac.genome[i]==1): print(i, end=", ")
    print("\n\npoids = ",float(sac.poids), ",     interet = " ,float(sac.interet), ",     note = " ,float(sac.note))
    print("\n=========================================================================\n")


#affiche tous les sacs du tableau population 
def affichePopulation(population:TabPopulation):
    for sac in population:
        afficheSac(sac)

        
#échange de poisitions les sacs situés aux positions i et j de tab
def permuter(tab: TabPopulation, i: int, j: int):
        temp = tab[i]
        tab[i] = tab[j]
        tab[j] = temp
 
#tri les sacs du tableau population, en utilisant le tri par insertion, et en triant les sacs par odre de note décroissante
def triPopulationInsertion(population:TabPopulation):
    n = len(population)
    for i in range (1, n):
            x = population[i].note
            j = i
            while j > 0 and population[j-1].note < x:
                    permuter(population,j,j-1)
                    j = j - 1
       


#croisement de sacs les parents 1 et 2 donnent les enfants 1 et 2. la 1ere moitie des parents 1 et 2 est recopiée dans les enfants 1 et 2,  puis la seconde moitiee des parents 2 et 1 est recopiée dans les enfants 1 et 2
def croisementSacs(parent1:Sac, parent2:Sac, enfant1:Sac, enfant2:Sac):
    enfant1.genome = zeros(NBOBJETS, int)
    enfant2.genome = zeros(NBOBJETS, int)
    milieu = NBOBJETS/2
    for i in range (0,int(milieu)):
            enfant1.genome[i] = parent1.genome[i]
            enfant2.genome[i] = parent2.genome[i]
    for i in range (int(milieu),NBOBJETS):
            enfant1.genome[i] = parent2.genome[i]
            enfant2.genome[i] = parent1.genome[i]
    calculProprietes(enfant1)
    calculProprietes(enfant2)
    
#demande le croisement des 2 premiers sacs du tableau population pour obtenir 2 enfants qui seront placés en fin de tableau 
def croisementPopulation(population:TabPopulation):
    parent1 = population[0]
    parent2 = population[1]
    enfant1 = Sac()
    enfant2 = Sac()
    croisementSacs(parent1, parent2, enfant1, enfant2)
    population[NBSACS-1] = enfant1
    population[NBSACS-2] = enfant2

#effectue une mutation : un sac (s'il ne fait pas parti des 2 premiers) est choisi au hasard et une valeur de son contenu est transformee (0 <-> 1)*/
def mutationPopulation(population:TabPopulation):
    nb = len(population)
    noMutant = randint(2,nb-1)
    sacMutant = population[noMutant]    
    noGeneMutant = randint(0,NBOBJETS-1)
    if population[noMutant].genome[noGeneMutant] == 1 :
            population[noMutant].genome[noGeneMutant] = 0 
    else : 
            population[noMutant].genome[noGeneMutant] = 1 
    calculProprietes(sacMutant)

#effectue nb croisements et mutations des sacs du tableau population*/
def reproductionDeSacs(nb:int, population:TabPopulation):
    for i in range (0,nb):
            triPopulationInsertion(population)
            croisementPopulation(population)
            mutationPopulation(population)
  
    
#petite fonction pour tester le tout..*/
def vie():
    population:TabPopulation= zeros(NBSACS, Sac)
    creerPopulation(population)
    reproductionDeSacs(5, population)
    triPopulationInsertion(population)
    affichePopulation(population)
    print("\nLe meilleur sac est celui-ci : \n")
    afficheSac(population[0])
                                                                        #FIN DU TP#


vie()
print("\n\n")
a = input()
