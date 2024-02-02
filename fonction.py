import string

def lire_fichier(fichier_txt):
    # Lire le fichier .txt 
    with open(fichier_txt, 'r', encoding='utf-8') as fichier:

        # Mettre le contenu dans une liste
        contenu = fichier.read()

    return contenu


# Modifier les caractères spéciaux 'àâèéêëôîû' d'un mot
def modifier_caracteres_speciaux(mot, caracteres_speciaux='àâèéêëôîïûùüç', caracteres_normaux='aaeeeeoiiuuuc'):
    # Pour chaque lettre du mot
    for lettre in mot:

        # Si la lettre est parmi les caractères spéciaux
        if lettre in caracteres_speciaux:
            # Trouver sa position dans les caractères spéciaux
            index_correspondant = caracteres_speciaux.find(lettre)

            # Remplacer la lettre par un caractère normal
            mot = mot.replace(lettre, caracteres_normaux[index_correspondant])

    # Retourner le mot sans caractères spéciaux
    return mot

# Séparer les mots en items d'une liste
def separer_mot_en_item_liste(contenu):

    # séparation à chaque espace
    return contenu.split(' ')

# Modifier les majuscules
def modifier_majuscules(liste_mots):
    liste_sans_majuscule = []
    for chaque_mot in liste_mots:
        liste_sans_majuscule.append(chaque_mot.lower())
    return liste_sans_majuscule

# Créer une liste avec comme item chaque mot sans caractère spécial et sans majuscule
def creer_liste_de_chaque_mot(fichier_texte):
    # Lire le fichier .txt
    liste_txt = lire_fichier(fichier_texte)

    # Modififier les caractères spéciaux de la liste
    liste_txt = modifier_caracteres_speciaux(liste_txt)

    # Séparer les mots en items à chaque espace
    liste_txt = separer_mot_en_item_liste(liste_txt)

    # Modifier les majuscules en minuscules
    liste_txt = modifier_majuscules(liste_txt)

    return liste_txt


# Crypter avec la méthode de César
def cryptage_cesar(mot, clef, alphabet = list(string.ascii_lowercase)):
    #
    mot_crypte = []
    for caractere in mot:
        if caractere in alphabet:
            mot_crypte.append(alphabet[(clef+alphabet.index(caractere)) % len(alphabet)])
        else:
            mot_crypte.append(caractere)
    
    return ''.join(mot_crypte)


def cryptage_enigma_cesar(mot, clef, alphabet = list(string.ascii_lowercase)):
    mot_crypte = []
    indice = 0
    for caractere in mot:
        if caractere in alphabet:
            # import pdb ; pdb.set_trace()
            mot_crypte.append(alphabet[(clef[indice % len(clef)]+alphabet.index(caractere)) % len(alphabet)])
            indice += 1
        else:
            mot_crypte.append(caractere)
    return ''.join(mot_crypte)
