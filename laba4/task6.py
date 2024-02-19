bork = []


#   - Эта функция заполняет матрицу bork для четного количества столбцов. 
#   - Генерируется двумерный список bork размером m_str x m_col, заполненный последовательными числами, начиная с 1.
#   - Четные столбцы заполняются снизу вверх, а нечетные - сверху вниз.
#   - Работа завершается возвращением заполненной матрицы bork.
def cols_is_even(m_str, m_col):
    global bork
    bork = [[0]*m_col for i in range(m_str)]
    count = 0 
    for col in range(m_col-1, -1, -1): 
        if col % 2 == 0: 
            for row in range(m_str-1, -1, -1): 
                count += 1
                bork[row][col] = count
        else:
            for row in range(0, m_str, 1):
                count += 1
                bork[row][col] = count
    return bork


#   - Эта функция заполняет матрицу bork для нечетного количества столбцов аналогично функции cols_is_even.
#   - Единственное отличие - условие на нечетные столбцы.
#   - Результатом является заполненная матрица bork.
def cols_is_uneven(m_str, m_col):
    global bork
    bork = [[0]*m_col for i in range(m_str)]
    count = 0
    for col in range(m_col-1, -1, -1):
        if col % 2 == 1:
            for row in range(m_str-1, -1, -1):
                count += 1
                bork[row][col] = count
        else:
            for row in range(0, m_str, 1):
                count += 1
                bork[row][col] = count
    return bork


#   - Эта функция в зависимости от четности/нечетности числа столбцов вызывает соответствующую функцию для заполнения матрицы.
#   - Если количество столбцов четное, вызывается `colsisuneven`, иначе `colsiseven`.
def matrix_build(m_str, m_col): 
    global bork
    if m_col % 2 == 0:
        cols_is_uneven(m_str, m_col)
    else:
        cols_is_even(m_str, m_col)

#   - Функция отражает матрицу по вертикали, меняя порядок строк на противоположный.
def mat_mir_down(matrix_d):
    matrix_d = bork[::-1]
    return matrix_d

#   - Данная функция отражает матрицу по горизонтали, меняя порядок элементов в каждой строке на обратный.
def matr_mir_down_right(mirr_matrix):
    matrix_d_r = [row[::-1] for row in mirr_matrix] #срез, создание копии списка с элементами в обратном порядке
    return matrix_d_r

#   - Эта функция выполняет двойное отражение матрицы: сначала по вертикали, а затем по горизонтали.
def matr_mir_down_right_up(mirr_matrix_dru):
    matrix_d_r_u = mirr_matrix_dru[::-1]
    return matrix_d_r_u

#   - Выводит на экран две матрицы: основную и ее отражение сначала вниз, затем вправо и вверх.
#   - Выполняет сравнение построчно двух матриц и выводит результат с разделителями.
def print_mirrored_matrix():
    print("основная + отзеркаленная вниз-вправо-вверх (вправо) матрицы")
    for item1, item2 in zip(bork, matr_mir_down_right_up(matr_mir_down_right(mat_mir_down(bork)))):
        print('\t'.join(map(str, item1)) + "\t|\t" + '\t'.join(map(str, item2)))
    print("")
    for item1, item2 in zip(mat_mir_down(bork), matr_mir_down_right(mat_mir_down(bork))):
        print('\t'.join(map(str, item1)) + "\t|\t" + '\t'.join(map(str, item2)))
    print("отзеркаленная вниз + отзеркаленная вниз-вправо матрицы")


def main():
    while True:
        try:
            rows = int(input("Введите кол-во строк матрицы:\n"))
            if rows > 0:
                break
            else:
                print("только положительные целочисленные значения N = [1, 2, 3,...]")
        except ValueError:
            print("только натуральные числа")

    while True:
        try:
            cols = int(input("Введите кол-во столбцов матрицы:\n"))
            if cols > 0:
                break
            else:
                print("только положительные целочисленные значения N = [1, 2, 3,...]")
        except ValueError:
            print("только натуральные числа")
    print(f"Размерность матрицы - {rows}x{cols}")
    matrix_build(rows, cols)
    print_mirrored_matrix()


if __name__ == "__main__":
    main()
