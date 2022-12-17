from scipy.stats import poisson
from numpy import random as numpy_random
import random
from prettytable import PrettyTable

class RequestsGenerator:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def get_request_time(self):
        return self.a + (self.b - self.a) * random.random()


class RequestsProcessor:
    def __init__(self, lambda_value, p_reenter: float):
        self.lambda_value = lambda_value
        self.p_reenter = p_reenter
        self.queue_size = 0
        self.max_queue_size = 0
        self.processed_requests = 0

    def process_request(self):
        if self.queue_size > 0:
            self.processed_requests += 1
            self.queue_size -= 1

            if numpy_random.random_sample() <= self.p_reenter:
                self.add_request_in_queue()
                self.processed_requests -= 1

    def get_processing_time(self):
        return poisson.rvs(self.lambda_value, size=1)[0]

    def add_request_in_queue(self):
        self.queue_size += 1
        if self.queue_size > self.max_queue_size:
            self.max_queue_size = self.queue_size

    def clean_stats(self):
        self.queue_size = 0
        self.max_queue_size = 0
        self.processed_requests = 0


class EventBasedController:
    @staticmethod
    def simulate(generator: RequestsGenerator, processor: RequestsProcessor, request_count):
        gen_next_event_time = generator.get_request_time()
        proc_next_event_time = gen_next_event_time + processor.get_processing_time()

        while processor.processed_requests < request_count:
            if gen_next_event_time <= proc_next_event_time:
                processor.add_request_in_queue()
                gen_next_event_time += generator.get_request_time()

            else:
                processor.process_request()
                if processor.queue_size > 0:
                    proc_next_event_time += processor.get_processing_time()
                else:
                    proc_next_event_time = gen_next_event_time + processor.get_processing_time()

        return processor.max_queue_size, round(proc_next_event_time)


class DeltaTBasedController:
    @staticmethod
    def simulate(generator: RequestsGenerator, processor: RequestsProcessor, request_count, delta_t):
        gen_next_event_time = generator.get_request_time()
        proc_next_event_time = gen_next_event_time
        current_time = 0

        while processor.processed_requests < request_count:
            if gen_next_event_time <= current_time:
                processor.add_request_in_queue()
                gen_next_event_time += generator.get_request_time()

            if current_time >= proc_next_event_time:
                processor.process_request()
                if processor.queue_size > 0:
                    proc_next_event_time += processor.get_processing_time()
                else:
                    proc_next_event_time = gen_next_event_time + processor.get_processing_time()

            current_time += delta_t

        return processor.max_queue_size, round(current_time)



def simulate_with_params(a, b, lambda_value, reenter_prob, n_tasks, delta_t):
    print()
    print(f'Генератор: R({a}, {b}), ОА: П({lambda_value}), '
          f'вероятность повторного попадания в очередь: {reenter_prob}, число заявок: {n_tasks}, delta t: {delta_t}')
    generator = RequestsGenerator(a, b)
    processor = RequestsProcessor(lambda_value, reenter_prob)

    random.seed(0)
    numpy_random.seed(0)
    event_based_result = EventBasedController.simulate(generator, processor, n_tasks)

    processor.clean_stats()
    random.seed(0)
    numpy_random.seed(0)
    delta_t_based_result = DeltaTBasedController.simulate(generator, processor, n_tasks, delta_t)

    print(f'Событийный принцип:    '
          f'Максимальный размер очереди: {event_based_result[0]}, время окончания моделирования: {event_based_result[1]}')
    print(f'Принцип delta t:       '
          f'Максимальный размер очереди: {delta_t_based_result[0]}, время окончания моделирования: {delta_t_based_result[1]}')
    return event_based_result[0], delta_t_based_result[0]


def main():
    a = 1
    b = 10
    n_tasks = 1000
    delta_t = 0.01

    lambda_values = [4, 10]
    reenter_probs = [0.1, 0.5]

    res_table = PrettyTable(field_names=['lambda', 'вероятность повторного попадания в очередь', 'максимальный размер очереди'])
    for lambda_value in lambda_values:
        for reenter_prob in reenter_probs:
            res_event, res_deltat = simulate_with_params(a, b, lambda_value, reenter_prob, n_tasks, delta_t)
            res_table.add_row([lambda_value, reenter_prob, f'Событийный: {res_event: 6d},   delta t: {res_deltat: 6d}'])
    print()
    print()
    print(res_table)





if __name__ == '__main__':
    main()
