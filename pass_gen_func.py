import random
import string


def pass_gen(parola_uzunlugu):
    semboller = string.ascii_letters + string.digits + string.punctuation
    parola = ""

    for i in range(parola_uzunlugu):
        parola = parola + random.choice(semboller)

    return parola