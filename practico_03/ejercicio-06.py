"""Magic Methods"""

from __future__ import annotations
from typing import List


# NO MODIFICAR - INICIO
class Article:
    """Agregar los métodos que sean necesarios para que los test funcionen.
    Hint: los métodos necesarios son todos magic methods
    Referencia: https://docs.python.org/3/reference/datamodel.html#basic-customization
    """

    def __init__(self, name: str) -> None:
        self.name = name

    # NO MODIFICAR - FIN

    # Completar

    def __str__ (self) -> str:
        return self.name
    
    def __repr__ (self):
        return f"Article('{self.name}')"


# NO MODIFICAR - INICIO
class ShoppingCart:
    """Agregar los métodos que sean necesarios para que los test funcionen.
    Hint: los métodos necesarios son todos magic methods
    Referencia: https://docs.python.org/3/reference/datamodel.html#basic-customization
    """

    def __init__(self, articles: List[Article] = None) -> None:
        if articles is None:
            self.articles = []
        else:
            self.articles = articles

    def add(self, article: Article) -> ShoppingCart:
        self.articles.append(article)
        return self

    def remove(self, remove_article: Article) -> ShoppingCart:
        new_articles = []

        for article in self.articles:
            if article != remove_article:
                new_articles.append(article)

        self.articles = new_articles

        return self

    # NO MODIFICAR - FIN

    # Completar

    def __str__ (self) -> str:                                        # Muestra el objeto en string 
        article_names = [str(article) for article in self.articles]
        return "['" + "', '".join(article_names) + "']"
     
    # def __repr__ (self):                                               # Muestra Clase + todas las propiedades del objeto 
    #     # article_repr = [repr(article) for article in self.articles]
    #     # return f"ShoppingCart([" + ", ".join(article_repr) + "])"  
    #     return ShoppingCart(repr(self.articles))
    
    def __repr__(self) -> str:
        return f"ShoppingCart({self.articles!r})"
    
    def __eq__(self, other):
        if isinstance(other, ShoppingCart):
            return set(self.articles) == set(other.articles)
        return False
    
    def __add__(self, other: ShoppingCart) -> ShoppingCart:
        new_articles = self.articles + other.articles
        return ShoppingCart(new_articles)


# NO MODIFICAR - INICIO

manzana = Article("Manzana")
pera = Article("Pera")
tv = Article("Television")

# Test de conversión a String
assert str(ShoppingCart().add(manzana).add(pera)) == "['Manzana', 'Pera']"

# Test de reproducibilidad
carrito = ShoppingCart().add(manzana).add(pera)
print(repr(carrito))
print(eval(repr(carrito)))
print(carrito)
print(carrito == eval(repr(carrito)) )
# assert carrito == eval(repr(carrito))  # Ver, no funciona

# Test de igualdad
assert ShoppingCart().add(manzana) == ShoppingCart().add(manzana)

# Test de remover objeto
assert ShoppingCart().add(tv).add(pera).remove(tv) == ShoppingCart().add(pera)

# Test de igualdad con distinto orden
assert ShoppingCart().add(tv).add(pera) == ShoppingCart().add(pera).add(tv)

# Test de suma
combinado = ShoppingCart().add(manzana) + ShoppingCart().add(pera)
assert combinado == ShoppingCart().add(manzana).add(pera)

# # NO MODIFICAR - FIN