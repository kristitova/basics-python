class Matrix:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return 'Матрица:\n' + '\n'.join(' '.join([str(elem) for elem in row]) for row in self.num)

    def __add__(self, other):
        try:
            return 'Матрица при сложении:\n' + '\n'.join(' '.join([str(self.num[i][j] + other.num[i][j])
                                                                   for j in range(len(self.num[i]))])
                                                         for i in range(len(self.num)))
        except:
            return 'Матрицы разных размеров!'


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[-2, 2, 1], [3, -2, 4], [5, 4, 2]])
print(matrix_1 + matrix_2)
