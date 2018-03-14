import os
from odf import text, teletype
from odf.opendocument import load

# textdoc = load("my document.odt")
# allparas = textdoc.getElementsByType(text.P)
# print teletype.extractText(allparas[0])

# observar lo primeros
# lo segnudo no

textdoc = load("plantilla.odt")
texts = textdoc.getElementsByType(text.P)
s = len(texts)
for i in range(s):
    old_text = teletype.extractText(texts[i])
    new_text = old_text.replace('{fecha}','01/01/01')
    new_S = text.P()
    new_S.setAttribute("stylename",texts[i].getAttribute("stylename"))
    new_S.addText(new_text)
    texts[i].parentNode.insertBefore(new_S,texts[i])
    texts[i].parentNode.removeChild(texts[i])
textdoc.save('myfile.odt')

# esto deberia funcionar.. revisar

# datos = [("{fecha}", "01/01/01"), ('{nombre}', 'diego')]
# valor = open('cc.xml', 'wb')
# with open("1/content.xml", 'rb') as odt:
#         for lista in datos:
#                 valor.write(odt.replace(lista[0], lista[1]))
#                 print(valor)
#                 print('------------------------------------------------')
        # print(dato[0])
        # print(dato[1])
        # for lista in contenido:
        #         lista = lista.replace(dato[0], dato[1])
        #         contenido.write(lista)
