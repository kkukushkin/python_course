import numpy as np

#task 1

random_vector = np.random.rand(10)
sorted_vector = np.sort(random_vector)
#print(sorted_vector)

#task2

matrix = np.zeros((8, 8), dtype=int)
matrix[::2, ::2] = 1  # Заполнение чётных строк и чётных столбцов
matrix[1::2, 1::2] = 1  # Заполнение нечётных строк и нечётных столбцов
#print(matrix)

#task 3
matrix1 = np.random.randint(1, 10, size=(8, 4))
matrix2 = np.random.randint(1, 10, size=(4, 2))
result_matrix = np.dot(matrix1, matrix2)
#print(result_matrix)

#task4
vector = np.linspace(0, 1, 12)[1:-1]
#print(vector)

#task5


def create_matrices(num):
    divisors = [i for i in range(2, num) if num % i == 0]
    matrices = []

    if not divisors:
        print("Нельзя разбить число на множители без остатка.")
    else:
        print(f"Множители для числа {num}: {divisors}")
        for i in divisors:
            m = num // i
            matrix = np.zeros((m, i), dtype=int)
            matrices.append(matrix)
            print(f"Матрица {m}x{i}:")
            print(matrix)
    return matrices

#create_matrices(12)

#task6

import re
class DataAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data_array = []

    def read_file(self):
        with open(self.file_path, 'r') as file:
            self.data_array = file.readlines()

    def search_text(self, pattern):
        matches = []
        for line in self.data_array:
            found = re.findall(pattern, line)
            matches.extend(found)
        return matches

# Пример использования класса
#analyzer = DataAnalyzer("____________.txt")
#analyzer.read_file()
#results = analyzer.search_text(r'pattern_to_search')
#print(results)

#task7

def process_vector(A, S, last=False):
    A_column_vector = np.reshape(A, (len(A), 1))
    B = np.random.rand(S, len(A))
    result_matrix = np.dot(B, A_column_vector)
    row_sum_vector = np.sum(result_matrix, axis=1)

    if not last:
        result_vector = np.sin(row_sum_vector)
    else:
        result_vector = np.maximum(row_sum_vector, 0)
    return result_vector, B

# Тестовые вызовы функции
# Первый вызов
vector1 = np.random.rand(5)
result1, matrix1 = process_vector(vector1, 10)
# Второй вызов
result2, matrix2 = process_vector(result1, 10)
# Третий вызов
result3, matrix3 = process_vector(result2, 5, last=True)

# Перевод значений результата в проценты
result3_percent = (result3 * 100).round(2)

# Вывод результатов в консоль
print("Результат в процентах для третьего вызова:")
print(result3_percent)

