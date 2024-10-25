import os
import shutil

a = r"C:\Users\User\Documents"
b = "DOCS"
if not os.path.exists(b):
    os.mkdir(b)
for file_name in os.listdir(a):
    if file_name.endswith(".doc"):
        shutil.copy(os.path.join(a, file_name), b)
print("Файлы скопированы!")
