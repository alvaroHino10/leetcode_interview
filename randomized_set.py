from random import choice

# No es del todo eficiente, ya que se podria hacer uso de un diccionario para almacenar los elementos y tener acceso
#  O(1) a los elementos, pero se opto por usar un conjunto para simplificar el codigo y no tener que hacer uso de un
#  diccionario
class RandomizedSet:
    """
        Implementa la estructura de datos RandomizedSet
    """

    def __init__(self):
        """
            RandomizedSet representado como un conjunto
        """
        self.__set = set()

    def insert(self, val: int) -> bool:
        """
            Inserta un elemento en el conjunto si no existe
        :param val: int: Elemento a insertar
        :return: bool: True si el elemento no existia en el conjunto, False en caso contrario
        """
        flag = True if val not in self.__set else False
        self.__set.add(val)
        return flag

    def remove(self, val: int) -> bool:
        """
            Elimina un elemento del conjunto si existe
        :param val: int: Elemento a eliminar
        :return: bool: True si el elemento existia en el conjunto, False en caso contrario
        """
        flag = True if val in self.__set else False
        self.__set.discard(val)
        return flag

    def getRandom(self) -> int:
        """
            Obtiene un elemento aleatorio del conjunto
        :return: int: Elemento aleatorio del conjunto
        """
        return choice(list(self.__set))

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

if __name__ == '__main__':
    rs = RandomizedSet()
    print(rs.insert(1))
    print(rs.remove(2))
    print(rs.insert(2))
    print(rs.getRandom())
    print(rs.remove(1))
    print(rs.insert(2))
    print(rs.getRandom())