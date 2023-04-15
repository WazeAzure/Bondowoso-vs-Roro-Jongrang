from globals import *
from util import atribut_line_idx

def isiJin(username : str , password : str, tipe_jin : str , jin_index : int,  matrix : list ) -> list :
  matrix[jin_index][idx_username] = username
  matrix[jin_index][idx_password] = password 
  matrix[jin_index][idx_role] = tipe_jin

def summonjin() -> None : 
  print("Jenis jin yang dapat dipanggil: \n"
  "  (1) Pengumpul - Bertugas mengumpulkan bahan bangunan\n"
  "  (2) Pembangun - Bertugas membangun candi")
  while True : 
    nomor_jin = input("Masukkan nomor jenis jin yang ingin dipanggil (1/2): ")
    if nomor_jin != "1" and nomor_jin != "2" :
      print(f"Tidak ada jenis jin bernomor “{nomor_jin}”!")
    else :
      break
  
  if nomor_jin == "1" :
    tipe_jin = "Pengumpul"
  else : 
    tipe_jin = "Pembangun"
  print(f"Memilih jin '{tipe_jin}'")
  
  while True : 
    username = input("Masukkan username jin: ")
    jin_index = atribut_line_idx(users,username,idx_username) 
    if jin_index != -1 : 
      print(f"Username {username} sudah diambil!")
    else : break

  while True : 
    password = input("Masukkan password jin: ")
    if len(password) < 5 or len(password) > 25 : 
      print("Password panjangnya harus 5-25 karakter!")
    else :
      break
  
  isiJin(username, password , tipe_jin , jin_index, users)  
  print("Mengumpulkan sesajen...")
  print("Menyerahkan sesajen...")
  print("Membacakan mantra...")
  print(f"Jin {username} berhasil dipanggil!")
  
