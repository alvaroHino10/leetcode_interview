from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
            Dada una lista de gas y cost, se debe retornar el indice donde se puede completar el circuito. Si no se
            puede completar el circuito, se debe retornar -1. Se puede intuir que si la suma de gas es menor que
            la suma de cost, no se puede completar el circuito.
            Es un ejercicio igual que resolvi en HackerRank.
        :param gas: List[int]: Lista de gas
        :param cost: List[int]: Lista de cost
        :return: int: Indice donde se puede completar el circuito
        """
        # Si el balance de la suma de gas y cost es menor a 0, no se puede completar el circuito desde ese indice y se
        # recorre al siguiente indice, reiniciando el total de gas y distancia.
        # Se garantiza el recorrido si la suma de gas es mayor o igual a la suma de cost. Si no se cumple, se retorna -1
        # directamente sin recorrer la lista.
        n = len(gas)
        index_i = 0
        total_gas = 0
        total_distance = 0
        if sum(gas) < sum(cost):
            return -1
        for i in range(n):
            actual_gas = gas[i]
            actual_distance = cost[i]
            total_gas += actual_gas
            total_distance += actual_distance
            if total_gas - total_distance < 0:
                total_gas = 0
                total_distance = 0
                index_i = i + 1
        return index_i

if __name__ == '__main__':
    s = Solution()
    print(s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))  # 3
    print(s.canCompleteCircuit([2, 3, 4], [3, 4, 3]))  # -1
    print(s.canCompleteCircuit([1, 1, 3], [2, 2, 1]))  # 2