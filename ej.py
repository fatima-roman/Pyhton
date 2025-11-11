print("\nEJ PARA VER \n")
print("1.  Cadenas de texto")
print("2.  Literales")
print("3.  Operadores aritméticos")
print("4.  Variables")
print("5.  Introducir datos (Input)")
print("6.  Operadores de comparación")
print("7.  Bucles")
print("8.  Cadenas")
print("9.  Listas y Tuplas")
print("10. Conversión de tipos")
print("11. Funciones")
print("12. Diccionarios")
print("13. Objetos y Clases")
print("14. Manejo de errores")
print("15. Archivos ----!!!!!! SE CREAN/ABREN ARCHIVOS !!!!!!!")
print("0.  Ver todos los temas")

opcion = input("\nElige una opción (0-15): ")

if opcion == "1" or opcion == "0":
    print("---------CADENAS DE TEXTO-----------")
    # /n = salto de linea 
    # argumetos: --- siempre deben ir al final de la línea
    #   - end = "*" salto de línea pero con el carácter entre comillas
    #   - sep = "--" lo que este separado con , se separa con el carácter entre comillas
    #   Existen los carácteres reservados, para poder escribirlos se debe usar una \ antes.
    #   En el caso de las "" podemos poner "" para definir la cadena de texto '' detro de esta.
    print("'Witsi' \"Witsi\"" "\nAraña subió a su telaraña.",  "Vino la lluvia y se la llevó.", sep="-", end="**" )
    print("Salió el sol, y se fue la lluvia.")

if opcion == "2" or opcion == "0":
    print("---------LITERALES---------")
    # LITERALES
    #   Enteros 
    #       Se puede escribir _ entre números muy grandes para aumentar la legibilidad. Ej = 1_000
    #   Octales y Hexadecimales 
    #       Octales: dígitos en el rango 0..7 Se representan con un 0o
    print("Octales: ", 0o123)
    #       Hexadecimales: se basa en número del 0..15 Se representa con 0x
    print("Hexadecimales: ", 0x123)
    #   Punto-flotantes
    #       Los punto-flotantes son carácteres que pueden contener una parte fraccionaria
    #       Se escriben como 2.5 o 0.4, al estar en décimal podemos omitir el 0. Ej: .4 o 4.
    print("Punto-flotantes: ", .4)
    #       E: la E se usa como exponente en base 10. En el ejemplo seria 2 * 10 elevado a 3 
    print("Uso del elevado a 10: ", 2E3)
    #   Booleanos 
    #       True (1) o False(0)
    #       Extiste el valor "none" indica la ausencia de valor .
    print("Booleanos: ", True>False)

if opcion == "3" or opcion == "0":
    print("----------OPERADORES ARITMÉTICOS----------")
    # OPERADORES
    #   + - * / // % **
    #       Exponenciación = **
    print("Exponenciación: ", 2**2)
    #       Multiplicación = * 
    print("Multiplicación: ", 1*2)
    #       División = /
    print("División: ", 2/2)
    #       División entera = //
    print("Divisón entera: ", 6//4)
    #       Residuo = %         En PseInt corresponde a el MOD
    print("Residuo: ", 6%4)
    #       Suma = +
    print("Suma: ", 1+2)
    #       Resta = - 
    print("Resta: ", 1-2)
    #   Los operadores siguen teniendo el mismo orden que en PseInt. Ej: primero va * a + 
    #   Si usamos el mismo operador exite la opción de que se haga de izq a der o de der a izq 

if opcion == "4" or opcion == "0":
    print("----------VARIABLES----------")
    # VARIABLES 
    #   Para declarar una variable 
    Ejemplo = 1 
    print(Ejemplo)
    #   No se pueden usar palabras reservadas como nombre de una variable, 
    #   como por ejemplo la palabra import, pero si sirve Import 
    #   Se pueden reasignar valores a las variables volviendo a asignar 
    Ejemplo = Ejemplo + 1 
    print(Ejemplo)

if opcion == "5" or opcion == "0":
    print("----------INTRODUCIR DATOS----------")
    # INPUT 
    #   El comando input sirve para que el usuario introduzca datos
    #   Correspondería al comando leer de PseInt 
    #   Dentro del mismo comando se puede poner un texto
    Ejemplo2 = input("Introduce un dato: ")
    print("Dato indroducido:", Ejemplo2)
    # INT Y FLOAT 
    #   El comando int trata de convertir un número a entero, en caso de no poder nos devuelve error
    #   El comando float trata de convertir un número a flotante (real)
    Ejemplo2 = float(input("Ingresa un número: "))
    Ejemplo = Ejemplo2 ** 2.0
    print(Ejemplo2, "a la potencia de 2 es", Ejemplo)

if opcion == "6" or opcion == "0":
    print("----------OPERADORES DE COMPARACIÓN----------")
    # OPERADORES
    #   == 
    #      es un igual estricto, 1 = '1' es vederdadero pero 1=='1' es falso s
    print("==: ", 1=='1')
    #   != 
    #      es un no es igual, es decir si pones 1 != 1 dará false
    #      ya que estas diciendo ¿1 es distino a 1?. Si pones 1!=2 dará true porque son distintos
    print("!=: ", 1!=1)
    #   < > <= >= 
    #       estos operadores son iguales a los ya dados en PseInt 
    print("< > <= >=: ", "1 >= 2: ", 1>=2, ", 1 <= 2: ", 1<=2)

if opcion == "7" or opcion == "0":
    print("----------BUCLES----------")
    # BUCLES
    #   IF: 
    #       esto corresponde a la función si en PseInt. El ejemplo coje los datos almacenados en las variables anteriores
    #       Todas las formas de esta función ya las dimos en PseInt. 
    print("--IF--")
    Ejemplo = 10
    Ejemplo2 = 5
    if Ejemplo > Ejemplo2: 
        print("El primer valor es mayor al segundo")
    else: 
        if Ejemplo2 > Ejemplo:
            print("El primer valor es menor al segundo")
        else: 
            print("Son iguales")
    #       En este caso se podría sustituir el else if por elif, que es exactamente lo mismo pero más corto.
    if Ejemplo > Ejemplo2: 
        print("El primer valor es mayor al segundo")
    elif Ejemplo2 > Ejemplo:
        print("El primer valor es menor al segundo")
    else: 
        print("Son iguales")
    # 
    print("-"*10+"WHILE--"+"-"*10)
    #   WHILE: 
    #       esto corresponde a la función mientras en PseInt. 
    #       Mientras lo que sea se cumpla haz esto. 
    cont = 0
    while cont != 2 : 
        cont = cont + 1 
        print ("Esto se ha repetido ", cont, " veces")
    #
    print("--FOR--")
    #   FOR: 
    #       esto corresponde a la función para en PseInt
    #       la estructura es: for variables in secuencia
    #       - Range(): puedes poner solo un valor que sería igual a 'Con Paso' en PseInt 
    #                  o puedes utilizar su estructura: inicio, fin, paso
    for i in range(2, 10, 2):  # Empieza en 2, hasta 10, de 2 en 2
        print(i)
    #       - Else: se puede usar en for y se ejecuta cuando termina el bucle
    #       - break: Sale del bucle, independientemente de si ha terminado de iterar sobre todos los elementos.
    #       - continue: Salta a la siguiente iteración del bucle sin ejecutar el resto del código dentro del bucle.
    #       - enumerate(): Te permite acceder tanto a los valores como a los índices de una secuencia.
    frutas = ["manzana", "plátano", "cereza", "pera", "uva"]
    for i, fruta in enumerate(frutas):
        if fruta == "pera":
            continue  # Salta "pera" 
        if fruta == "cereza":
            break  # Detiene el bucle al encontrar "cereza"
        print(f"Índice {i}: {fruta}")
    else:
        print("Ejemplo de for terminó sin interrupciones.")

if opcion == "8" or opcion == "0":
    print("----------CADENAS (MÉTODOS)----------")
    # CADENAS
    #   Dentro de la cadena no puedes cambiar valores, para ello 
    #   debes poner, por ejemplo, cadena = cadena.upper()
    #   Cadenas con comillas dobles ""
    print("Es un día 'genial'")
    #   Cadenas con comillas simples ''
    print('Dijo "Hola" y se fue.')
    #   Cadenas con comillas triples
    cad4 = """Hola,
que tal?"""
    #   OPERADORES 
    #       Concatenación (+) : para añadir algún valor a la cadena 
    #       Repetición (*): para repetir el valor en cadena
    #       Indexación: sirve para acceder a caracteres individuales
    #       Longitud (len): el número de caracteres de la cadena
    #       Recorrido: puedes recorer la cadena con un bucle for
    #       OPERADORES DE PERTENENCIA
    #           In: comprueba si esta el valor pedido en la cadena 
    #           Not in: comprueba si no esta el valor pedido en la cadena
    cadena = "Python"
    print("Concatenación: ", cadena + " es genial")  # Python es genial
    print("Repetición: ", cadena * 2)  # PythonPython
    print("Longitud: ",len(cadena))  # 6
    print("Indexación: ", cadena[0], cadena[-1])  # P n
    for c in cadena:
        print("Recorrido: ",c, end=" ")  # P y t h o n
    print("\nOperadores de pertenencia: ","P" in cadena, "z" not in cadena)  # True True

if opcion == "9" or opcion == "0":
    print("-------------LISTAS Y TUPLAS-------------------")
    #LISTAS Y TUPLAS
    #   LISTAS
    #       Listas en Python (Tipo de dato secuencia)
    #       Son mutables, lo que significa que podemos modificar sus elementos.
    #       Definiendo una lista
    lista = [1, 2, 3, 4, 5, 6]
    #       Recorrer una lista con un bucle for
    for num in lista:
        print(num, end=" ")  # Salida: 1 2 3 4 5 6
    print()
    #       Concatenación de listas
    lista2 = lista + [7, 8, 9]
    print(lista2)  # Salida: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #       Repetición de listas
    lista_repetida = lista * 2
    print(lista_repetida)  # Salida: [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
    #       Indexación y slicing
    print(lista[2])  # Salida: 3
    print(lista[1:4])  # Salida: [2, 3, 4]
    print(lista[::-1])  # Salida: [6, 5, 4, 3, 2, 1]
    #       Métodos principales de listas
    lista.append(7)  # Agregar un elemento al final
    lista.insert(1, 100)  # Insertar 100 en la posición 1
    print(lista)  # Salida: [1, 100, 2, 3, 4, 5, 6, 7]
    #       Eliminar elementos
    lista.pop()  # Elimina el último elemento
    lista.remove(100)  # Elimina el primer 100 encontrado
    print(lista)  # Salida: [1, 2, 3, 4, 5, 6]
    #       Ordenar lista
    lista.sort()
    print(lista)  # Salida: [1, 2, 3, 4, 5, 6]
    lista.sort(reverse=True)
    print(lista)  # Salida: [6, 5, 4, 3, 2, 1]
    #
    #
    #   TUPLAS
    #       Tuplas en Python (son inmutables)
    tupla = (1, 2, 3, 4, 5)
    print(tupla[1])  # Salida: 2
    #       Intentar modificar una tupla genera error
    #       tupla[1] = 10  # Esto genera TypeError
    #        Métodos de búsqueda en tuplas
    print(tupla.count(2))  # Salida: 1 (cuántas veces aparece el 2)
    print(tupla.index(3))  # Salida: 2 (posición de la primera aparición de 3)

if opcion == "10" or opcion == "0":
    print("----------CONVERSIÓN DE TIPOS----------")
    # CONVERSIÓN DE TIPOS
    #   INT()
    #       sirve para volver entero un número o un texto
    #       si el número tiene decimales los borra
    numero_texto = "123"
    numero = int(numero_texto)
    print("int(): ", numero)
    print("float a int: ", int(3.9))  # pone 3, borra el .9
    #
    #   FLOAT()
    #       sirve para volver decimal un número o un texto
    texto = "45.67"
    decimal = float(texto)
    print("float(): ", decimal)
    #
    #   STR()
    #       sirve para volver texto cualquier cosa
    edad = 20
    mensaje = "Tengo " + str(edad) + " años"
    print("str(): ", mensaje)
    #
    #   BOOL()
    #       sirve para volver True o False algo
    #       el 0, las comillas vacías "", las listas vacías [] y los diccionarios vacíos {} son False
    #       todo lo demás es True
    print("bool(): ", bool(0), bool(1), bool(""))
    #
    #   LIST()
    #       sirve para volver lista algo
    tupla_ejemplo = (1, 2, 3)
    lista_desde_tupla = list(tupla_ejemplo)
    print("list(): ", lista_desde_tupla)
    #
    #   TUPLE()
    #       sirve para volver tupla algo
    lista_ejemplo = [4, 5, 6]
    tupla_desde_lista = tuple(lista_ejemplo)
    print("tuple(): ", tupla_desde_lista)

if opcion == "11" or opcion == "0":
    print("----------FUNCIONES----------")
    # FUNCIONES
    #   son como mini programas que haces para reutilizar código
    #   se pone def, luego el nombre, luego () y luego :
    def saludar():
        print("Hola desde una función")
    #   para usarla la llamas poniendo su nombre con ()
    saludar()
    #
    #   CON PARÁMETROS
    #       los parámetros son variables que le pasas a la función
    #       van dentro de los ()
    def suma(a, b):
        resultado = a + b
        print("La suma es:", resultado)
    suma(5, 3)
    #
    #   RETURN
    #       sirve para que la función te devuelva un valor
    #       cuando pones return la función se termina
    def multiplicar(x, y):
        return x * y
    resultado = multiplicar(4, 7)
    print("Resultado con return:", resultado)
    #
    #   PARÁMETROS POR DEFECTO
    #       puedes poner valores que se usan si no pasas nada
    def potencia(base, exponente=2):
        return base ** exponente
    print("Con exponente por defecto:", potencia(5))  # usa 2
    print("Con exponente específico:", potencia(5, 3))  # usa 3
    #
    #   ARGUMENTOS VARIABLES
    #       *args sirve para pasar todos los valores que quieras
    def sumar_varios(*numeros):
        total = 0
        for num in numeros:
            total += num
        return total
    print("Suma variable:", sumar_varios(1, 2, 3, 4, 5))

if opcion == "12" or opcion == "0":
    print("----------DICCIONARIOS----------")
    # DICCIONARIOS
    #   son como listas pero en vez de números usas palabras para buscar
    #   se pone entre {} y separas con clave: valor
    persona = {
        "nombre": "Juan",
        "edad": 25,
        "ciudad": "Madrid"
    }
    #
    #   VER VALORES
    #       se pone el nombre del diccionario y entre [] la clave
    print("Nombre:", persona["nombre"])
    print("Edad:", persona["edad"])
    #
    #   AGREGAR O CAMBIAR
    #       para agregar o cambiar pones = a una clave
    persona["profesion"] = "Programador"  # agregarias un campo nuevo 
    persona["edad"] = 26  # cambiarias un campo existente 
    print(persona)
    #
    #   COMANDOS ÚTILES
    #       keys() te da todas las claves
    print("Claves:", persona.keys())
    #       values() te da todos los valores
    print("Valores:", persona.values())
    #       items() te da todo junto = A TODO 
    print("Items:", persona.items())
    #       get() busca un valor, si no existe pone None 
    print("Get:", persona.get("nombre"))
    print("Get no get:", persona.get("apellido"))
    #
    #   RECORRER
    #       se puede recorrer con for
    for clave, valor in persona.items():
        print(f"{clave}: {valor}")

if opcion == "13" or opcion == "0":
    print("----------OBJETOS Y CLASES----------")
    # OBJETOS Y CLASES
    #   las clases son como moldes para crear cosas
    #   se pone class y luego el nombre
    #
    #   HACER UNA CLASE
    class Perro:
        #   __init__ es lo que pasa cuando creas el objeto
        #   self es para que el objeto se refiera a sí mismo
        def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad
        #
        #   FUNCIONES DENTRO DE LA CLASE
        #       se llaman métodos
        def ladrar(self):
            print(f"{self.nombre} dice: Guau!")
        #
        def cumpleanos(self):
            self.edad += 1
            print(f"{self.nombre} ahora tiene {self.edad} años")
    #
    #   CREAR OBJETOS
    #       se pone el nombre de la clase con () como si fuera una función
    mi_perro = Perro("Max", 3)
    otro_perro = Perro("Luna", 5)
    #
    #   USAR LOS MÉTODOS
    print("Nombre:", mi_perro.nombre)
    print("Edad:", mi_perro.edad)
    mi_perro.ladrar()
    mi_perro.cumpleanios()
    #
    #   HERENCIA
    #       una clase puede copiar cosas de otra clase
    #       se pone el nombre de la clase padre entre ()
    class PerroPolicia(Perro):
        def __init__(self, nombre, edad, placa):
            super().__init__(nombre, edad)  # copia del padre
            self.placa = placa
        #
        def patrullar(self):
            print(f"{self.nombre} con placa {self.placa} está patrullando")
    #
    policia = PerroPolicia("Rex", 4, "K9-001")
    policia.ladrar()  # esto lo heredó de Perro
    policia.patrullar()  # esto es nuevo

if opcion == "14" or opcion == "0":
    print("-"*10+"MANEJO DE ERRORES----------")
    # MANEJO DE ERRORES
    #   TRY-EXCEPT
    #       sirve para que si hay un error el programa no se rompa
    #       pones try: y luego el código que puede fallar
    #       pones except: y luego qué hacer si falla
    try:
        numero = int(input("Ingresa un número: "))
        resultado = 10 / numero
        print("Resultado:", resultado)
    except ValueError:
        print("Error: Debes ingresar un número válido")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero")
    #
    #   EXCEPT SIN ESPECIFICAR
    #       atrapa cualquier error
    try:
        valor = "texto" + 5
    except:
        print("Ocurrió un error")
    #
    #   ELSE
    #       se ejecuta si todo salió bien
    try:
        num = int("10")
    except ValueError:
        print("Error de conversión")
    else:
        print("Conversión exitosa:", num)
    #
    #   FINALLY
    #       se ejecuta siempre, pase lo que pase
    try:
        archivo = "Ejemplo"
    except:
        print("Error")
    finally:
        print("Esto siempre se ejecuta")

if opcion == "15" or opcion == "0":
    uwu= input("SEGUGOR DE EJECUTAR \"ARCHIVOS\": (Y = SI Y TIENE QUE SER EN MAYUS)")
    if uwu == "Y":
        print("----------ARCHIVOS----------")
        # ARCHIVOS
        #   ABRIR ARCHIVO
        #       open() sirve para abrir archivos
        #       "r" es para leer, "w" es para escribir, "a" es para añadir
        #
        #   ESCRIBIR
        #       "w" borra todo y escribe de nuevo
        #       "a" añade al final sin borrar
        archivo = open("ejemplo.txt", "w")
        archivo.write("Hola, este es un archivo de prueba\n")
        archivo.write("Segunda línea\n")
        archivo.close()  # siempre hay que cerrar
        print("Archivo creado y escrito")
        #
        #   LEER
        #       "r" es para leer
        archivo = open("ejemplo.txt", "r")
        contenido = archivo.read()  # lee todo
        print("Contenido del archivo:")
        print(contenido)
        archivo.close()
        #
        #   LEER LÍNEA POR LÍNEA
        #       se puede usar un for
        archivo = open("ejemplo.txt", "r")
        for linea in archivo:
            print("Línea:", linea.strip())  # strip() quita el salto de línea
        archivo.close()
        #
        #   WITH
        #       es mejor usar with porque cierra solo el archivo
        with open("ejemplo.txt", "r") as archivo:
            contenido = archivo.read()
            print("Usando with:", contenido)
        #   cuando termina el with el archivo se cierra solo

print("="*50)
print("FIN DE LOS APUNTES")
print("="*50)