from pathlib import Path

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