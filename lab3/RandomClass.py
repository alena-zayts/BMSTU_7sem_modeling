
# MT19937, 32-битный генератор MT
class Random():
    def __init__(self, c_seed=0):
        # Параметры n и r выбраны так, что характеристический многочлен примитивный или
        # (nw — r) (число клеток в регистре сдвига, пространство состояний) равна числу Мерсенна 19937
        self.w = 32  # размер слова -- 32 бит
        self.n = 624  # число элементов в регистре сдвига
        self.r = 31  # количество младших бит
        self.m = 397

        # Параметры закалки подобраны так, что мы можем получить хорошее равномерное распределение.
        self.l = 18
        self.s = 7
        self.t = 15
        self.u = 11
        self.a = 0x9908B0DF
        self.b = 0x9D2C5680
        self.c = 0xEFC60000

        self.f = 1812433253

        # Массив для хранения состояний генератора
        self.MT = [0 for _ in range(self.n)]
        self.lower_mask = 0x7FFFFFFF  # битовая маска младших r бит,
        self.upper_mask = 0x80000000  # битовая маска старших w-r бит

        # Инициализация
        self.index = self.n + 1
        self.seed(c_seed)

    def seed(self, num):
        """
        Начальное заполнение матрицы состояний
        """
        self.MT[0] = num
        for i in range(1, self.n):
            temp = self.f * (self.MT[i-1] ^ (self.MT[i-1] >> (self.w-2))) + i
            self.MT[i] = temp & 0xffffffff

    def twist(self):
        """
        Генерация следующих n значений из последовательности x_i
        """
        for i in range(self.n):
            # Шаг 2. Вычисление (xiu | xi+1l)
            x = (self.MT[i] & self.upper_mask) + \
                (self.MT[(i+1) % self.n] & self.lower_mask)
            # Шаг 3. Вычисление значения следующего элемента последовательности по
            # рекуррентному выражению
            xA = x >> 1
            if (x % 2) != 0:
                xA = xA ^ self.a
            self.MT[i] = self.MT[(i + self.m) % self.n] ^ xA
        self.index = 0

    def extract_number(self):
        """
        Закалка (на основе MT[index])
        Необработанные последовательности, генерируемые рекурсией, обладают плохим равномерным распределением на больших
        размерностях. Чтобы это исправить, используется метод закалки (англ. tempering), на выходе которого получается
        итоговая псевдослучайная последовательность. Метод заключается в том, что каждое сгенерированное слово
        умножается справа на специальную обратимую матрицу T размера w × w.
        Каждые n чисел вызывается twist
        """
        if self.index >= self.n:
            self.twist()
        # Шаг 4. Вычисление x[i]T
        y = self.MT[self.index]
        y = y ^ ((y >> self.u) & 0xFFFFFFFF)
        y = y ^ ((y << self.s) & self.b)
        y = y ^ ((y << self.t) & self.c)
        y = y ^ (y >> self.l)

        self.index += 1
        return y & 0xffffffff

    def random(self):
        """ Равномерное распределение [0,1) """
        return self.extract_number() / 4294967296  # 2^w

    def randint(self, a, b):
        """ Случайное целое на отрезке [a,b) """
        n = self.random()
        return int(n / (1 / (b-a)) + a)

