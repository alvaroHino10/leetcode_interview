class Solution:
    def romanToInt(self, s: str) -> int:
        """
            Se convierte un número romano a un número entero. donde el número romano estará en el rango de 1 a 3999.
        :param s: str: Número romano a convertir a número entero.
        :return: int: Número entero.
        """
        # Se crea un diccionario con los números romanos y su equivalente en número entero. Se construyen los números
        # recorriendo de derecha a izquierda y se verifica si el número actual es menor al anterior, si es así se resta,
        # de lo contrario se suma.
        symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev = 0
        for c in reversed(s):
            if symbols[c] < prev:
                result -= symbols[c]
            else:
                result += symbols[c]
            prev = symbols[c]
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('III'))  # 3
    print(s.romanToInt('IV'))   # 4
    print(s.romanToInt('IX'))   # 9
    print(s.romanToInt('LVIII'))  # 58
    print(s.romanToInt('MCMXCIV'))  # 1994