from read_brainweb import read_brainweb
import os
#for training set ... not complete
if __name__ == "__main__":
    src = ""
    path = r"D:\\MLDLRL\\brainweb\\data_download\\"
    rfiles = os.listdir(path)
    print(rfiles)
    for f in rfiles:
        for i in range(30):
            read_brainweb("training set",path+f,i*3)
            read_brainweb("test set", path+f, i*3+1)
