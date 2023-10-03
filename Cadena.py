# DEL LA SIGUIENTE VARIABLE TEXTO =
"""
'SON LAS 7 DE LA NOCHE Y YA ME QUIERO IR'
SI ENCUENTRA EL NUMERO 7 Y ES MENOR A 8
IMPRIMIR EL NUMERO 7 CONVERTIDO A INT 
Y EL TEXTO, ' ES HORA DE IRNOS SON LAS : '7'
"""
texto = "Son las 7 de la noche"

for letra in texto:
    if letra == "7":
        numero = int(letra)

if numero < 8:
    print("Es hora de irnos, son las 7")