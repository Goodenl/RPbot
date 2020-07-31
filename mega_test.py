import os
from mega import Mega

mega = Mega()

m = mega.login("dadan.yanickii@gmail.com", "6453123m")

path_to_write = os.getenv("RP_PATH")
episod_number = "Episod 1"


folder = m.find('Episod 1')
print(folder)
file = m.upload(f"{path_to_write}{episod_number}\\temp.txt", folder[0])