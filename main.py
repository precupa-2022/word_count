############################################
# Alexander Precup 402
# TP1 : Compter le nombre des mots
#############################################

# fonction count_word
# phrase : argument de type string pour la fonction count_word
# la fonction retourne le nombre de mots dans l'argument phrase
def count_word(phrase):
    return print(len(phrase.split(" ")))

# afficher le nombre de mots en utilisant la fonction count_word
print(count_word("Ceci est une longue phrase pour TP1"))