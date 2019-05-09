
def big2little(src,dst):
    stack = list()
    # print(""==bytes(0))
    byte = 0
    fs = open(dst, "wb")
    f = open(src, "rb")
    # == and is have g great difference
    while byte != b'':
        byte = f.read(1);
        stack.append(byte)
        byte = f.read(1);
        stack.append(byte);
        bw = stack.pop()
        fs.write(bw)
        bw = stack.pop()
        fs.write(bw)
    fs.close()
    f.close()