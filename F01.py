from globals import *
import globals


def login() -> None :
  if globals.user_id == -1 : 
    username = input("Username: ")
    password  = input("Password: ")
    i = 0
    while i < Nmax and users[i] != [Mark for i in range(3)] :
      if users[i][idx_username] == username and users[i][idx_password] == password: 
        globals.user_id = i 
        print(f"Selamat datang, {username}!")
        print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
        return
      elif users[i][idx_username] == username and users[i][idx_password] != password:
        print("Password salah")
        return
      i += 1
    print("\nusername tidak terdaftar")
  else : 
      print("login gagal")
      print(f"Anda telah login dengan username {users[globals.user_id][idx_username]}. Silakan logout sebelum login kembali") 