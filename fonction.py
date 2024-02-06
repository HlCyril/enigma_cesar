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
def cryptage_cesar(mot, clef, alphabet=list(string.ascii_lowercase)):
    #
    mot_crypte = []
    for caractere in mot:
        if caractere in alphabet:
            mot_crypte.append(alphabet[(clef+alphabet.index(caractere)) % len(alphabet)])
        else:
            mot_crypte.append(caractere)
    
    return ''.join(mot_crypte)


def cryptage_enigma_cesar(mot, clef, alphabet=list(string.ascii_lowercase)):
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


# J'ai ajouté ces deux fonctions pour le décryptage
def clef_potentielle(texte_crypte, lettre_alphabet, alphabet=list(string.ascii_lowercase)):
    for mot in texte_crypte:
        for caractere in mot:
            if caractere in alphabet:
                return abs(alphabet.index(lettre_alphabet)-alphabet.index(caractere))


def mots_fichier(fichier_txt):
    with open(fichier_txt, 'r', encoding='utf-8') as fichier:
        lignes = fichier.readlines()
        liste_mots = [mot.strip() for mot in lignes]
    return liste_mots


def trouver_premier_3_lettres(texte, alphabet):
    for mot in texte:
        if len(mot) >= 3:
            if mot[0] in alphabet and mot[1] in alphabet and mot[2] in alphabet:
                return mot


def mots_en_communs(texte_crypte, base_de_donnee):
    mots_communs = set(texte_crypte) & set(base_de_donnee)
    return len(mots_communs)


def brut_force_cesar(texte_crypte, alphabet=list(string.ascii_lowercase)):
    mots_populaires = mots_fichier('french.txt')
    mots_populaires = [mot.lower() for mot in mots_populaires]
    grande_liste = []
    toutes_les_clefs = []
    for lettre in alphabet:
        clef = clef_potentielle(texte_crypte, lettre)
        toutes_les_clefs.append(clef)
        liste_par_clef = []
        for mot in texte_crypte:
            mot_decrypte = []
            for caractere in mot:
                if caractere in alphabet:
                    mot_decrypte.append(alphabet[(-clef + alphabet.index(caractere)) % len(alphabet)])
                else:
                    mot_decrypte.append(caractere)

            liste_par_clef.append(''.join(mot_decrypte))
        grande_liste.append(liste_par_clef)

    liste_compteur = []
    for sous_liste in grande_liste:
        compteur = 0
        for mot in sous_liste:
            if mot in mots_populaires:
                compteur += 1
        liste_compteur.append(compteur)

    indice = liste_compteur.index(max(liste_compteur))
    print(' '.join(grande_liste[indice]))
    print('la clef était: ', toutes_les_clefs[indice])


def brut_force_enigma_cesar(texte_crypte, alphabet=list(string.ascii_lowercase)):
    mots_populaires = mots_fichier('french.txt')
    mots_populaires = [mot.lower() for mot in mots_populaires]
    compteur1 = 0
    vraies_clefs = []
    texte_decrypte = []
    gros_compteur = []
    for i in range(len(alphabet)):
        for j in range(len(alphabet)):
            for k in range(len(alphabet)):
                clefs = [i, j, k]
                compteur2 = 0
                texte_decrypte_potentiel = []
                for mot in texte_crypte:
                    mot_decrypte = []
                    indice = 0
                    for caractere in mot:
                        if caractere in alphabet:
                            mot_decrypte.append(
                                alphabet[(-clefs[indice % len(clefs)] + alphabet.index(caractere)) % len(alphabet)])
                            indice += 1
                        else:
                            mot_decrypte.append(caractere)
                    texte_decrypte_potentiel.append(''.join(mot_decrypte))
                    compteur2 = mots_en_communs(texte_decrypte_potentiel, mots_populaires)
                if compteur2 > compteur1:
                    vraies_clefs = clefs
                    texte_decrypte = texte_decrypte_potentiel
                    compteur1 = compteur2
                gros_compteur.append(compteur2)
    print('Les clef sont', vraies_clefs)
    print('Le texte décrypté est :')
    print(' '.join(texte_decrypte))
