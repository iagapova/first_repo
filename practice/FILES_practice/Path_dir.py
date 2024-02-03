from pathlib import Path

file_path = Path('test.txt')

print([m for m in dir(file_path) if not m.startswith('_')])

print()

print(Path.cwd())

print(Path('usr').joinpath('local').joinpath('bin'))
print(Path('usr') / 'local' / 'bin')

print(Path('CODING').exists())
print(Path('CODING').is_dir())
print(Path('CODING').is_file())
print(Path('files_1.py').exists())

print('--- check cwd ---')
cwd = Path('.')
print(cwd.absolute())
cwd1 = Path('/Users').joinpath('irina.agapova').joinpath('Documents').joinpath(
    'Projects').joinpath('My repo').joinpath('first_repo')
print(cwd1)
print(cwd1.exists())
cwd1 = Path('/Users').joinpath('irina.agapova').joinpath('Documents').joinpath(
    'Projects').joinpath('My repo').joinpath('first_repo').joinpath('DELME')
if not cwd1.exists():
    print(cwd1.mkdir())  # создаем папку
if cwd1.exists():
    print(cwd1.rmdir())  # удаляем папку
