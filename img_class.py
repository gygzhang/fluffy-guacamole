from read_brainweb import read_brainweb

#for training set ... not complete
if __name__ == "__main__":
    src = ""
    read_brainweb("trainning set","D:\ml\\brainweb\phantom_1.0mm_normal_crisp.rawb",85)
    read_brainweb("test set", "D:\ml\\brainweb\phantom_1.0mm_normal_crisp.rawb", 87)
