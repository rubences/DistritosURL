def leer_fichero(url):
    """
    Función que abre un fichero de texto desde una url y devuelve una lista de listas con los datos del fichero.
    Parámetros:
        url: URL del fichero de texto en formato csv donde cada registro aparece en una línea y los campos están separados por punto y coma `;`.
    Devuelve:
        Una lista cuyos elementos son a su vez listas que contienen los datos de cada línea del fichero menos la primera línea.
    """
    # Carga del módulo necesario para acceder a un fichero de internet.
    from urllib import request
    from urllib.error import URLError
    # Abrimos el fichero con la url dada.
    try:
        f = request.urlopen(url)
    except URLError: # Si se produce un error al acceder a la url informamos devolvemos una cadena informando de ello.
        return('¡La url ' + url + ' no existe!')
    # Leemos los datos del fichero en una cadena.
    datos = f.read()
    # Decodificamos los datos con la codificación latin1.
    datos = datos.decode('latin1')
    # Creamos una lista con las líneas del fichero dividiendo la cadena por el cambio de línea.
    datos = datos.split('\n')
    # Eliminamos la primera línea que no contiene información interesante.
    datos.pop(0)
    # Recorremos las líneas de la lista y para cada línea creamos una lista con los datos separando por el punto y coma. 
    # Devolvemos la lista de listas mediante comprensión de listas.
    datos_viviendas = [i.split(';') for i in datos]
    return datos_viviendas


def distritos(datos_viviendas):
    """
    Función recibe una lista de listas con los datos de la viviendas arrendadas y devuelve los distritos.
    Parámetros:
        datos_viviendas: Es una lista de listas como la que devuelve la función leer_fichero donde cada lista contienen los datos de viviendas arrendadas de un distrito. 
    Devuelve:
        Una lista con los distritos correspondientes a cada lista.
    """
    # Recorremos la lista de listas y para cada lista accedemos el primer elemento que contiene el nombre del distrito. 
    # Devolvemos la lista de distritos mediante comprensión de listas.
    distritos = [i[0] for i in datos_viviendas[1:]]
    return distritos


def filtrar_distritos(datos_viviendas, distritos):
    """
    Función que recibe una lista de listas con los datos de las viviendas arrendadas y una lista de nombres de distritos y devuelve una lista con las listas correspondientes a los distritos indicados
    Parámetros:
        datos_viviendas: Es una lista de listas como la que devuelve la función leer_fichero donde cada lista contienen los datos de viviendas arrendadas de un distrito. 
        distritos: Una lista de cadenas con nombres de distritos.
    Devuelve:
        Una lista con las listas que contienen los datos de las viviendas arrendadas de los distritos indicados.
    """
    # Recorremos la lista de listas y nos quedamos con las listas que cumplan que su primer elemento (el nombre del distrito) está en la lista de distritos. 
    # Devolvemos la lista de listas filtrada mediante comprensión de listas.
    datos_distritos = [i for i in datos_viviendas if i[0] in distritos]
    return datos_distritos


def viviendas_distritos(datos_viviendas):
    """
    Función que recibe una lista de listas con los datos de las viviendas arrendadas y devuelve un diccionario con los nombres de los distritos y el número total de viviendas arrendadas en el distrito.
    Parámetros:
        datos_viviendas: Es una lista de listas como la que devuelve la función leer_fichero donde cada lista contienen los datos de viviendas arrendadas de un distrito. 
    Devuelve:
        Un diccionario cuyas claves son los nombres de los distritos y cuyos valores son el número total de viviendas arrendadas en cada distrito.
    """
    # Recorremos la lista de listas y para cada lista accedemos el primer elemento que contiene el nombre del distrito y al segundo elemento que contiene el total de viviendas arrendadas.
    # Devolvemos el diccionario formado por los pares con clave el nombre del distrito y valor el total de viviendas arrendadas mediante comprensión de diccionarios.
    viviendas = {i[0]:i[1] for i in datos_viviendas}
    return viviendas



# Llamada a las funciones de prueba
datos = leer_fichero('https://datos.madrid.es/egob/catalogo/300117-0-arrendamiento-programas.csv')
print(distritos(datos))
datos_filtrados = filtrar_distritos(datos, ['CHAMBERI', 'HORTALEZA'])
print(viviendas_distritos(datos_filtrados))  #Devuelve un diccionario con el número total de viviendas arrendadas en Chamberí y Hortaleza.

def leer_fichero(url):
    """
    Función que abre un fichero de texto desde una url y devuelve una lista de listas con los datos del fichero.
    Parámetros:
        url: URL del fichero de texto en formato csv donde cada registro aparece en una línea y los campos están separados por punto y coma `;`.
    Devuelve:
        Una lista cuyos elementos son a su vez listas que contienen los datos de cada línea del fichero menos la primera línea.
    """
    # Carga del módulo necesario para acceder a un fichero de internet.
    from urllib import request
    from urllib.error import URLError
    # Abrimos el fichero con la url dada.
    try:
        f = request.urlopen(url)
    except URLError: # Si se produce un error al acceder a la url informamos devolvemos una cadena informando de ello.
        return('¡La url ' + url + ' no existe!')
    # Leemos los datos del fichero en una cadena.
    datos = f.read()
    # Decodificamos los datos con la codificación latin1.
    datos = datos.decode('latin1')
    # Creamos una lista con las líneas del fichero dividiendo la cadena por el cambio de línea.
    datos = datos.split('\n')
    # Eliminamos la primera línea que no contiene información interesante.
    datos.pop(0)
    # Creamos una lista vacía para ir añadiendo los datos de cada línea.
    datos_viviendas = []
    # Recorremos las listas de la lista
    for i in datos:
        # Para cada línea creamos una lista con los datos separando por el punto y coma y la añadimos a la lista principal.
        datos_viviendas.append(i.split(';'))
    return datos_viviendas


def distritos(datos_viviendas):
    """
    Función recibe una lista de listas con los datos de la viviendas arrendadas y devuelve los distritos.
    Parámetros:
        datos_viviendas: Es una lista de listas como la que devuelve la función leer_fichero donde cada lista contienen los datos de viviendas arrendadas de un distrito. 
    Devuelve:
        Una lista con los distritos correspondientes a cada lista.
    """
    # Creamos una lista vacía para ir añadiendo los distritos.
    distritos = []
    
    # Recorremos la lista de listas (empezando en el segundo elemento ya que el primero contiene los nombres de las columnas)
    for i in datos_viviendas[1:]: 
        # Para cada lista accedemos el primer elemento que contiene el nombre del distrito y lo añadimos a la lista de distritos.
        distritos.append(i[0])
    return distritos


def filtrar_distritos(datos_viviendas, distritos):
    """
    Función que recibe una lista de listas con los datos de las viviendas arrendadas y una lista de nombres de distritos y devuelve una lista con las listas correspondientes a los distritos indicados
    Parámetros:
        datos_viviendas: Es una lista de listas como la que devuelve la función leer_fichero donde cada lista contienen los datos de viviendas arrendadas de un distrito. 
        distritos: Una lista de cadenas con nombres de distritos.
    Devuelve:
        Una lista con las listas que contienen los datos de las viviendas arrendadas de los distritos indicados.
    """
    # Creamos una lista vacía para ir añadidiendo las listas fitradas.
    datos_distritos = []
    # Recorremos la lista de listas (empezando en el segundo elemento ya que el primero contiene los nombres de las columnas)
    for i in datos_viviendas[1:]:
        # Comprobamos si el primer elemento de que contiene el nombre del distrito está en la lista de distritos.
        if i[0] in distritos:
            # Si el distrito está en la lista añadimos la lista con los datos del distrito a la lista filtrada.
            datos_distritos.append(i)
    return datos_distritos


def viviendas_distritos(datos_viviendas):
    """
    Función que recibe una lista de listas con los datos de las viviendas arrendadas y devuelve un diccionario con los nombres de los distritos y el número total de viviendas arrendadas en el distrito.
    Parámetros:
        datos_viviendas: Es una lista de listas como la que devuelve la función leer_fichero donde cada lista contienen los datos de viviendas arrendadas de un distrito. 
    Devuelve:
        Un diccionario cuyas claves son los nombres de los distritos y cuyos valores son el número total de viviendas arrendadas en cada distrito.
    """
    # Creamos un diccionario vacío para añadir las viviendas arrendadas en cada distrito.
    viviendas = {}
    # Recorremos la lista de listas
    for i in datos_viviendas:
        # Para cada lista accedemos el primer elemento que contiene el nombre del distrito y al segundo elemento que contiene el total de viviendas arrendadas y añadimos el par al didcionario.
        viviendas[i[0]] = i[1]
    return viviendas


# Llamada a las funciones de prueba
datos = leer_fichero('https://datos.madrid.es/egob/catalogo/300117-0-arrendamiento-programas.csv')
print(distritos(datos))
datos_filtrados = filtrar_distritos(datos, ['CHAMBERI', 'HORTALEZA'])
print(viviendas_distritos(datos_filtrados))  #Devuelve un diccionario con el número total de viviendas arrendadas en Chamberí y Hortaleza.