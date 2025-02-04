Pour lancer le projet.
## main modifiable à volonté
python main.py 
## tests
python -m unittest discover -s tests

> Projet > Réaliser par Letonade (Git)
> Énoncé > propriété de Equinox
---------------------------------------------------------
Bonjour X, 

Voici comme convenu l'exercice technique à faire svp avant votre rencontre avec Y ///.

Merci et belle fin de semaine, 

Amusez-vous ! ;)
----------------------------------------------------------

Énoncé:

Note avant de commencer : la solution doit être faite comme si elle était réalisée pour un client et doit poser les bonnes bases de travail de votre future équipe. Elle doit être exemplaire.

L'équipe de production de Back to the Future voudrait remettre au goût du jour sa saga avec une technique marketing imparable :

Revenir dans le passé, en 2000 ! Et passer un deal super smart avec une boutique de vente de DVD (on espère que vous vous rappelez encore ce que c'est…) avec une promo qui déchire :

    Le DVD d'un volet de la saga vaut 15 €
    Pour l'achat de 2 volets DIFFÉRENTS de la saga, on applique une réduction de 10 % sur l'ensemble des DVDs "Back to the Future" achetés
    Pour l'achat de 3 volets DIFFÉRENTS de la saga, on applique une réduction de 20 % sur l'ensemble des DVDs "Back to the Future" achetés

La boutique de DVDs vend également d'autres films qui coûtent chacun 20 €.

L'équipe de production vous charge d'écrire un programme qui aura le comportement suivant :

    En entrée, un panier sous forme de texte, séparé par des retours à la ligne qui contient le nom des films achetés
    En sortie, le nombre représentant le prix

Vous êtes libre de montrer le résultat de la manière qui vous convient et cela peut rester très minimaliste, tant qu'il est clair que le programme sait lire le format d'entrée et qu'il suit bien les règles spécifiées. Néanmoins, comme indiqué en début d’énoncé, ce code devra être traité comme si vous l’initiiez pour votre future équipe.

Vous pourrez choisir le langage qui vous paraîtra le plus pertinent (dans lequel vous êtes à l'aise, c'est mieux), et qui devra pouvoir s'exécuter sur une JVM ou Python. Vous vous assurerez que le projet livré permette à quelqu'un ayant le SDK adéquat de lancer, utiliser et maintenir votre programme aisément. En résumé, le code doit être de très bonne qualité.

Lors de l’éventuel entretien, venez avec votre code sur votre PC (pour vous permettre d’avoir un support sur lequel vous avez la main).

 
Quelques exemples d’entrées et sortie

Exemple n°1

Entrée :

Back to the Future 1 Back to the Future 2 Back to the Future 3

Sortie :

36

 

 

Exemple n°2

Entrée :

Back to the Future 1 Back to the Future 3

Sortie :

27

 

 

Exemple n°3 :

Entrée :

Back to the Future 1

Sortie :

15

 

 

Exemple n°4 :

Entrée :

Back to the Future 1 Back to the Future 2 Back to the Future 3 Back to the Future 2

Sortie :

48

Explication : ((15*4)*0.8) = 48

 

 

Exemple n°5

Entrée :

Back to the Future 1 Back to the Future 2 Back to the Future 3 La chèvre

Sortie :

56

 

Explication : ((15*3)*0.8)+20 = 56

 