# -*- coding: utf-8 -*-
"""10_Transpose

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KtmSX2ZsTnKw10MPtC1lk6E_Nm8l0LMH
"""

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transpose = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transpose[j][i] = matrix[i][j]

    return transpose

# Example usage with user input:
def main():
    matrix = []
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    print("Enter the elements row-wise:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter element [{i}][{j}]: "))
            row.append(element)
        matrix.append(row)

    print("Original Matrix:")
    for row in matrix:
        print(row)

    transposed_matrix = transpose_matrix(matrix)
    print("\nTransposed Matrix:")
    for row in transposed_matrix:
        print(row)

if __name__ == "__main__":
    main()

