###################################
# Auteur : Valynseele Alexis      #
# Titre  :  BonCompte - TP 4      #
# L1 INFO S2 - ISTV               #
###################################
                                                                        #DEBUT DU TP#

#Entete
from numpy import array,zeros
from typing import Iterable
from random import randint
##Les Types
TabInt = Iterable[int]
TexteOpe = (str,15)
TabOpe = Iterable[str]
class Calcul:
    etapes:TabOpe=None
    valeur:int=0
##Les constantes
SIGNES:TabOpe=array(["+", "*", "-", "//"])

#Exercice 1
def copier_tab(src: TabInt, dest: TabInt, nb: int) :
    for i in range (0,nb):
        dest [i] = src [i]

#Exercice 2
def extraire(tab: TabInt, i: int, pos_fin: int) -> int :
    valeur = tab[i]
    tab[i] = tab [pos_fin]
    tab[pos_fin] = 0
    return valeur

#Exercice 3
def verifier(op: str, a: int, b: int) -> bool :
    if op =='//':
        if(b == 1) :
            return False
        elif (b == 0):
            return False
        elif (a%b) != 0 :
            return False
        else:
            return True
    elif op == '*':
        if(b == 1):
            return False
        else :
            return True
    elif op == '-':
        if (a-b) < 0 :
            return False
        else :
            return True
    else :
        return True
#Exercice 4
def calculer(op: str, a: int, b: int) -> int : 
    if  op == '//':
        return int((a//b))
    elif op == '*':
        return int((a*b))
    elif op == '+':
        return int((a+b))
    elif op == '-':
        return int((a-b))

#Exercice 5


def choisir_operateur(a: int, b: int) -> str:
    x = randint(0,3)
    op = SIGNES[x]
    test = verifier(op, a,b)
    while test != True : 
        x = randint(0, 3)
        op = SIGNES[x]
        test = verifier(op, a, b)
    return op

#Exercice 6
def essayer_calcul (tab_num : TabInt, but: int)-> Calcul : 
    calcul: Calcul = Calcul()
    copie_num:TabInt = zeros(6,int)
    j : int = 0
    a : int = 0
    b : int = 0
    signe : str = ''
    copier_tab(tab_num,copie_num,6)
    calcul.etapes = zeros(5,TexteOpe)
    for nb in range (5,0,-1):
        #prendre une valeur entre 0 et nb
        i = randint(0,nb)
        a = extraire(copie_num,i,nb)
        i = randint(0,nb-1)
        b = extraire(copie_num,i,nb-1)
        signe = choisir_operateur(a,b)
        valeur = calculer(signe,a,b)
        copie_num[nb-1] = valeur
        calcul.valeur = valeur
        calcul.etapes[j]= '' + str(a) + signe + str(b) + '=' + str(valeur)
        j = j + 1
        if (int(valeur)-int(but)) == 0:
            return  calcul
    return calcul
    
#Exercice 7
def afficher_solution(calcul:Calcul):
    for i in range (0,5):
        print(calcul.etapes[i])

def lancer_essais() :
    tab_num:TabInt = zeros(6,int)
    but:int = 0
    resultat : Calcul = Calcul()
    best : Calcul = Calcul()
    best.etapes = zeros(5, TexteOpe)
    resultat.valeur = 0
    i:int = 0

    print("Veuillez entrer vos 6 nombres")
    for i in range (0,6):
        tab_num[i] = input()
    print("Veuillez entrer votre but")
    but = input()
    resultat = essayer_calcul(tab_num,but)
    best.valeur = int(resultat.valeur)
    i = i + 1
    if (int(resultat.valeur) == int(but)):
        print("Le but a ete atteint en 1 essai")
    else:
        while (int(resultat.valeur) != int(but) and  i<10000):
            resultat = essayer_calcul(tab_num, but)
            i = i + 1
            if(abs(int(but) - int(resultat.valeur)) < abs(int(but) - int(best.valeur))) :
                best.valeur = resultat.valeur
                for i in range (0,5):
                    best.etapes[i] = resultat.etapes[i]
    if (int(resultat.valeur) == int(but)):
        print("\nLe but a ete atteint en ",i," essai\n")
        print("Voici le détail de la solution trouvée :\n")
        afficher_solution(resultat)
    else : 
        print("\nLe but n'a pas ete atteint en ", i, " essai\n")
        print("Le meilleur resultat est : ",best.valeur,"\n")
        print("Voici le détail de cette solution : \n")
        afficher_solution(best)
 
                                                                          #FIN DU TP#																																	  
#main
lancer_essais()
