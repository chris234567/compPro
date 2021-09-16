def readFile(path):
    with open(path) as lines:
        lines = [list(map(int, line.replace("\n","").split(" "))) for line in lines.readlines()]

    return lines
