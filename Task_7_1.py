import os

dir_path = 'my_project'
box = ['settings', 'mainapp', 'adminapp', 'authapp']
if not os.path.exists(dir_path):
   os.mkdir(dir_path)
os.chdir(dir_path)
for i in range(4):
   if not os.path.exists(dir_path):
      os.makedirs(box[i])
