# SCRIPT CRYPTAGE ENIGMA-CESAR

## 1. Description générale du programme

Ce script permet de crypter et de décrypter du texte en utilisant la méthode César ou la méthode Enigma-César. Il offre une interface assez conviviale pour choisir entre les différentes méthodes de cryptage et de décryptage. L'utilisateur peut entrer le texte à crypter ou décrypter directement dans la console du programme ou consigné dans un fichier texte.

## 2. Configurations compatibles

- Python 3.12 et versions compatibles.

- La version de l’OS (Windows 10, Ubuntu 20, Mac...).

## 3. Packages et modules

Ce script fait appelle aux modules random et ```string``` déjà implémentés à ```Python 3```. Il ne nécessite donc aucune installation de package supplémentaire.

## 4. Utilisation du programme

***Pour utiliser ce script, suivez ces étapes*** :

1. Assurez-vous d'avoir Python installé sur votre système.

2. Téléchargez le script :
   
      git clone (https://github.com/HlCyril/enigma_cesar.git)

3. Exécutez le script.

4. Choisissez l'opération de cryptage ou de décryptage que vous souhaitez effectuer en entrant le numéro correspondant à l'option.

5. Suivez les instructions à l'écran pour choisir l'opération de cryptage ou de décryptage que vous souhaitez effectuer, ainsi que les paramètres nécessaires.

```
Choisir choix:
 "1": Cryptage avec la méthode César,
 "2": Cryptage avec la méthode Enigma-César,
 "3": Décryptage avec la méthode César,
 "4": Décryptage avec la méthode Enigma-César,
 1

Donnez une nombre entier comme clef de cryptage: 3
```

## Options de Cryptage et de Décryptage

Le script propose les options suivantes :

- **Cryptage avec la méthode de César** : Vous pouvez crypter du texte en utilisant la méthode de César en spécifiant une clé de cryptage sous forme d'un entier.

- **Cryptage avec la méthode Enigma-César** : Vous pouvez crypter du texte en utilisant la méthode Enigma-César en spécifiant une clé de cryptage sous forme d'une liste d'entiers.

- **Décryptage avec la méthode de César** : Vous pouvez décrypter du texte crypté avec la méthode de César en spécifiant la même clé de cryptage utilisée pour le cryptage.

- **Décryptage avec la méthode Enigma-César** : Vous pouvez décrypter du texte crypté avec la méthode Enigma-César en spécifiant la clé de cryptage négative utilisée pour le cryptage.

## Description des Fonctions du script

***Les fonctionnalités globales du programme sont les suivantes*** :

- Choix aléatoire d'un mot parmi une liste prédéfinie.

- Choix aléatoire d'un mot parmi une liste fournie par le joueur. Nommez votre fichier : "mots_pendu.txt". Les mots avec accents et caractère spéciaux sont pris en compte par le programme.

********Par ailleur le code est composé principlement de fonctions.****

Ce script nécessite Python et la bibliothèque `fonction.py`. Assurez-vous de télécharger également le fichier `fonction.py` et de le placer dans le même répertoire que le script principal.

- **lire_fichier(fichier_txt)** : Cette fonction prend en entrée le chemin d'un fichier texte et retourne son contenu sous forme d'une seule chaîne de caractères.
- **modifier_caracteres_speciaux(mot, caracteres_speciaux, caracteres_normaux)** : Cette fonction permet de modifier les caractères spéciaux **'àâèéêëôîïûùüç'** d'un mot en caractère normaux **aaeeeeoiiuuuc**.
- **separer_mot_en_item_liste(contenu)** : Cette fonction permet de diviser une chaine de caractère en mots individuels en utilisant l'espace comme séparateur.
- **modifier_majuscules(liste_mots)** : Cette fonction prend en entrée une liste de mots et convertit chaque mot en minuscules.
- **creer_liste_de_chaque_mot(fichier_texte)** : Cette fonction prend en entrée un fichier texte et retourne une liste contenant chaque mot du fichier.
- **cryptage_cesar(mot, clef, alphabet)** : Cette fonction prend en entrée un mot et une clé de cryptage, pour retourner le mot crypté par la méthode César.

- **cryptage_enigma_cesar(mot, clef, alphabet)** : Cette fonction prend en entrée un mot et une clé de cryptage, pour retourner le mot crypté par la méthode Enigma-César.
- **clef_potentielle(texte_crypte, lettre_alphabet, alphabet)** : Cette fonction prend en entrée un texte crypté et retourne la clé de décryptage potentielle.
- **mot(fichier_txt)** : Cette fonction prend en entrée un fichier texte contenant une liste de mots et retourne une liste contenant chaque ligne du fichier en tant que mot.

## Auteurs

Cyril HELOU

Stéphane Hu

Cédric Foffé Ngoufo
