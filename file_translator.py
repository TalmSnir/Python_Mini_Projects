from translate import Translator

f = None
try:
    with open('file_to_translate.txt', 'r') as f:
        text_to_translate = f.read()

    translator = Translator(to_lang="zh")
    translated_text = translator.translate(text_to_translate)
    print(translated_text)

except FileNotFoundError as er:
    print('its seems that there is no such file')
except IOError as err:
    print('there is a problem with reading/writing ')

finally:
    if f != None:
        f.close()
