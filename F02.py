import globals

def logout() -> None :
   if globals.user_id != -1 :  
      globals.user_id = -1
      print("Anda telah logout")
   else : 
      print("Logout gagal!")
      print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")