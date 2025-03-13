from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
            Problema de distribución de caramelos a niños con calificaciones. Se distribuye en base a la calificacion de
            ambos vecinos (izquierda y derecha). Se busca minimizar el número de caramelos a distribuir.
            Esta solucion es de doble pasada, en la primera pasada se distribuyen los caramelos de izquierda a derecha y
            en la segunda pasada de derecha a izquierda. Tiene una complejidad de tiempo de O(n) y espacio de O(n).
        :param ratings: List[int]: Lista de calificaciones de los niños
        :return: int: Número total de caramelos a distribuir
        """
        candies = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)

    def candy2(self, ratings: List[int]) -> int:
        """
            Esta solucion es de una pasada, en la que se lleva un control de los picos y valles de las calificaciones.
            Se distribuyen los caramelos en base a los picos y valles, y se lleva un control de los incrementos y
            decrementos. Tiene una complejidad de tiempo de O(n) y espacio de O(1).
            Implementacion no propia, inspirada en el foro de discusiones de LeetCode.
        :param ratings: List[int]: Lista de calificaciones de los niños
        :return: int: Número total de caramelos a distribuir
        """
        n = len(ratings)
        if n == 1:
            return 1
        candies = 0
        up = down = peak = 0
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                up += 1
                peak = up
                down = 0
                candies += 1 + up
            elif ratings[i] < ratings[i - 1]:
                down += 1
                up = 0
                candies += 1 + down
                if down > peak:
                    candies += 1
            else:
                up = down = peak = 0
                candies += 1

        return candies + 1


if __name__ == "__main__":
    s = Solution()
    print(s.candy([1, 0, 2]))  # 5
    print(s.candy([1, 2, 2]))  # 4
    print(s.candy([60, 80, 100, 100, 100, 100, 100]))
    print(s.candy([1, 2, 87, 87, 87, 2, 1]))
    print(s.candy([100, 80, 70, 60, 70, 80, 90, 100, 90, 80, 70, 60, 60]))
    print(s.candy([6, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 1, 0]))
    print(s.candy(
        [20000, 20000, 16001, 16001, 16002, 16002, 16003, 16003, 16004, 16004, 16005, 16005, 16006, 16006, 16007, 16007,
         16008, 16008, 16009, 16009, 16010, 16010, 16011, 16011, 16012, 16012, 16013, 16013, 16014, 16014, 16015, 16015,
         16016, 16016, 16017, 16017, 16018, 16018, 16019, 16019, 16020, 16020, 16021, 16021, 16022, 16022, 16023, 16023,
         16024, 16024]))
