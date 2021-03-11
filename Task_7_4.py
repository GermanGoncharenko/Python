import os
from collections import defaultdict
from os.path import relpath

import django

dir_path = 'my_project'
django_files = defaultdict(list)
for root, dirs, files in os.walk(dir_path):
   for file in files:
       ext = file.rsplit('.', maxsplit=1)[-1].lower()
       rel_path = relpath(os.path.join(root, file), dir_path)
       django_files[ext].append(rel_path)

for ext, files in sorted(django_files.items(),
                        key=lambda x: len(x[1]), reverse=True):
   print(f'{ext}: {len(files)}')

print('\nPY FILES')
print(*sorted(django_files['py'])[:10], sep='\n')
