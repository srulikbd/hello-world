import re



def clean_text(text):
    eng_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # english_free = ''.join([ch for ch in doc if ch not in eng_letters])
    # stop_free = ' '.join([i for i in punc_free.split() if i not in arb_long_sw])
    try:
        stop_free = re.sub("^RT:", "", text)
        stop_free = re.sub("User Location:.*", "", stop_free)
        # stop_free = re.sub(r'http\S+', "", stop_free)
        stop_free = re.sub(r'\bhttps?://\S+', "", stop_free)
        stop_free = re.sub("@.*:", "", stop_free)
        # stop_free = re.sub("@.*", "", stop_free)
        stop_free = stop_free.strip()
    except:
        stop_free = ''
        print('cant parse the text')

    return stop_free