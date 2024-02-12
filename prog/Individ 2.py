#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    # Ввод списка с клавиатуры
    float_list = list(map(float, input("Введите вещественные числа через пробел: ").split()))

    # 1) Номер минимального элемента списка
    min_index = float_list.index(min(float_list))
    print(f"1) Номер минимального элемента списка: {min_index}")

    # 2) Сумма элементов между первым и вторым отрицательными элементами
    first_negative_index = -1
    second_negative_index = -1

    for i, num in enumerate(float_list):
        if num < 0:
            if first_negative_index == -1:
                first_negative_index = i
            else:
                second_negative_index = i
                break

    if first_negative_index != -1 and second_negative_index != -1:
        sum_between_negatives = sum(float_list[first_negative_index + 1:second_negative_index])
        print(f"2) Сумма элементов между первым и вторым отрицательными элементами: {sum_between_negatives}")
    else:
        print("2) В списке нет двух отрицательных элементов.")

    # Преобразование списка
    sorted_list = sorted(float_list, key=lambda x: (abs(x) > 1, x))
    print(f"Преобразованный список: {sorted_list}")

if __name__ == "__main__":
    main()