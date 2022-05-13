si  __nombre__  ==  '__principal__' :
 cantidad Palabaras  =  0
 archivo  =  abrir ( 'palabras.txt' ) #abre el archivo
 print ( '>>> FILTRANDO PALABRAS DE 5 LETRAS' )
 diccionario  = []
 con  abierto ( 'palabras.txt' , 'r' ) como  archivo : #lee el archivo
    for  linea  in  archivo :     #recorro el archivo linea por linea
        if  len ( linea ) ==  6 :   #condicional para verificar que la palabra se de tamaño 5 letras
            cantidadPalabaras  +=  1
            diccionario _ agregar ( linea . tira ())
 print ( '>>> OPERACION COMPLETADA CON SALIDA' )
 print ( '>>> SE ENCONTRARON '  +  str ( cantidadPalabaras ) +  ' PALABRAS DE 5 LETRAS' )  
 imprimir ( diccionario )
 palabraCorrecta = False # variable para repetir el loop/while
 while not(palabraCorrecta): # loop que se ejecuta hasta que palabraCorrecta sea True
     print('>>> INTRODUCIR PALABRA DE 5 LETRAS')
     palabra = input() # variable de input
     errors = []
     if len(palabra) is not 5: # verifica si la palabra no tiene 5 caracteres
        errors.append('NO ES DE 5 LETRAS')
     if palabra.isalpha() == False: # verifica si la palabra/String son letras
        errors.append('CONTIENE CARACTERES NO VALIDOS')
     if (palabra not in diccionario): # verifica si la palabra esta en el diccionario
        errors.append('NO ESTA EN EL DICCIONARIO')
     if len(errors) is 0: # si la lista de errores esta vacia ejecuta 2 operaciones
        print('>>> OPERACION COMPLETADA CON EXITO')
        palabraCorrecta = True # termina el loop/while
     else:
        print('>>> ERROR: La palabra introducida '+','.join(errors)+'. Por favor vuelva a ingresar una palabra')
