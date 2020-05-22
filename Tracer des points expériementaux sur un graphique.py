"""
Étude de la caractéristique d'un conducteur ohmnique.
Niveau : Seconde
Chapitre : 11 Électricité
"""
import matplotlib.pyplot as plt
import numpy as np


#### Fonction
def  calculer_coefdirecteur_modele(I,U):
    delta_I = sum(I)/len(I)
    delta_U = sum(U)/len(U)
    a = delta_U/delta_I
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
    plt.xlabel("Intensité I  (en A)")
    plt.ylabel("Tension U (en V)")
    plt.title("Caractéristique U = f(I)")
    plt.grid()

    # Enregistrement sous la forme d'une image
    plt.savefig("Caractéristique de la bouilloire.png")

    # Affichage
    plt.show()


##### Programme principal
## Données expérimentales
U =[0.0, 3.0, 4.42, 6.03, 7.55, 9.08, 11.93]
I =[0.0, 0.13, 0.19, 0.23, 0.29, 0.36, 0.49]


#(a, b) = calculer_modele(X=i, Y=u)
a= calculer_coefdirecteur_modele(I, U)
tracer_modele(a)
afficher_equation_modele(a)
afficher_graphe()

