from typing import *
from prettytable import PrettyTable
from random import random, seed
seed(0)

REQUESTS_TO_GENERATE = 300
MOD_TIME_STEP = 0.01

CLIENT_TIMES = [8, 12]
O1_TIMES = [15, 25]
O2_TIMES = [30, 50]
O3_TIMES = [20, 60]
C1_TIME = 15
C2_TIME = 30

ACCUMULATORS = [0, 0]
O1_ACCUM_INDEX = 0
O2_ACCUM_INDEX = 0
O3_ACCUM_INDEX = 1
C1_ACCUM_INDEX = 0
C2_ACCUM_INDEX = 1


class DistributedTimeGenerator:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def generate(self):
        return self.a + (self.b - self.a) * random()


class RequestsGenerator:
    def __init__(self, time_generator: DistributedTimeGenerator):
        self.time_generator = time_generator
        self.remaining_time = 0

    def update_time_and_check_for_request(self):
        if self.remaining_time > 0:
            self.remaining_time -= MOD_TIME_STEP
            return False
        else:
            self.remaining_time = self.time_generator.generate()
            return True


class Operator:
    def __init__(self, accum_index: int, time_generator: DistributedTimeGenerator):
        self.accum_index = accum_index
        self.time_generator = time_generator

        self.is_busy = False
        self.remaining_time = 0

    def update_time(self):
        self.remaining_time -= MOD_TIME_STEP

        if self.is_busy and self.remaining_time <= 0:
            self.is_busy = False
            ACCUMULATORS[self.accum_index] += 1

    def start_process_new_request(self):
        self.is_busy = True
        self.remaining_time = self.time_generator.generate()


class Computer:
    def __init__(self, accum_index: int, processing_time: int):
        self.accum_index = accum_index
        self.processing_time = processing_time
        self.is_busy = False
        self.remaining_time = 0

    def update_time_and_check_for_finished_processing(self):
        self.remaining_time -= MOD_TIME_STEP

        if self.is_busy:
            if self.remaining_time <= 0:
                self.is_busy = False
                return True
        else:
            if ACCUMULATORS[self.accum_index] > 0:
                ACCUMULATORS[self.accum_index] -= 1
                self.is_busy = True
                self.remaining_time = self.processing_time

        return False


def find_free_operator(operators):
    for i in range(len(operators)):
        if not operators[i].is_busy:
            return i


def simulate():
    requests_generator = RequestsGenerator(DistributedTimeGenerator(*CLIENT_TIMES))

    operators = [
        Operator(O1_ACCUM_INDEX, DistributedTimeGenerator(*O1_TIMES)),
        Operator(O2_ACCUM_INDEX, DistributedTimeGenerator(*O2_TIMES)),
        Operator(O3_ACCUM_INDEX, DistributedTimeGenerator(*O3_TIMES))
    ]

    computers = [
        Computer(C1_ACCUM_INDEX, C1_TIME),
        Computer(C2_ACCUM_INDEX, C2_TIME)
    ]

    generated, processed, rejected, modeling_time = 0, 0, 0, 0
    while processed + rejected < REQUESTS_TO_GENERATE:
        modeling_time += MOD_TIME_STEP
        if generated < REQUESTS_TO_GENERATE:
            request = requests_generator.update_time_and_check_for_request()
            if request:
                generated += 1
                free_operator_index = find_free_operator(operators)
                if free_operator_index is None:
                    rejected += 1
                else:
                    operators[free_operator_index].start_process_new_request()

        for operator in operators:
            operator.update_time()

        for computer in computers:
            if computer.update_time_and_check_for_finished_processing():
                processed += 1

    return generated, processed, rejected, modeling_time


def main():
    global REQUESTS_TO_GENERATE
    global C2_TIME
    global O3_TIMES
    global CLIENT_TIMES

    res_table = PrettyTable()
    res_table.field_names = ['Случай', 'Имитационное время моделирования', 'Вероятность отказа']

    seed(0)
    generated, processed, rejected, modeling_time = simulate()
    print(generated, processed, rejected, modeling_time)
    res_table.add_row(['Исходные настройки', modeling_time, round(rejected / generated, 2)])

    seed(0)
    mn = 10
    tmp = REQUESTS_TO_GENERATE
    REQUESTS_TO_GENERATE = REQUESTS_TO_GENERATE * mn
    generated, processed, rejected, modeling_time = simulate()
    print(generated, processed, rejected, modeling_time)
    res_table.add_row([f'Количество заявок увеличено в {mn} раза', modeling_time, round(rejected / generated, 2)])
    REQUESTS_TO_GENERATE = tmp

    seed(0)
    mn = 3
    tmp = C2_TIME
    C2_TIME = C2_TIME * mn
    generated, processed, rejected, modeling_time = simulate()
    print(generated, processed, rejected, modeling_time)
    res_table.add_row([f'Время 2 компьютера увеличено в {mn} раза', modeling_time, round(rejected / generated, 2)])
    C2_TIME = tmp

    seed(0)
    mn = 3
    tmp = O3_TIMES
    O3_TIMES = list(map(lambda time: time * mn, O3_TIMES))
    generated, processed, rejected, modeling_time = simulate()
    print(generated, processed, rejected, modeling_time)
    res_table.add_row([f'Время 3 оператора увеличено в {mn} раза', modeling_time, round(rejected / generated, 2)])
    O3_TIMES = tmp

    seed(0)
    mn = 2
    tmp = CLIENT_TIMES
    CLIENT_TIMES = list(map(lambda time: time // mn, CLIENT_TIMES))
    generated, processed, rejected, modeling_time = simulate()
    print(generated, processed, rejected, modeling_time)
    res_table.add_row([f'Время генерации заявок уменьшено в {mn} раза', modeling_time, round(rejected / generated, 2)])
    CLIENT_TIMES = tmp

    print(res_table)

if __name__ == '__main__':
    main()