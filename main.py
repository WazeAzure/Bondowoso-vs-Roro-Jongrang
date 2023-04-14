from data import load_folder
import command

load_folder()

while True:
  masukan = input(">>> ")
  command.run(masukan)