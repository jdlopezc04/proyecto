si  __nombre__  ==  '__principal__' :
 cantidad Palabaras  =  0
 archivo  =  abrir ( 'palabras.txt' ) #abre el archivo
 print ( '>>> FILTRANDO PALABRAS DE 5 LETRAS' )
 con  abierto ( 'palabras.txt' , 'r' ) como  archivo : #lee el archivo
    for  linea  in  archivo :     #recorro el archivo linea por linea
        if  len ( linea ) ==  5 :   #condicional para verificar que la palabra se de tamaño 5 letras
            cantidadPalabaras  +=  1
 print ( '>>> OPERACION COMPLETADA CON SALIDA' )
 print ( '>>> SE ENCONTRARON '  +  str ( cantidadPalabaras ) +  ' PALABRAS DE 5 LETRAS' )  
