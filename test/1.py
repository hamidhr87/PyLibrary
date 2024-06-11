# pip install pond-library==0.0.1
from PondLibrary.PondLibrary import PondLibrary

username = input("Please Enter Username: ")
password = input("Please Enter Password:")
obj = PondLibrary(username, password)

file_name = "3.txt"
domain_name = "domain1"
datasource_name = "hamid"
content = obj.download_file(domain_name, datasource_name, file_name)
with open(file_name, "wb") as file:
    file.write(content)

message = obj.upload_file("domain1","hamid","bucket","33.txt")
print(message)
