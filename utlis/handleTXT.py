

def readTxt(path):
    with open(path) as f:
        firstline = f.readline()
        lines = f.readlines()
    f.close()
    headers = firstline.strip().split(",")
    resultHeaders = list(map(lambda x: int(x), headers))
    resultLines = []
    for line in lines:
        prep = line.strip().split(",")
        line = list(map(lambda x: int(x), prep))
        resultLines.append(line)
    return ( resultHeaders,resultLines)