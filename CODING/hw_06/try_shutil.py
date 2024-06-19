import shutil
from pathlib import Path

source_file = '/Users/irina.agapova/Downloads/111/vpn_111.png'
destination_folder = 'Users/12345'

source_path = Path(source_file)
print(source_path)  # => /Users/irina.agapova/Downloads/111/vpn_111.png
print(source_path.parent)  # => /Users/irina.agapova/Downloads/111/
print(source_path.name)  # => vpn_111.png
print(source_path.suffix)  # => .png
destination_path = Path(destination_folder) / \
    source_path.name  # => Users/12345/vpn_111.png

print(destination_path)

print('-----------')


def appendix(file):
    return file.with_name(f"{file.stem}_1").with_suffix(file.suffix)

    # path = file.parent
    # name = file.stem + '_1'
    # suffix = file.suffix
    # return path.joinpath(name + suffix)


my_path = Path(
    '/Users/irina.agapova/Downloads/12345/SORTED/DOCUMENTS/Praktichna_robota__3.pdf')
print(appendix(my_path))

my_list = ['.asc', '.woff2', '.aif', '.scpt', '.torrent', '.DOC#', '.mjs', '.dat', '.pka', '.cdm', '.mom', '.xods', '.ppt', '.reg', '.otf', '.docm', '.pages', '.odc', '.wasm', '.tmLanguage', '.h', '.yml', '.ps1', '.bin', '.xml', '.woff', '.swift', '.tgz',
           '.xlsm', '.ts', '.swf', '.xodt', '.car', '.numbers', '.aiff', '.opf', '.asar', '.node', '.modulemap', '.xlsb', '.tif', '.exe', '.omo', '.strings', '.entitlements', '.docxx', '.nib', '.dylib', '.docx#', '.pcapng', '.xmind', '.zsh', '.ncx', '.odt#']
print(sorted(my_list))
