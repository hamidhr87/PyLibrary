# from PyLibrary.PyLibrary import PyLibrary
from PyLibrary.PyLibrary import PyLibrary

obj = PyLibrary("f.taheri", "1234")
content = obj.download_file("domain1","hamid","3.txt")
# with open("3.txt","wb") as file:
#     file.write(content)
# message = obj.upload_file("domain1","hamid","bucket","33.txt")
# print(message)
