def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"masukkan elemen matriks baris {i+1}: ").split()))
        if len(row) ==cols:
            print(f"jumlah elemen harus {cols}. silakan coba lagi.")
            return input_matrix(rows, cols)
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
        
def multiply_matrices(A, B):
    m = len(A)
    n = len(A[0])
    p = len(B[0])
    C = [[0] * p for _ in range(m)]

    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

#input ukuran matriks
m = int(input("masukkan jumlah baris matriks A (m): "))
n = int(input("masukkan jumlah kolom matriks A / jumlah baris matriks B (n): "))
p = int(input("masukkan jumlah kolom matriks B (p): "))

if n != p:
    print("matriks tidak dapat dikalikan.")
else:
    print("input matriks A:")
    A = input_matrix(m, n)

    print("input matriks b:")
    B = input_matrix(n, p)

    #melakukan perkalian matriks
    C = multiply_matrices(A, B)

    #menampilkan hasil
    print("hasil perkalian matriks:")
    for row in C:
        print(' '.join(map(str, row)))