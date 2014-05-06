# coding=utf-8

vector = [2,3,6,5]
matrix = [
  [1,3,9,2],
  [2,4,6,8]
]

matrixA = [
  [1,3,9,2],
  [2,4,6,8]
]
matrixB = [
  [2,1],
  [3,2],
  [6,0],
  [5,4]
]


print 'vector', vector
print 'matrix', matrix
print 'matrixA', matrixA
print 'matrixB', matrixB


def matrix_multiplication(matrix, multiplier):
  try:
    return [[cell * multiplier for cell in row] for row in matrix]
  except:
    print 'matrix_multiplication calculation error'


print '\nmatrix_multiplication(matrix, 5)\n', matrix_multiplication(matrix, 5)

def vectorMatrix_multiplication(matrix, vector):
  # I attmeped to do it using the inline style above, but was having issues
  try:
    for i in range(len(matrix)):
      for j in range(len(vector)):
        matrix[i][j] = vector[j] * matrix[i][j]
      matrix[i] = sum(matrix[i])
    return matrix
  except:
    print 'vectorMatrix_multiplication calculation eror'

print '\nvectorMatrix_multiplication(matrix, vector)\n', vectorMatrix_multiplication(matrix, vector)

# use unittest eventually...
print '\nTrying to multiply with bad vector [2,3]'
vectorMatrix_multiplication(matrix, [2,3])

# add matrix matrix multiplication

def matrixMatrix_multiplication(matrix1, matrix2):
  # times the

  if len(matrix1[0]) == len(matrix2):
    print 'The new matrix will be ', len(matrix1), 'x' , len(matrix2[0])

    result = [[0 for col in range(len(matrix1))] for row in range(len(matrix2[0]))]
    for i in range(len(matrix1)):
      for j in range(len(matrix2[0])):
        cell = []
        # cell = []
        for k in range(len(matrix1[0])):
          print 'i, j, k', i, j, k
          cell.append(matrix1[i][k] * matrix2[k][j])
        print 'cell is', cell
        result[i][j] = sum(cell)

    print 'Result:'
    return result

print '\nmatrixMatrix_multiplication(matrixA,matrixB)\n', matrixMatrix_multiplication(matrixA,matrixB)



def iMatrix(identity):
  matrix = []
  for i in range(identity):
    matrix.append([])
    for j in range(identity):
      if i == j:
        matrix[i].append(1)
      else:
        matrix[i].append(0)
  return matrix

print '\niMatrix(6)\n', iMatrix(6)