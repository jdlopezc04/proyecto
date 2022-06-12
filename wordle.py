
import random
if __name__ == '__main__':
 cantidadPalabaras = 0
 intentos = 5
 archivo = open('palabras.txt') #abre el archivo
 diccionario = []
 with open('palabras.txt','r') as archivo: #lee el archivo
    for linea in archivo:    #recorro el archivo linea por linea
        if len(linea) == 6:  #condicional para verificar que la palabra se de tamaño 5 letras
            cantidadPalabaras += 1
            diccionario.append(linea.strip())
  
 
 palabraRandom = random.choice(diccionario)
 while intentos > 0: # loop que se ejecuta hasta que primerControl sea True
     palabra = input('>>> INTRODUCIR PALABRA DE 5 LETRAS: ') # variable de input
     errors = []
     if len(palabra) != 5: # verifica si la palabra no tiene 5 caracteres
        errors.append('NO ES DE 5 LETRAS')
     if palabra.isalpha() == False: # verifica si la palabra/String son letras
        errors.append('CONTIENE CARACTERES NO VALIDOS')
     if (palabra not in diccionario): # verifica si la palabra esta en el diccionario
        errors.append('NO ESTA EN EL DICCIONARIO')
     if len(errors) == 0: # si la lista de errores esta vacia ejecuta 2 operaciones
        palabraParaMostrar = ''
        for letra in range(5):
         if palabra[letra] == palabraRandom[letra]:
            palabraParaMostrar += '\x1b[6;30;42m' + palabra[letra] + '\x1b[0m' #color verde
         elif palabra[letra] in palabraRandom:
            palabraParaMostrar += '\x1b[6;30;43m' + palabra[letra] + '\x1b[0m' #color amarillo
         else:
            palabraParaMostrar += '\x1b[6;30;41m' + palabra[letra] + '\x1b[0m' #color rojo
        if palabra == palabraRandom:
           print('>>> GANASTE')
           print(palabraParaMostrar)
           intentos = 0
        else:
            print(palabraParaMostrar)    
            intentos -= 1
     else:
        print('>>> ERROR: La palabra introducida '+','.join(errors)+'. Por favor vuelva a ingresar una palabra')
