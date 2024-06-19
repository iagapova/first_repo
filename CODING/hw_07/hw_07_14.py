def to_indexed(source_file, output_file):
    with open(source_file, 'r') as fh:
        result = []
        i = 0
        lines = fh.readlines()
        for line in lines:
            # print(line)
            line = str(i) + ': ' + line
            i += 1
            result.append(line)
        ttt = ''.join(result)

    with open(output_file, 'w') as fh:
        fh.write(ttt)
