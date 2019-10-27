import os

for file in os.listdir('.'):
    if not file.startswith('VQA.zip') or file == 'VQA.zip.001':
        continue
    os.system(f'git add {file}')
    os.system("git commit -m 'add new file'")
    os.system('git push')
