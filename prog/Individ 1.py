#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    # Ввод списка с клавиатуры
    A = list(map(float, input("Введите 10 чисел через пробел: ").split()))

    # Инициализация произведения отрицательных элементов
    product_of_negatives = 1

    # Находим произведение отрицательных элементов
    for num in A:
        if num < 0:
            product_of_negatives *= num

    # Вывод результата
    print(f"Произведение отрицательных элементов списка: {product_of_negatives}")

if __name__ == "__main__":
    main()
