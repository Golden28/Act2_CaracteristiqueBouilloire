""
Étude de la caractéristique d'un conducteur ohmnique.
Niveau : Seconde
Chapitre : 11 Électricité




"""
import matplotlib.pyplot as plt
import numpy as np


#### Fonction
def  calculer_coefdirecteur_modele(I,U):
  """
  Cette fonction n'est pas valide, elle doit être complétés pour pouvoir être utilisée
  suivre les indications disponnibles en commentaires
  """
    Xmoyen = sum(?)/len(?)   # Remplacer les ? par une variable contenant une liste
    Ymoyen = sum(?)/len(?)   # Remplacer les ? par une variable contenant une liste
    a = ???                  # Remplacer les ??? par l'expression qui permet de calculer le coefficient a
    return a

def tracer_modele(a):
    X =[x /10 for x in range(60)]
    Y = [x*a for x in X]
    plt.plot(X, Y, "b-", label="Modelisation")


def afficher_equation_modele(a):
    equation = "Équation du modèle : Y = a X"
    a = "Avec a =" + str(round(a, 1))
    plt.text(0.05, 11, equation, color="blue")
    plt.text(0.05, 10.5, a, color="blue")



def afficher_graphe():
    """Configuration de la représentation graphique et affichage"""
    plt.plot(I, U, 'r+', markersize=9)
    plt.xlim(0.00, 0.55)
    plt.ylim(0.00, 13)
    plt.xlabel("??????????") # Remplacer les ??? par une légende adapté
    plt.ylabel("??????????") # Remplacer les ??? par une légende adapté
    plt.title("???????????") # Remplacer les ??? par une légende adapté
    plt.grid()

    # Enregistrement sous la forme d'une image
    plt.savefig("Caractéristique de la bouilloire.png")

    # Affichage
    plt.show()


##### Programme principal
## Données expérimentales
U =[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] # Modifiez cette liste par vos données
I =[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] # Modifiez cette liste par vos données



# a = calculer_coefdirecteur_modele(I, U)
# Remplacer ce commentaire par l'appel de la fonction permétant de tracer le modèle
# Remplacer ce commentaire par l'appel de la fonction permétant l'affichage de l'équation du modéle



afficher_graphe()
