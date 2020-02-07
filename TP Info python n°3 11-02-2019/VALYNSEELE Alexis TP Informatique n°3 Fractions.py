###################################
# Auteur : Valynseele Alexis      #
# Titre  :  Fractions - TP 3      #
# L1 INFO S2 - ISTV               #
###################################
                                                                        #DEBUT DU TP#
#Exercice 1

#definition des types :
class Fraction:
 num:int
 denom:int

#Exercice 2
#fonction creer_fraction : renvoie une fraction dont le numerateur et le denominateur ont été passés en entrée
def creer_fraction(num:int, denom:int)->Fraction:
 f:Fraction = Fraction()
 f.num = num
 f.denom = denom
 return f

#Exercice 3 
#fonction saisir_fonction : renvoie une fraction entrée par l'utilisateur 
def saisir_fraction (f:Fraction)->Fraction:
 num = input("Entrez votre numerateur : ")
 denom = input("Entrez votre denominateur : ")
 return creer_fraction(int(num),int(denom))
 
 #Exercice 4
#fonction f2str : transformme une fraction en chaine de caractères
def f2str(f:Fraction)->str:
 if f.num == 0 :
     return '0'
 elif f.denom == 1  :
    return str(f.num)
 elif f.denom == 0 :
    print("Erreur division par 0")
 else :
     return str(f.num) + '/' + str(f.denom)

#Exercice 5
#fonction pgcd : renvoie le pgcd entre deux entiers a et b 
def pgcd(a:int, b:int)->int :
    #définition du min et du max entre les deux entrées pour effectuer la méthode par division (on divise le plus grand par le plus petit)
 if a>b:
     dividende = a
     diviseur  = b
 else:
    dividende = b
    diviseur  = a
    #gestion des cas particuliers : divison par 0 ou l'une des deux entrées à 0 
 if dividende==0 and diviseur == 0 :
     return 0
 elif dividende==0 : 
     return 1
    #calcul du pgcd 
 reste = 1
 while reste !=  0:
    reste = dividende%diviseur
    dividende = diviseur
    diviseur = reste
 return dividende

#Exercice 6
#Procedure simplifieFraction : passe sous forme forme simplifiée la fraction passée en entrée
def simplifieFraction(f:Fraction) : 
 simplificateur = pgcd(f.num,f.denom)
 f.num /= simplificateur
 f.denom /= simplificateur

#Exercice 7 
#Fonction addition : renvoie l'addition sous forme de fraction de deux fractions passées en entrée
def addition(a:Fraction, b:Fraction)->Fraction:
 f:Fraction = Fraction()
 if a.denom == b.denom:
   f.num = a.num + b.num
   f.denom = a.denom
 else:
   f.num = (a.num * b.denom) + (a.denom * b.num)
   f.denom = a.denom * b.denom
 simplifieFraction(f)
 return f

#Exercice 8 
#Fonction soustraction : renvoie la soustraction sous forme de fraction de deux fractions passées en entrée
def soustraction(a:Fraction, b:Fraction)->Fraction:
 f:Fraction = Fraction()
 if a.denom == b.denom:
   f.num = a.num - b.num
   f.denom = a.denom
 else:
   f.num = (a.num * b.denom) - (a.denom * b.num)
   f.denom = a.denom * b.denom
 simplifieFraction(f)
 return f

 #Exerice 9 
#Fonction multiplication : renvoie la multiplication sous forme de fraction de deux fractions passées en entrée
def multiplication(a:Fraction, b:Fraction)->Fraction:
 f:Fraction = Fraction()
 f.num = a.num * b.num
 f.denom = a.denom * b.denom
 simplifieFraction(f)
 return f

#Exerice 10
#Fonction division : renvoie la divison sous forme de fraction de deux fractions passées en entrée
def division(a:Fraction, b:Fraction)->Fraction:
 f:Fraction = Fraction()
 f.num = a.num * b.denom
 f.denom = a.denom * b.num
 simplifieFraction(f)
 return f

#Exercice 11
#Procedure menu : affiche un menu sous forme de texte et affiche 3 fractions
def menu(f1:Fraction, f2:Fraction, f3:Fraction):
 print("------- GESTION DE FRACTIONS -------")
 print("F1 = " + f2str(f1))
 print("F2 = " + f2str(f2))
 print("F3 = " + f2str(f3))
 print("1 -> saisir F1")
 print("2 -> saisir F2")
 print("3 -> F3 = F1 + F2")
 print("4 -> F3 = F1 - F2")
 print("5 -> F3 = F1 * F2")
 print("6 -> F3 = F1 / F2")
 print("0 -> Quitter")
 

 #Exercice 12
#Procedure interagir : permet d'interagir avec menu()
def interagir() :
 f1:Fraction = Fraction()
 f2:Fraction = Fraction()
 f3:Fraction = Fraction()
 f1 = creer_fraction(0,0)
 f2 = creer_fraction(0,0)
 f3 = creer_fraction(0,0)
 choix = 1
 while choix != '0' : 
    menu(f1,f2,f3)
    choix = input ("\nEntrez votre choix : ")
    if choix == '1' :
       f1 = saisir_fraction(f1)
       simplifieFraction(f1)
    elif choix == '2' :
       f2 = saisir_fraction(f2)
       simplifieFraction(f2)
    elif choix == '3' :
       f3 = addition(f1,f2)
       print ("\n F3 = " + f2str(f1) + " + " + f2str(f2) + " = " + f2str(f3) + "\n")
    elif choix == '4' :
       f3 = soustraction(f1,f2)
       print ("\n F3 = " + f2str(f1) + " - " + f2str(f2) + " = " + f2str(f3) + "\n")
    elif choix == '5' :
       f3 = multiplication(f1,f2)
       print ("\n F3 = " + f2str(f1) + " * " + f2str(f2) + " = " + f2str(f3) + "\n")
    elif choix == '6' :
       f3 = division(f1,f2)
       print ("\n F3 = " + f2str(f1) + " / " + f2str(f2) + " = " + f2str(f3) + "\n")
    elif choix == '0' :
       print ("\nfin du programme, aurevoir")
    else :
       print("\nERREUR - Valeur non reconnue\n")

                                                                          #FIN DU TP#
interagir ()


 
 

