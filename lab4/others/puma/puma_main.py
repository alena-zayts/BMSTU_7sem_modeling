from numpy.random import normal
import random


class EvenDistribution:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def generate(self):
        return self.a + (self.b - self.a) * random.random()




class NormalDistribution:
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

    def generate(self):
        return normal(self.mu, self.sigma)



######## event
from random import randint


def event_model(generator, processor, total_tasks=0, repeat=0):
    processed_tasks = 0
    cur_queue_len = max_queue_len = 0
    events = [[generator.generate(), 'g']]
    free, process_flag = True, False

    while processed_tasks < total_tasks:
        event = events.pop(0)
        # Генератор
        if event[1] == 'g':
            cur_queue_len += 1
            if cur_queue_len > max_queue_len:
                max_queue_len = cur_queue_len
            add_event(events, [event[0] + generator.generate(), 'g'])
            if free:
                process_flag = True
        # Обработчик
        elif event[1] == 'p':
            processed_tasks += 1
            if randint(1, 100) <= repeat:
                cur_queue_len += 1
            process_flag = True

        if process_flag:
            if cur_queue_len > 0:
                cur_queue_len -= 1
                add_event(events, [event[0] + processor.generate(), 'p'])
                free = False
            else:
                free = True
            process_flag = False

    return max_queue_len


def add_event(events, event: list):
    i = 0
    while i < len(events) and events[i][0] < event[0]:
        i += 1
    if 0 < i < len(events):
        events.insert(i - 1, event)
    else:
        events.insert(i, event)


######### delta

def step_model(generator, processor, total_tasks=0, repeat=0, step=0.001):
    processed_tasks = 0
    t_curr = step
    t_gen = generator.generate()
    t_gen_prev = t_proc = 0
    cur_queue_len = max_queue_len = 0
    free = True

    while processed_tasks < total_tasks:
        # Генератор
        if t_curr > t_gen:
            cur_queue_len += 1
            if cur_queue_len > max_queue_len:
                max_queue_len = cur_queue_len
            t_gen_prev = t_gen
            t_gen += generator.generate()

        # Обработчик
        if t_curr > t_proc:
            if cur_queue_len > 0:
                was_free = free
                if free:
                    free = False
                else:
                    processed_tasks += 1
                    if random.randint(1, 100) <= repeat:
                        cur_queue_len += 1
                cur_queue_len -= 1
                if was_free:
                    t_proc = t_gen_prev + processor.generate()
                else:
                    t_proc += processor.generate()
            else:
                free = True
        t_curr += step

    return max_queue_len


def main():
    a, b = 1, 10
    generator = EvenDistribution(a, b)

    mu, sigma = 4, 0.2  # диапазон +- [3;5]
    processor = NormalDistribution(mu, sigma)

    total_tasks = 1000
    repeat_percentage = 0
    step = 0.01

    print('event_model:', event_model(generator, processor, total_tasks, repeat_percentage))
    print('step_model:', step_model(generator, processor, total_tasks, repeat_percentage, step))


if __name__ == '__main__':
    main()