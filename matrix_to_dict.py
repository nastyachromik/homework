def matrix_to_dict(matrix: list[list[int]]) -> dict[int, list[int]]:
    dicti = {}
    for i in range(len(matrix)):
        dicti[i+1] = matrix[i]
    return dicti

matrixx = [[5, 6, 7], [8, 3, 2], [4, 9, 8]]
print(matrix_to_dict(matrixx))