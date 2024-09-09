texto = "este es el mundo en python" 

print("\n")
print("CANTIDAD DE PALABRAS")

palabra = texto.split()
print(f"Hemos encontrado {len(palabra)} palabras en tu texto")

print("\n")
print("LETRA DE INICIO Y DE FIN")

letra_inicio = texto[0]
letra_fin = texto[-1]

print(f"La letra inicial es {letra_inicio} y la letra final es {letra_fin}")

print("\n")
print("TEXTO IVERTIDO")
palabra.reverse()
texto_invertido = ' '.join(palabra)

print(f"si ordenamos tu texto al reves va a decir: {texto_invertido}")

print("\n")
print("BUSCANDO LA PALABRA PYTHON")
buscar_python = 'python' in texto 

dic = {True: "si", False: "no"}

print(f"La palabra python {dic[buscar_python]} se encuentra en el texto")