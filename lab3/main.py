from prettytable import PrettyTable
from RandomClass import Random
from math import sqrt

N_RANDOMS = 100000
eps = 1e-6
N_OUTPUT = 10

numbers_limits = {1: [0, 10], 2: [10, 99], 3: [100, 999]}


def hi2_quantiles_for_v(v, ps=(1, 5, 10, 90, 95, 99)):
    return {xp: v + (sqrt(2 * v) * xp) + (2 * (xp ** 2) / 3) - (2 / 3) for xp in ps}


hi2_quantiles = {
    # 1 цифра -> возможные числа [0; 9] -> возможно 19 разниц [-9; 9] (10 чисел)
    1: {1: 2.088, 5: 3.325, 10: 4.158, 90: 14.684, 95: 16.919, 99: 21.666},
    # 2 цифры ->возможные числа [10; 99] -> возможно 179 разниц [-89; 89] (90 чисел)
    2: hi2_quantiles_for_v(89),
    # 3 цифры ->возможные числа [100; 999] -> возможно 1799 разниц [-899; 899] (900 чисел)
    3: hi2_quantiles_for_v(899),
}

for row in hi2_quantiles.items():
    print(row)


def random_from_table():
    with open('random_ints.txt') as file:
        lines = file.readlines()

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
    one = [random.randint(*numbers_limits[1]) for _ in range(N_RANDOMS)]
    two = [random.randint(*numbers_limits[2]) for _ in range(N_RANDOMS)]
    three = [random.randint(*numbers_limits[3]) for _ in range(N_RANDOMS)]
    return one, two, three


def calc_coef(random_numbers, start_random, end_random):
    if start_random != 0:
        end_random += 1
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


def analyze_coef(counted_coef, digits_amount):
    if counted_coef < hi2_quantiles[digits_amount][1] or counted_coef > hi2_quantiles[digits_amount][99]:
        return "Числа не случайные"
    elif hi2_quantiles[digits_amount][5] < counted_coef < hi2_quantiles[digits_amount][95]:
        return "Числа случайные"
    else:
        return "Числа подозрительные"


def check_limit_values():
    tests = [
        [1, list(range(10))],
        [1, list(range(9, -1, -1))],
        [1, [1, 3, 1, 3, 1, 3, 1, 3, 1, 3]],
        # [2, list(range(10, 100))],#[:N_OUTPUT]],
        # [2, list(range(99, 9, -1))],#[:N_OUTPUT]],
        #[2, [10, 30, 10, 30, 10, 30, 10, 30, 10, 30]],
        [3, list(range(100, 1000))],#[:N_OUTPUT]],
        # [3, list(range(999, 99, -1))],#[:N_OUTPUT]],
        #[3, [100, 300, 100, 300, 100, 300, 100, 300, 100, 300]],
    ]
    print('\n\n\nТестирование на предельных значениях')
    for digits, arr in tests:
        print()
        print(f'Разрядность: {digits}')
        print(f'Последовательность: {arr[:min(len(arr), N_OUTPUT)]}')
        coef = calc_coef(arr, *numbers_limits[digits])
        print(f'Мера случайности: {coef}')
        print(f'Итог: {analyze_coef(coef, digits)}')


def main():
    indexes = [i for i in range(N_OUTPUT)]

    for alg, alg_name in [[random_from_table, 'Табличный метод'], [random_from_alg, 'Алгоритмический метод']]:
        res_table = PrettyTable()
        one, two, three = alg()
        res_table.add_column("№", indexes + ['Мера случайности', 'Итог'])

        one_coef = calc_coef(one, *numbers_limits[1])
        two_coef = calc_coef(two, *numbers_limits[2])
        three_coef = calc_coef(three, *numbers_limits[3])
        res_table.add_column('1 разряд', one[:N_OUTPUT] + [one_coef, analyze_coef(one_coef, 1)])
        res_table.add_column('2 разряда', two[:N_OUTPUT] + [two_coef, analyze_coef(two_coef, 2)])
        res_table.add_column('3 разряда', three[:N_OUTPUT] + [three_coef, analyze_coef(three_coef, 3)])

        print(f"\t\t\t{alg_name}")
        print(res_table)

    check_limit_values()

    print("\n\n\n")
    digits = int(input("Разрядность вводимой последовательности (1, 2 или 3).\n"))
    print("Введите последовательность чисел через пробел")
    arr = list(map(int, input().split()))
    coef = calc_coef(arr, *numbers_limits[digits])
    print("Коэффициент: ", coef)
    print(analyze_coef(coef, digits))


if __name__ == '__main__':
    main()
