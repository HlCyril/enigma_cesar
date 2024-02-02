import mod
import string
print("Ce programme va crypter vos phrases avec la méthode du cryptage de César")

# On récupère la clef de cryptage
cesar = int(input("Donnez une nombre entier comme clef de cryptage"))
clef = [1,2,1]
alphabet = list(string.ascii_lowercase)

liste_txt = mod.lire_fichier("phrases.txt")
print(liste_txt)
liste_txt = mod.enlever_accents(liste_txt)
print(liste_txt)
liste_txt = mod.liste(liste_txt)
print(liste_txt)
liste_txt = [mot.lower() for mot in liste_txt]
print(liste_txt)
txt_crypte = []

for mot in liste_txt:
    txt_crypte.append(mod.cryptage_cesar(mot, alphabet, cesar))
txt_decrypte = []
for mot in txt_crypte:
    txt_decrypte.append(mod.cryptage_cesar(mot, alphabet, -cesar))

print('Txt :', ' '.join(liste_txt))
print('Txt cryp :', ' '.join(txt_crypte))
print('Txt dcrypt :', ' '.join(txt_decrypte))
txt_crypte_e = []
for mot in liste_txt:
    txt_crypte_e.append(mod.cryptage_enigma_cesar(mot, alphabet, clef))
print('Txt cryp :', ' '.join(txt_crypte_e))
txt_decrypte_e = []
clef_decrypte = [-i for i in clef]
print(clef_decrypte)
for mot in txt_crypte_e:
    txt_decrypte_e.append(mod.cryptage_enigma_cesar(mot, alphabet, clef_decrypte))
print('Txt decrypt enigma cesar', ' '.join(txt_decrypte_e))
