from globals import *
import globals
from F01 import login
from F02 import logout

# Menerima masukan 
def run(masukan : str) -> None :
  # Fitur yang dapat diakses semua user
  if masukan == "quit" : 
     quit()
  elif masukan == "login" : 
     login()
  elif masukan == "save" :
     save()
  elif masukan == "help" : 
     help()
  elif masukan == "logout" : 
     logout()

  # Fitur yang dapat diakses bandung_bondowoso
  elif globals.user_id != -1 : 
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
    elif users[user_id][idx_role] == "roro_jongrang" : 
        if masukan == "hancurkancandi" :
            hancurkancandi()
        elif masukan == "ayamberkokok" :
            ayamberkokok()

  # Fitur yang dapat diakses jin_pengumpul
    elif masukan == "kumpul" :
        kumpul()

  # Fitur yang dapat diakses jin_pembangun
    elif masukan == "bangun" :
        bangun()
  else : 
     print('Masukan tidak valid. Silakan check daftar command menggunakan command "help" ')
