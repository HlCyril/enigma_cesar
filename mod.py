from unidecode import unidecode


def lire_fichier(fichier_txt):
    with open(fichier_txt, 'r', encoding='utf-8') as fichier:
        contenu = fichier.read()
    return contenu


def enlever_accents(contenu):
    return unidecode(contenu)


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
