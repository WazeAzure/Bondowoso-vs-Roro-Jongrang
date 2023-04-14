from globals import *
from F01 import login
from F02 import logout

# Menerima masukan 
def run(masukan : str) -> None : 
  # Fitur yang dapat diakses semua user
  if masukan == "quit" : 
     quit()
  elif masukan == "login" : 
    if user_id == -1 : 
      login()
    else : 
      print("login gagal")
      print(f"Anda telah login dengan id {user_id}. Silakan logout sebelum login kembali")
  elif masukan == "logout" : 
    if user_id != -1 : 
      logout()
    else : 
      print("Logout gagal!")
      print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
  elif masukan == "save" :
    save()
  elif masukan == "help" : 
    help()

  # Fitur yang dapat diakses bandung_bondowoso
  if id != -1 : 
    if users[user_id][idx_role] == "bandung_bondowoso" : 
        if masukan == "summonjin" :
            summonjin()
        elif masukan == "hapusjin" :
            hapusjin()
        elif masukan == "ubahjin" :
            ubahjin()
        elif masukan == "batchkumpul" :
            batchkumpul()
        elif masukan == "batchbangun" :
            batchbangun()
        elif masukan == "laporanjin" :
            laporanjin()
        elif masukan == "laporancandi" :
            laporancandi()

  # Fitur yang dapat diakses roro_jongrang
    if users[user_id][idx_role] == "roro_jongrang" : 
        if masukan == "hancurkancandi" :
            hancurkancandi()
        elif masukan == "ayamberkokok" :
            ayamberkokok()

  # Fitur yang dapat diakses jin_pengumpul
    if masukan == "kumpul" :
        kumpul()

  # Fitur yang dapat diakses jin_pembangun
    if masukan == "bangun" :
        bangun()
  else : 
     print("Kamu tidak dapat mengakses fitur ini ")
