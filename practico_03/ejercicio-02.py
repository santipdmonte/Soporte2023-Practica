"""Variables y Métodos de Clase"""


class Articulo:
    """Clase con "nombre" como variable de instancia y un id incremental
    generado automáticamente.

    Restricciones:
        - Utilizar sólamente el constructor (__init__) y un método de
          clase (@classmethod) con una variable de clase
    """

    # Completar


    _last_id = 0  # Variable de clase para almacenar el ultimo id

    def __init__ (self, nombre=None):
        self.nombre = nombre
        self.id_ = self.generar_id()  # Asigna el id
    
    @classmethod
    def generar_id(cls):
        cls._last_id += 1   # Incrementa el ultimo id asignado
        return cls._last_id
        


# NO MODIFICAR - INICIO
art1 = Articulo("manzana")
art2 = Articulo("pera")
art3 = Articulo()
art3.nombre = "tv"

assert art1.nombre == "manzana"
assert art2.nombre == "pera"
assert art3.nombre == "tv"

assert art1.id_ == 1
assert art2.id_ == 2
assert art3.id_ == 3
assert Articulo._last_id == 3

# # NO MODIFICAR - FIN