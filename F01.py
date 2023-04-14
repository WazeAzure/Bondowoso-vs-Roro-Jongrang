from globals import *

def login() -> None : 
  username = input("Username: ")
  password  = input("Password: ")
  i = 0
  while i < Nmax and users[i] != [Mark for i in range(3)] : 
    if users[i][idx_username] == username and users[i][idx_password] == password: 
      print(f"Selamat datang, {username}!")
      print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
      global user_id
      user_id = i 
      return
    elif users[i][idx_username] == username and users[i][idx_password] != password:
      print("Password salah")
      return
    i += 1
  print("\nusername tidak terdaftar")