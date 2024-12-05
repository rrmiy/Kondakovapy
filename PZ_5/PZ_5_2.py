#Описать функцию ShiftLeft3(A, B, C), выполняющую левый циклический сдвиг:
#значение A переходит в C, значение C — в B, значение B — в A (A, B, C —
#вещественные параметры, являющиеся одновременно входными и выходными). С
#помощью этой функции выполнить левый циклический сдвиг для двух данных
#наборов из трех чисел: (A1, B1, C1) и (A2, B2, C2).

def ShiftLeft3(A, B, C):
  return C, A, B #циклический сдвиг влево

#заданный наборы чисел:
A1, B1, C1 = 1.0, 2.0, 3.0
A2, B2, C2 = 4.0, 5.0, 6.0

#до сдвига
print('До сдвига 1:', A1, B1, C1)
print('До сдвига 2:', A2, B2, C2)

#сдвиг для первого набора:
A1, B1, C1 = ShiftLeft3(A1, B1, C1)
print(f"После сдвига 1: A1={A1}, B1={B1}, C1={C1}")

#сдвиг для второго набора:
A2, B2, C2 = ShiftLeft3(A2, B2, C2)
print(f"После сдвига 2: A2={A2}, B2={B2}, C2={C2}")