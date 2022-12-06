from typing import *
from prettytable import PrettyTable
from random import random, seed
from scipy.stats import poisson
from numpy.random import normal
seed(1)

MOD_TIME_STEP = 0.01


class UniformlyDistributedTimeGenerator:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def generate(self):
        return self.a + (self.b - self.a) * random()


class NormallyDistributedTimeGenerator:
    def __init__(self, m: float, sigma: float):
        self.m = m
        self.sigma = sigma

    def generate(self):
        return normal(self.m, self.sigma)


class PoissonDistributedTimeGenerator:
    def __init__(self, lambda_value: int):
        self.lambda_value = lambda_value

    def generate(self):
        return poisson.rvs(self.lambda_value, size=1)[0]


class Request:
    def __init__(self, washing_p):
        self.need_wash = random() < washing_p


class RequestsGenerator:
    def __init__(self, time_generator, washing_p):
        self.remaining_time = 0
        self.time_generator = time_generator
        self.washing_p = washing_p

    def update_time_and_check_for_request(self):
        if self.remaining_time > 0:
            self.remaining_time -= MOD_TIME_STEP
            return None
        else:
            t = self.time_generator.generate()
            if t == 0:
                self.remaining_time = 1
            else:
                self.remaining_time = 1 / t
            # print(self.remaining_time)
            return Request(self.washing_p)


class OnePlaceChannel:
    def __init__(self, accum_in: List, accum_out: List, time_generator, max_out_accum=None):
        self.accum_in = accum_in
        self.accum_out = accum_out
        self.time_generator = time_generator
        self.max_out_accum = max_out_accum

        self.is_busy = False
        self.remaining_time = 0
        self.processed_count = 0

    def update_time(self):
        processed = False
        if self.max_out_accum is None or len(self.accum_out) < self.max_out_accum:
            if self.is_busy:
                self.remaining_time -= MOD_TIME_STEP

                if self.remaining_time <= 0:
                    self.processed_count += 1
                    self.is_busy = False
                    self.accum_out.append(0)
                    processed = True

            if not self.is_busy:
                if len(self.accum_in) > 0:
                    self.accum_in.pop(0)
                    self.is_busy = True
                    self.remaining_time = self.time_generator.generate()
        return processed

    # def start_process_new_request(self):
    #     self.is_busy = True
    #     self.remaining_time = self.time_generator.generate()


class SimultaneousChannel:
    def __init__(self, accum_out, time_generator):
        self.accum_in = []
        self.accum_out = accum_out
        self.time_generator = time_generator
        self.processed_count = 0

    def start_process_new_request(self):
        self.accum_in.append(self.time_generator.generate())

    def update_time(self):
        left_times = []
        finished_count = 0
        for time in self.accum_in:
            time -= MOD_TIME_STEP
            if time > 0:
                left_times.append(time)
            else:
                finished_count += 1
                self.accum_out.append(0)
        self.accum_in = left_times
        self.processed_count += finished_count

        return finished_count


def simulate(requests=10000, requests_lambda=1, n_washers=5, washing_p=0.1, parking_spaces=50):
    washing_times = (40, 80)
    tc_m = 150
    tc_sigma = 10

    operator_parking_times = [1, 3]
    operator_washing_times = [1, 3]
    operator_paying_times = [2, 4]

    max_operator_parking_len = 30
    max_operator_washing_len = 5

    operator_parking_accum = []
    operator_washing_accum = []
    washing_accum = []
    parking_accum = []
    paying_accum = []
    processed_accum = []

    requests_generator = RequestsGenerator(PoissonDistributedTimeGenerator(lambda_value=requests_lambda), washing_p)
    operator_parking = OnePlaceChannel(operator_parking_accum, parking_accum,
                                       UniformlyDistributedTimeGenerator(*operator_parking_times), max_out_accum=parking_spaces)
    operator_washing = OnePlaceChannel(operator_washing_accum, parking_accum,
                                       UniformlyDistributedTimeGenerator(*operator_washing_times), max_out_accum=parking_spaces)
    tc = SimultaneousChannel(paying_accum, NormallyDistributedTimeGenerator(tc_m, tc_sigma))
    washers = [OnePlaceChannel(washing_accum, paying_accum,
                               UniformlyDistributedTimeGenerator(*washing_times)) for _ in range(n_washers)]
    operator_paying = OnePlaceChannel(paying_accum, processed_accum,
                                      UniformlyDistributedTimeGenerator(*operator_paying_times))

    washing_generated, parking_generated, washing_rejected, parking_rejected, modeling_time, max_paying_len = 0, 0, 0, 0, 0, 0

    while len(processed_accum) < requests:
        if len(paying_accum) > max_paying_len:
            max_paying_len = len(paying_accum)

        #print(washing_generated + parking_generated, len(processed_accum), len(parking_accum), len(tc.accum_in))
        modeling_time += MOD_TIME_STEP
        if (washing_generated + parking_generated) < requests:
            request = requests_generator.update_time_and_check_for_request()
            if request is not None:
                if request.need_wash:
                    washing_generated += 1
                    if len(operator_washing_accum) >= max_operator_washing_len:
                        washing_rejected += 1
                        processed_accum.append(0)
                    else:
                        operator_washing_accum.append(0)
                else:
                    parking_generated += 1
                    if len(operator_parking_accum) >= max_operator_parking_len:
                        parking_rejected += 1
                        processed_accum.append(0)
                    else:
                        operator_parking_accum.append(0)

        new_visitor_to_tc = operator_parking.update_time()
        if new_visitor_to_tc:
            tc.start_process_new_request()
        visitors_from_tc = tc.update_time()
        for _ in range(visitors_from_tc):
            parking_accum.pop(0)

        washing_request = operator_washing.update_time()
        if washing_request:
            washing_accum.append(0)

        for operator in washers:
            washing_finished = operator.update_time()
            if washing_finished:
                parking_accum.pop(0)

        operator_paying.update_time()

    print(washing_generated, parking_generated, washing_rejected, parking_rejected, modeling_time, max_paying_len)
    return washing_generated, parking_generated, washing_rejected, parking_rejected, modeling_time, max_paying_len

def add_row(table, name, washing_generated, parking_generated, washing_rejected, parking_rejected, modeling_time,
            max_paying_len):
    table.add_row([name, round(modeling_time),
                       washing_generated + parking_generated,
                       round(100 * washing_generated / (parking_generated + washing_generated)),
                       round(100 * parking_rejected / (parking_generated + parking_rejected)),
                       round(100 * washing_rejected / (washing_generated + washing_rejected)),
                       max_paying_len
                       ])

def main():
    res_table = PrettyTable()
    res_table.field_names = ['Случай', 'Им. время модел.',
                             'Кол-во клиентов', '% обр. за автомойкой',
                             '% отказа от парковки', '% отказа от автомойки', 'max очередь на оплату']

    add_row(res_table, 'Исходный', *simulate())
    add_row(res_table, 'requests_lambda=10', *simulate(requests_lambda=10))
    add_row(res_table, 'n_washers=7', *simulate(n_washers=7))
    add_row(res_table, 'washing_p=0.3', *simulate(washing_p=0.3))
    add_row(res_table, 'parking_spaces=100', *simulate(parking_spaces=100))
    add_row(res_table, 'parking_spaces=500', *simulate(parking_spaces=500))
    add_row(res_table, 'requests=50000', *simulate(requests=50000))

    print(res_table)


if __name__ == '__main__':
    main()