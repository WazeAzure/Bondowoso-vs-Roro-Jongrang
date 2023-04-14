def validasi_search(users : list, username : str) -> int :
  i = 0 
  while i < Nmax and users[i] != [Mark for i in range(Nmax)] :
    if username == users[i][user_id] : 
       return i 
    i += 1 
  return -1

def summonjin() -> None : 
  print(" Jenis jin yang dapat dipanggil: \n"
  "  (1) Pengumpul - Bertugas mengumpulkan bahan bangunan\n"
  "  (2) Pembangun - Bertugas membangun candi")
  nomor_jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: ",end=""))
  while True : 
    if nomor_jin != 1 and nomor_jin != 2 :
      print(f"Tidak ada jenis jin bernomor “{nomor_jin}”!")
    else :
      break
  
  if nomor_jin == 1 :
    print(" Memilih jin “Pengumpul”.")
    username = input("Masukkan username jin: ")
    while True : 
      if validasi_search(users,username) != -1 : 
        print(f"Username {username} sudah diambil!")
      else : 
        print("Masukkan password jin: ")
        password = input("Masukkan password jin: ")
        if len(password) < 5 or len(password) > 25 : 
          print("Password panjangnya harus 5-25 karakter!")
        else : 
          pass
        

  elif nomor_jin == 2 :
    print("Memilih jin “Pembangun”.")  
    username = input("Masukkan username jin: ")
    while True : 
      if validasi_search(users,username) != -1 : 
        print(f"Username {username} sudah diambil!")
      else : 
        print("Masukkan password jin: ")
        password = input("Masukkan password jin: ")
        if len(password) < 5 or len(password) > 25 : 
          print("Password panjangnya harus 5-25 karakter!")
        else : 
          pass
