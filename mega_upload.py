import os
from mega import Mega


email = os.getenv("Mega_EMAIL")
passw = os.getenv("Mega_PASSWORD")
#get files position
path_to_write = os.getenv("RP_PATH")
episod_number = "Episod 1"

mega = Mega()
m = mega.login(email, passw)


# find folder and upload file
def upload_on_cloud():
	folder = m.find('Episod 1')

	file = m.upload(f"{path_to_write}{episod_number}\\temp.txt", folder[0])

	#delet prevers update
	f = m.find(filename="temp.txt")
	last_update = m.get_link(f)
	try:
		print(last_update)
		m.delete_url(last_update)
	except:
		pass