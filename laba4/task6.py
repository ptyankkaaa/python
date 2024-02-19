bork = []


def cols_is_even(m_str, m_col):
    global bork
    bork = [[0]*m_col for i in range(m_str)]  #создается двумерный список с размером `m_str` строк на `m_col` столбцов, заполненный нулями
    count = 0 #для отслеживания номера текущего элемента в матрице
    for col in range(m_col-1, -1, -1): #бежит по столбцам от последнего к первому
        if col % 2 == 0: #проверяет столбец на чётность
            for row in range(m_str-1, -1, -1): #бежит по строкам от последнего к первому
                count += 1
                bork[row][col] = count
        else:
            for row in range(0, m_str, 1):
                count += 1
                bork[row][col] = count
    return bork


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


def matrix_build(m_str, m_col): 
    global bork
    if m_col % 2 == 0:
        cols_is_uneven(m_str, m_col)
    else:
        cols_is_even(m_str, m_col)


def mat_mir_down(matrix_d):
    matrix_d = bork[::-1]
    return matrix_d


def matr_mir_down_right(mirr_matrix):
    matrix_d_r = [row[::-1] for row in mirr_matrix]
    return matrix_d_r


def matr_mir_down_right_up(mirr_matrix_dru):
    matrix_d_r_u = mirr_matrix_dru[::-1]
    return matrix_d_r_u


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
