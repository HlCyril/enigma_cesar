from unidecode import unidecode


def lire_fichier(fichier_txt):
    with open(fichier_txt, 'r', encoding='utf-8') as fichier:
        contenu = fichier.read()
    return contenu


def enlever_accents(contenu):
    return unidecode(contenu)

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

def creer_liste_sans_caracteres_speciaux(liste_mots):
    # Créer une nouvelle liste vide
    liste_mot_sans_caracteres_speciaux = []

    # Pour chaque mot dans la liste
    for chaque_mot in liste_mots:
        # Modifier les caractères spéciaux dans le mot
        nouveau_mot = modifier_caracteres_speciaux(chaque_mot)

        # Ajouter le nouveau mot dans la nouvelle liste
        liste_mot_sans_caracteres_speciaux.append(nouveau_mot)

    # Retourner une nouvelle liste de mots sans caractères spéciaux
    return liste_mot_sans_caracteres_speciaux

def liste(contenu):
    return contenu.split()


def cryptage_cesar(mot, alphabet, cesar):
    # avion.
    mot_crypte = []
    for caractere in mot:
        if caractere in alphabet:
            mot_crypte.append(alphabet[(cesar+alphabet.index(caractere)) % len(alphabet)])
        else:
            mot_crypte.append(caractere)
    print(mot_crypte)
    return ''.join(mot_crypte)

def cryptage_enigma_cesar(mot, alphabet, clef):
    mot_crypte = []
    indice = 0
    for caractere in mot:
        if caractere in alphabet:
            #import pdb ; pdb.set_trace()
            mot_crypte.append(alphabet[(clef[indice%len(clef)]+alphabet.index(caractere)) % len(alphabet)])
            indice += 1
        else:
            mot_crypte.append(caractere)
    return ''.join(mot_crypte)
