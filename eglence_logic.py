import random

def yazitura():
    para = random.randint(0, 2)
    if para == 0:
        return ":coin: **YAZI**"
    else:
        return ":coin: **TURA**"
    
def randomemoji():
    emoji = ""
    emoji_sozluk = [':white_heart:',':nerd_face:',':thumbsdown:',':thumbsup:']
    emoji = random.choice(emoji_sozluk)

    return emoji

def randommuzik():
    muzik = ""
    muzik_sozluk = [':white_heart:',':nerd_face:',':thumbsdown:',':thumbsup:']
    muzik = random.choice(muzik_sozluk)

    return muzik
