import math
import copy


# Ввод матрицы пользователем.
def in_matr(matr):
    n = 11
    m = 11
    print(f'Создание матрицы')
    while n > 10:
        try:
            n = int(input('Введите количество строк:'))
            if n > 10:
                print('Ошибка ввода!\nСтрок не может быть больше 10.')
        except ValueError:
            print('Количество строк должно быть числом!')
    while m > 10:
        try:
            m = int(input('Введите количество столбцов:'))
            if m > 10:
                print('Ошибка ввода!\nСтолбцов не может быть больше 10.')
        except ValueError:
            print('Количество столбцов должно быть числом!')
    for i in range(n):
        matr.append([])
        for j in range(m):
            matr[i].append(float(input(f'Введите [{i + 1},{j + 1}]:')))


# Вывод матрицы.
def out_matr(matr):
    for i in range(len(matr)):
        print(matr[i])
    print('\n')


# Вычисление первой нормы матрицы.
def perv(matr):
    norm = 0.0
    Sum = []
    for i in range(len(matr)):
        Sum.append(0)
        for j in range(len(matr[i])):
            Sum[i] += math.fabs(matr[i][j])
        if norm < Sum[i]:
            norm = Sum[i]
    return norm


# Вычисление второй нормы матрицы.
def vtor(matr):
    norm = 0.0
    Sum = []
    for j in range(len(matr[i])):
        Sum.append(0)
        for k in range(len(matr)):
            Sum[j] += math.fabs(matr[k][j])
        if norm < Sum[j]:
            norm = Sum[j]
    return norm


# Вычисление третьей нормы матрицы.
def tret(matr):
    S = 0.0
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            S += matr[i][j] * matr[i][j]
    norm = math.sqrt(S)
    return norm


A = []
A1 = []
A2 = []
B = []
C = []
D = []
Norm1A = 0.0
Norm2A = 0.0
Norm3A = 0.0
co = 0
norm1A2co = 0.0
norm2A2co = 0.0
norm3A2co = 0.0
norm1C = 0.0
norm2C = 0.0
norm3C = 0.0
norm1B = 0.0
norm2B = 0.0
norm3B = 0.0
norm1D = 0.0
norm2D = 0.0
norm3D = 0.0
cht = 6
lo = 0

# Ввод матрицы A пользователем.
in_matr(A)

while cht < 1 or cht > 5:
    print('1. Вывести матрицу.')
    print('2. Вывести абсолютную величину (модуль) матрицы.')
    print('3. Вычислить нормы матрицы.')
    print('4. Проверить свойства норм матрицы.')
    print('5. Выйти.')
    cht = int(input('Введите число от 1 до 5:'))
    if cht == 1:
        # Вывод матрицы A.
        print('Вывод матрицы A:')
        out_matr(A)
        print('Вернуться в главное меню?')
        lo = int(input('1-да, 2-нет\n'))
        if lo == 1:
            cht = 6
            print("\n" * 5)
        else:
            cht = 5

    elif cht == 2:
        # Вычисление абсолютной величины (модуля) матрицы A.
        A1 = copy.deepcopy(A)
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] < 0:
                    A1[i][j] = -A[i][j]
                else:
                    A1[i][j] = A[i][j]

        # Вывод абсолютной величины (модуля) матрицы A.
        print('Вывод модуля матрицы A:')
        out_matr(A1)
        print('Вернуться в главное меню?')
        lo = int(input('1-да, 2-нет\n'))
        if lo == 1:
            cht = 6
            print("\n" * 5)
        else:
            cht = 5


    elif cht == 3:
        # Вычисление первой нормы матрицы A.
        norm1A = perv(A)
        print('Первая норма матрицы равна:', norm1A, '\n')

        # Вычисление второй нормы матрицы A.
        norm2A = vtor(A)
        print('Вторая норма матрицы A равна:', norm2A, '\n')

        # Вычисление третьей нормы матрицы A.
        norm3A = tret(A)
        print('Третья норма матрицы A равна:', norm3A, '\n')
        print('Вернуться в главное меню?')
        lo = int(input('1-да, 2-нет\n'))
        if lo == 1:
            cht = 6
            print("\n" * 5)
        else:
            cht = 5

    elif cht == 4:
        # Проверка свойств норм матриц.
        # Проверка первого свойства.
        co = int(input('Введите значение константы:'))
        print('\n')
        A2 = copy.deepcopy(A)

        for i in range(len(A)):
            for j in range(len(A[i])):
                A2[i][j] *= co

        norm1A2co = perv(A2)
        print('Проверка первого свойства')
        print(str(norm1A2co), '=', str(math.fabs(co) * norm1A))
        if norm1A2co == math.fabs(co) * norm1A:
            print('Свойство верно!')
        else:
            print('Свойство неверно!')
        print('\n')

        norm2A2co = vtor(A2)
        print(str(norm2A2co), '=', str(math.fabs(co) * norm2A))
        if norm2A2co == math.fabs(co) * norm2A:
            print('Свойство верно!')
        else:
            print('Свойство неверно!')
        print('\n')

        norm3A2co = tret(A2)
        print(str(norm3A2co), '=', str(math.fabs(co) * norm3A))
        if norm3A2co == math.fabs(co) * norm3A:
            print('Свойство верно!')
        else:
            print('Свойство неверно!')
        print('\n')

        # Проверка второго свойства.
        print(f'Создание матрицы B')
        for i in range(len(A)):
            B.append([])
            for j in range(len(A[i])):
                B[i].append(int(input(f'Введите B[{i + 1},{j + 1}]:')))
        print('\n')

        C = copy.deepcopy(A)
        for i in range(len(C)):
            for j in range(len(C[i])):
                C[i][j] = A[i][j] + B[i][j]

        print('Проверка второго свойства')
        norm1C = perv(C)
        norm1B = perv(B)
        print(str(norm1C), '<=', str(norm1A + norm1B))
        if norm1C <= (norm1A + norm1B):
            print('Свойство верно!')
        else:
            print('Свойство неверно!')
        print('\n')

        norm2C = vtor(C)
        norm2B = vtor(B)
        print(str(norm2C), '<=', str(norm2A + norm2B))
        if norm2C <= (norm2A + norm2B):
            print('Свойство верно!')
        else:
            print('Свойство неверно!')
        print('\n')

        norm3C = tret(C)
        norm3B = tret(B)
        print(str(norm3C), '<=', str(norm3A + norm3B))
        if norm3C <= (norm3A + norm3B):
            print('Свойство верно!')
        else:
            print('Свойство неверно!')
        print('\n')

        # Проверка третьего свойства.
        D = copy.deepcopy(A)
        for i in range(len(D)):
            for j in range(len(D[i])):
                D[i][j] = A[i][j] * B[i][j]

        print('Проверка третьего свойства')
        norm1D = perv(D)
        print(str(norm1D), '<=', str(norm1A * norm1B))
        if norm1D <= (norm1A * norm1B):
            print('Свойство верно!')
        else:
            print('Свойство неверно!')
        print('\n')

        norm2D = vtor(D)
        print(str(norm2D), '<=', str(norm2A * norm2B))
        if norm2D <= (norm2A * norm2B):
            print('Свойство верно!')
        else:
            print('Свойство неверно!')
        print('\n')

        norm3D = tret(D)
        print(str(norm3D), '<=', str(norm3A * norm3B))
        if norm3D <= (norm3A * norm3B):
            print('Свойство верно!')
        else:
            print('Свойство неверно!')
        print('\n')
        print('Вернуться в главное меню?')
        lo = int(input('1-да, 2-нет\n'))
        if lo == 1:
            cht = 6
            print("\n" * 5)
        else:
            cht = 5

    # Выйти.
    elif cht == 5:
        exit(0)
    else:
        print('Ошибка!')
