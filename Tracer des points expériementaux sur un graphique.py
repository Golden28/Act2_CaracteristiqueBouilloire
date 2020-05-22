""
Étude de la caractéristique d'un conducteur ohmnique.
Niveau : Seconde
Chapitre : 11 Électricité

Consignes : 
  pour untiliser ce programme, il vous sera nécéssaire de remplacer les données expériementalles
  pour que le graphique affiché soit complet, il vous sera nécéssaire  de Remplacer quelques ? dans la fonction afficher_graphe()
  Vous trouvez plus d informations dans le programme sous forme de commentaire
"""

import matplotlib.pyplot as plt
import numpy as np


#### Fonction
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


## Appels de fontion
afficher_graphe()
