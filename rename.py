import os
def rename_files():
#(1) get file names from the from the folder
file_list = os.listdir(r"C:\OOP\prank")
print(file_list)
#(2) for each file rename filename 
for file_name in file_list :
 os.rename(file_name,filename_transaltion(None,"0123456789")) 
 rename_files()
