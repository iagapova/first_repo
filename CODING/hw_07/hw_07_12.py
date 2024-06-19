def file_operations(path, additional_info, start_pos, count_chars):
    with open(path, 'a') as fh:
        fh.write(additional_info)

    with open(path, 'r') as fh:
        cont = fh.read()  # получаем контент файла
        # режем контент с указанной позиции по нужной длине
        return cont[fh.seek(start_pos): fh.seek(start_pos) + count_chars]
