vector = [2,3,6,5]
matrix = [
  [1,3,9,2],
  [2,4,6,8]
]

print 'vector', vector
print 'matrix', matrix

def matrix_multiplication(matrix, multiplier):
  return [[cell * multiplier for cell in row] for row in matrix]

print 'matrix_multiplication(matrix, 5)', matrix_multiplication(matrix, 5)

def vectorMatrix_multiplication(matrix, vector):
  # I attmeped to do it using the inline style above, but was having issues

  for i in range(len(matrix)):
    for j in range(len(vector)):
      matrix[i][j] = vector[j] * matrix[i][j]
    matrix[i] = sum(matrix[i])
  return matrix

print vectorMatrix_multiplication(matrix, vector)