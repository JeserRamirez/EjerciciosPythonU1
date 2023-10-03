"""
#0 CREAR UNA LISTA : 1, 2, 5, 3, 2, 3, 3, 6, 10, 8, 9
#1.CONVERTIR LA LISTA EN UN SET PARA ELIMINAR DUPLICADOS
#2. CALCULAR LA SUMA DE LOS NUMEROS USANDO UNA LISTA
#3.CALCULAR LA SUMA DE LOS NUMEROS USANDO UN SET
#4.CREAR UN DICCIONARIO PARA ALMACENAR LAS ESTADISTICAS
   NUMEROS UNICOS, SUMA TOTAL LISTA, SUMA TOTAL SET 
   MAXIMO VALOR, MINIMO VALOR
#5. IMPRIMIR LAS ESTADISTICAS"""
numeros = [1, 2, 2, 3, 4, 4]
numerosSet = set(numeros)
sumaLista = sum(numeros)
sumaSet = sum(numerosSet)
len(numerosSet)
valorMaximo = max(numeros)
valorMinimo = min(numeros)

miDiccionario = {
    'numeros_Unicos': numerosSet,
    'suma_total_lista': sumaLista,
    'suma_total_set': sumaSet,
    'valor_maximo': valorMaximo,
    'valor_minimo': valorMinimo
}

print(f"""
Numeros Unicos: {miDiccionario['numeros_Unicos']}
Suma total lista: {miDiccionario['suma_total_lista']}
Suma total set: {miDiccionario['suma_total_set']}
Valor maximo: {miDiccionario['valor_maximo']}
Valor minimo: {miDiccionario['valor_minimo']}""")
