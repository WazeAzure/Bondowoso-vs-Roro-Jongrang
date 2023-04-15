# Contain Frequently used functions 
from globals import Nmax,Mark

# TODO : mencari index_baris suatu atribut dalam suatu matrix. 
# Mengembalikan -1 jika atribut tidak ada di matrix.
def atribut_line_idx(matrix : list, atribut : str, collum : int) -> int :
  i = 0 
  while i < Nmax and matrix[i] != [Mark for i in range(collum)] :
    if atribut == matrix[i][collum] : 
      return i 
    i += 1 
  return -1
