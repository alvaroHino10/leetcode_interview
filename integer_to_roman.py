class Solution:
    def intToRoman(self, num: int) -> str:
        """
            Se convertirá un número entero a un número romano. donde el numero entero estará en el rango de 1 a 3999.
        :param num: int: Número entero a convertir a número romano.
        :return: str: Número romano.
        """
        # Se crea un diccionario con los números romanos y su equivalente en número entero. Se construyen los números
        # en base a los casos especiales que tienen los numeros romanos. Un enfoque greedy con los casos especiales en
        # el diccionario es igual de valido y efiiciente.
        nums_to_roman = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        result = []
        div = 1
        while num > 0:
            digit = num % 10
            num //= 10
            if digit == 9:
                result.insert(0, nums_to_roman[div * 10])
                result.insert(0, nums_to_roman[div])
            elif digit == 4:
                result.insert(0, nums_to_roman[div * 5])
                result.insert(0, nums_to_roman[div])
            elif digit >= 5:
                for _ in range(digit - 5):
                    result.insert(0, nums_to_roman[div])
                result.insert(0, nums_to_roman[div * 5])
            else:
                for _ in range(digit):
                    result.insert(0, nums_to_roman[div])
            div *= 10
        return ''.join(result)

if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(3))  # III
    print(s.intToRoman(4))  # IV
    print(s.intToRoman(9))  # IX
    print(s.intToRoman(58))  # LVIII
    print(s.intToRoman(1994))  # MCMXCIV
