from links import tTwo_infile


def lines():
    with open(tTwo_infile) as file:
        line = sum(1 for line in file)
    return line


def columns():
    with open(tTwo_infile) as file:
        for line in file:
            column = ([int(x) for x in line.split()])
            break
    return len(column)
