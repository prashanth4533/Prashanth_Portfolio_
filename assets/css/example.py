
def left_rotate_matrix(mat, k):
    rows, cols = len(mat), len(mat[0])

    # Calculate the effective number of rotations
    effective_rotations = k % cols

    for row in mat:
        # Perform left rotation using slicing
        row[:] = row[effective_rotations:] + row[:effective_rotations]

    return mat
k2 = 2
mat2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result2 = left_rotate_matrix(mat2, k2)
for row in result2:
    print(" ".join(map(str, row)))