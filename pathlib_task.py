from pathlib import Path

p = Path('/Users/irina.agapova/Documents')  # p Вказує на теку /Users/irina.agapova/Documents
#for i in p.iterdir():
#    print(i.name)  # Виведе у циклі імена всіх тек та файлів у /Users/irina.agapova/Documents

def parse_folder(path):
    files = []
    folders = []
    for i in path.iterdir():
        if i.is_file():
            files.append(i.name)
        elif  i.is_dir():
            folders.append(i.name)
        
        
            
        
    print(files)
    print(folders)
    return files, folders

parse_folder(p)