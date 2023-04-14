import argparse 
import os
from globals import *

def load_folder() -> None : 
    parser = argparse.ArgumentParser()
    parser.add_argument("nama_folder", help= "validasi nama folder", nargs = '?', default = "")
    arg = parser.parse_args()
    folder = arg.nama_folder
    if folder == "" : 
        print("Tidak ada nama folder yang diberikan!")
        print("Usage: python main.py <nama_folder>")
        quit()
    elif os.path.isdir("./file_external/" + folder) :
        print("Loading...")
        load(folder,"user.csv", users)
        load(folder,"candi.csv", candi)
        load(folder,"bahan_bangunan.csv", bahan_bangunan)
        print("Selamat datang di program “Manajerial Candi”")
        print("Silakan masukkan username Anda")
    else : 
        print(f'Folder {folder} tidak ditemukan.')
        quit()

def splitline(line : str , separator : str) -> list : 
    result = [0 for i in range(1000)]
    temp = ""
    idx = 0
    for i in range(len(line)):
        if line[i] == separator or line[i] == '\n':
            result[idx] = temp
            temp = ""
            idx += 1
        else:
            temp += line[i]
    return [result[i] for i in range(idx)]

def load(folder : str , file : str, matrix : list) -> list : 
    f =  open("./file_external/" + folder + "/" + file ,'r')
    line_count = 0
    for line in f:
        if line_count > 0:
            ans  = splitline(line, ';')
            matrix[line_count-1] = ans
        line_count += 1
    f.close()
    return matrix




