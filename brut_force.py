import fonction
import string

print("Ce programme va brut force un texte écrit avec le crypte de césar")

alphabet = list(string.ascii_lowercase)
mots_populaires = fonction.mot('french.txt')
# D'après l'analyse en fréquence des lettres
#alphabet_ordre_utilisation = 'eaisnrtoiudcmpgbvhfqyxjkwz'


texte_crypte = fonction.creer_liste_de_chaque_mot('texte_cesar.txt')

grande_liste = []
toutes_les_clefs = []
for lettre in alphabet:
    clef = fonction.clef_potentielle(texte_crypte, lettre)
    toutes_les_clefs.append(clef)
    if lettre == 'i':
        print(clef)
    liste_par_clef = []
    for mot in texte_crypte:
        mot_decrypte = []
        for caractere in mot:
            if caractere in alphabet:
                mot_decrypte.append(alphabet[(-clef+alphabet.index(caractere)) % len(alphabet)])
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
print(indice)
print(' '.join(grande_liste[indice]))
print('la clef était: ',toutes_les_clefs[indice])

