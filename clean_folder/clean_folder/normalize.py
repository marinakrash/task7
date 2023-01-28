
import re
import transliterate

def normalize(name):
    l_name = transliterate.translit(name, language_code='ru', reversed=True)
    nor_name=re.sub(r'\W^.', '_', l_name)
    return(nor_name)


