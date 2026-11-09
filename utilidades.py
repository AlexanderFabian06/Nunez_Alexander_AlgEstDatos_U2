"""
utilidades.py
Funciones auxiliares del sistema de biblioteca (Unidad 2: diccionarios y conjuntos).
 
Estructuras usadas (todas nativas de Python):
  - dict  -> HashMap: catalogo {codigo: {"titulo": ..., "autor": ...}}
  - set   -> socios registrados y socios con préstamos por género
"""

def registrar_libro(catalogo: dict, codigo: str, titulo: str, autor: str) -> bool:
    """Registra un libro. Devuelve False si el código ya existía (no sobrescribe)."""
    codigo = codigo.strip().upper()
    # 'in' sobre un dict usa la función hash de la clave: O(1) promedio
    if codigo in catalogo:
        return False
    catalogo[codigo] = {"titulo": titulo.strip(), "autor": autor.strip()}  # put: O(1) promedio
    return True
 
 
def buscar_libro(catalogo: dict, codigo: str):
    """Busca un libro por código. Devuelve su info o None si no existe."""
    # get: O(1) promedio (hash del código -> bucket -> valor)
    return catalogo.get(codigo.strip().upper())
 

def catalogo_ordenado(catalogo: dict) -> list:
    """
    Devuelve [(codigo, info), ...] ordenado por código.
    sorted(): O(n log n) porque un dict (HashMap) NO guarda orden.
    Alternativa: sortedcontainers.SortedDict mantiene las claves ordenadas
    en cada inserción (O(log n)) y recorrerlas ya ordenadas cuesta O(n).
    """
    return sorted(catalogo.items(), key=lambda par: par[0])
 

def registrar_socio(socios: set, id_socio: str) -> bool:
    """Registra un socio. Devuelve False si ya estaba (el set evita duplicados)."""
    id_socio = id_socio.strip().upper()
    if id_socio in socios:      # pertenencia: O(1) promedio
        return False
    socios.add(id_socio)        # add: O(1) promedio
    return True
 
 
def socio_registrado(socios: set, id_socio: str) -> bool:
    """Verifica al instante si un identificador ya está registrado."""
    return id_socio.strip().upper() in socios  # O(1) promedio
 

def registrar_prestamo(socios: set, prestamos: set, id_socio: str) -> bool:
    """Marca que un socio (ya registrado) tiene préstamo en un género."""
    id_socio = id_socio.strip().upper()
    if id_socio not in socios:  # O(1) promedio
        return False
    prestamos.add(id_socio)     # O(1) promedio
    return True
 
 
def analizar_prestamos(novela: set, ciencia: set) -> dict:
    """Operaciones de conjuntos sobre los socios con préstamos."""
    return {
        "ambos": novela & ciencia,    # intersección: O(min(n, m))
        "solo_novela": novela - ciencia,  # diferencia: O(n)
        "total": novela | ciencia,    # unión: O(n + m)
    }
 

def cargar_datos_ejemplo(catalogo: dict, socios: set, novela: set, ciencia: set) -> None:
    libros = [
        ("L003", "Cien años de soledad", "Gabriel García Márquez"),
        ("L001", "Don Quijote de la Mancha", "Miguel de Cervantes"),
        ("L005", "Cosmos", "Carl Sagan"),
        ("L002", "Breve historia del tiempo", "Stephen Hawking"),
        ("L004", "El principito", "Antoine de Saint-Exupéry"),
    ]
    for codigo, titulo, autor in libros:
        registrar_libro(catalogo, codigo, titulo, autor)
 
    for id_socio in ["S01", "S02", "S03", "S04", "S05", "S02"]:  # S02 repetido a propósito
        registrar_socio(socios, id_socio)
 
    for id_socio in ["S01", "S02", "S03"]:
        registrar_prestamo(socios, novela, id_socio)
    for id_socio in ["S02", "S04"]:
        registrar_prestamo(socios, ciencia, id_socio)