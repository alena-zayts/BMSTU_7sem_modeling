from prettytable import PrettyTable
from itertools import islice
from RandomClass import Random
from collections import defaultdict
from math import sqrt

N_RANDOMS = 100000
eps = 1e-6


def random_from_table():
    with open('random_ints.txt') as file:
        lines = file.readlines()

    # numbers = set()
    # for line in lines:
    #     numbers.update(set(list(map(int, line.strip().split()))))
    # print(numbers)
    # numbers = list(numbers)[:N_RANDOMS]
    numbers = list()
    for line in lines:
        numbers.extend(list(map(int, line.strip().split())))
    numbers = numbers[:N_RANDOMS]

    one = [number % 10 for number in numbers]
    two = [10 + number % 90 for number in numbers]
    three = [100 + number % 900 for number in numbers]

    return one, two, three


def random_from_alg():
    random = Random(2)
    one = [random.randint(0, 10) for _ in range(N_RANDOMS)]
    two = [random.randint(10, 100) for _ in range(N_RANDOMS)]
    three = [random.randint(100, 1000) for _ in range(N_RANDOMS)]
    return one, two, three


# def calc_hi(arr, start, end):
#     n = len(arr)
#     tab = [0 for i in range(start + end)]
#     for i in range(n):
#         tab[arr[i]] += 1
#     s = 0
#     for i in tab:
#         s += i * i
#     return s * (end - start) / n - n


def calc_hi2(random_numbers, start_random, end_random):
    min_dif = start_random - end_random + 1
    max_dif = end_random - start_random - 1

    possible_differences = list(range(min_dif, max_dif + 1))
    probabilities_of_differences = {
        difference: (end_random - start_random - abs(difference)) / ((end_random - start_random) ** 2)
        for difference in possible_differences
    }

    n_differences = len(random_numbers) - 1
    differences = [random_numbers[i + 1] - random_numbers[i] for i in range(n_differences)]
    differences_counts = {difference: differences.count(difference) for difference in possible_differences}

    if sum(differences_counts.values()) != len(differences) or \
            abs(sum(probabilities_of_differences.values()) - 1) > eps:
        print(sum(differences_counts.values()))
        print(sum(probabilities_of_differences.values()))
        raise ValueError

    V = 0
    for difference in differences_counts.keys():
        V += (differences_counts[difference] ** 2) / probabilities_of_differences[difference]
    V = (V / n_differences) - n_differences
    return V


def calc_hi(random_numbers, start_random, end_random):
    min_dif = start_random - end_random + 1
    max_dif = end_random - start_random - 1

    possible_differences = list(range(min_dif, max_dif + 1))
    probabilities_of_differences = {
        difference: (end_random - start_random - abs(difference)) / ((end_random - start_random) ** 2)
        for difference in possible_differences
    }

    n_differences = len(random_numbers) // 2
    differences = [random_numbers[2 * i + 1] - random_numbers[2 * i] for i in range(n_differences)]
    differences_counts = {difference: differences.count(difference) for difference in possible_differences}

    if sum(differences_counts.values()) != len(differences) or \
            abs(sum(probabilities_of_differences.values()) - 1) > eps:
        print(sum(differences_counts.values()))
        print(sum(probabilities_of_differences.values()))
        raise ValueError

    V = 0
    for difference in differences_counts.keys():
        V += (differences_counts[difference] ** 2) / probabilities_of_differences[difference]
    V = (V / n_differences) - n_differences
    return V

def hi2_quantiles_for_v(v, ps=(1, 5, 10, 90, 95, 99)):
    return {xp: v + (sqrt(2 * v) * xp) + (2 * (xp ** 2) / 3) - (2 / 3) for xp in ps}

# hi2_quantiles = {
#     # 1 цифра -> возможные числа [0; 9] -> возможно 19 разниц [-9; 9]
#     1: {0.1: 5.407, 1: 7.663, 5: 10.117, 10: 11.65, 90: 27.2, 95: 30.144, 99: 27.204, 99.9: 43.8},
#     # 2 цифры ->возможные числа [10; 99] -> возможно 179 разниц [-89; 89]
#     2: hi2_quantiles_for_v(179),
#     # 3 цифры ->возможные числа [100; 999] -> возможно 1799 разниц [-899; 899]
#     3: hi2_quantiles_for_v(1799),
# }

hi2_quantiles = {
    # 1 цифра -> возможные числа [0; 9] -> возможно 19 разниц [-9; 9] (10 чисел)
    1: {1: 2.558, 5: 3.94, 10: 4.865, 90: 15.99, 95: 18.31, 99: 23.21},
    # 2 цифры ->возможные числа [10; 99] -> возможно 179 разниц [-89; 89] (90 чисел)
    2: hi2_quantiles_for_v(90), #{1: 61.75, 5: 68.13, 10: 73.29, 90: 107.6, 95: 113.1, 99: 124.1},
    # 3 цифры ->возможные числа [100; 999] -> возможно 1799 разниц [-899; 899] (900 чисел)
    3: hi2_quantiles_for_v(900),
}

for row in hi2_quantiles.items():
    print(row)


def check_with_criterion(counted_coef, digits_amount):
    # if counted_coef < hi2_quantiles[digits_amount][0.1] or counted_coef > hi2_quantiles[digits_amount][99.9]:
    #     return "Числа не случайные"
    # elif hi2_quantiles[digits_amount][1] < counted_coef < hi2_quantiles[digits_amount][99]:
    #     return "Числа случайные"
    # else:
    #     return "Числа подозрительные"
    if counted_coef < hi2_quantiles[digits_amount][1] or counted_coef > hi2_quantiles[digits_amount][99]:
        return "Числа не случайные"
    elif hi2_quantiles[digits_amount][5] < counted_coef < hi2_quantiles[digits_amount][95]:
        return "Числа случайные"
    else:
        return "Числа подозрительные"


def main():
    n_output = 10
    indexes = [i for i in range(n_output)]
    table_tbl = PrettyTable()
    for alg, alg_name in [[random_from_table, 'Табличный метод'], [random_from_alg, 'Алгоритмический метод']]:
        res_table = PrettyTable()
        one, two, three = alg()
        res_table.add_column("№", indexes + ['Мера случайности', 'Итог'])


        one_coef = calc_hi(one, 0, 10)
        two_coef = calc_hi(two, 10, 100)
        three_coef = calc_hi(three, 100, 1000)
        res_table.add_column('1 разряд', one[:n_output] + [one_coef, check_with_criterion(one_coef, 1)])
        res_table.add_column('2 разряда', two[:n_output] + [two_coef, check_with_criterion(two_coef, 2)])
        res_table.add_column('3 разряда', three[:n_output] + [three_coef, check_with_criterion(three_coef, 3)])

        # res_table.add_row(['Мера случайности', one_coef, two_coef, three_coef])
        # res_table.add_row(['Итог',
        #                    check_with_criterion(one_coef, 1),
        #                    check_with_criterion(two_coef, 2),
        #                    check_with_criterion(three_coef, 3)])
        print(f"\t\t\t{alg_name}")
        print(res_table)

    one_tbl, two_tbl, three_tbl = random_from_table()

    table_tbl.add_column("№", indexes)
    table_tbl.add_column('1 разряд', one_tbl[:10])
    table_tbl.add_column('2 разряда', two_tbl[:10])
    table_tbl.add_column('3 разряда', three_tbl[:10])

    one_alg, two_alg, three_alg = random_from_alg()
    table_tbl.add_column('1 разряд', one_alg[:10])
    table_tbl.add_column('2 разряда', two_alg[:10])
    table_tbl.add_column('3 разряда', three_alg[:10])

    koef_tbl_one = calc_hi(one_tbl, 0, 10)
    koef_tbl_two = calc_hi(two_tbl, 10, 100)
    koef_tbl_three = calc_hi(three_tbl, 100, 1000)
    koef_alg_one = calc_hi(one_alg, 0, 10)
    koef_alg_two = calc_hi(two_alg, 10, 100)
    koef_alg_three = calc_hi(three_alg, 100, 1000)

    table_tbl.add_row(['Коэффициент', koef_tbl_one, koef_tbl_two, koef_tbl_three, koef_alg_one, koef_alg_two, koef_alg_three])

    table_tbl.add_row(['Критерий',
                      check_with_criterion(koef_tbl_one, 1),
                      check_with_criterion(koef_tbl_two, 2),
                      check_with_criterion(koef_tbl_three, 3),
                      check_with_criterion(koef_alg_one, 1),
                      check_with_criterion(koef_alg_two, 2),
                      check_with_criterion(koef_alg_three, 3)])
    print("\t\t\t                    Табличный метод\t\t\t\t\t                                    Алгоритмический метод")

    print(table_tbl)

    flag = input("Введите 1 если хотите проанализировать свою последовательность: ")
    if flag == '1':
        print("Выберите размерность вводимой последовательности")
        digit_str = input("Одноразрядные - введите 1, двухразрядные - введите 2, трехразрядные - введите 3: ")
        arr = []
        if digit_str in ['1', '2', '3']:
            print("Введите последовательность чисел (через пробел)")
            arr_str = list(input().split())
            for digit in arr_str:
                if len(digit) != int(digit_str):
                    print("Некорректная разрядность")
                    return
                try:
                    d = int(digit)
                except:
                    print("Некорректное значение")
                    return
                arr.append(d)
            if digit_str == '1':
                hi_koef = calc_hi(arr, 0, 10)
            elif digit_str == '2':
                hi_koef = calc_hi(arr, 10, 100)
            else:
                hi_koef = calc_hi(arr, 100, 1000)
            print("Коэффициент: ", hi_koef)
            print(check_with_criterion(hi_koef, int(digit_str)))
        else:
            print("Некорректный ввод")
            return

if __name__ == '__main__':
    main()