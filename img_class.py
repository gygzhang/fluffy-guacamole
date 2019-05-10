from read_brainweb import read_brainweb
import os
import data_download
#for training set ... not complete
if __name__ == "__main__":
    src = ""
    #path = r"D:\\MLDLRL\\brainweb\\data_download\\"
    #print(os.listdir(os.getcwd()))
    if "dataset" not in os.listdir(os.getcwd()):
        os.mkdir(os.getcwd()+"\\dataset")
    data_download.download()
    #print(os.listdir(os.getcwd()+"\\dataset\\"))
    if "training set" not in os.listdir(os.getcwd()+"\\dataset"):
        os.mkdir(os.getcwd()+"\\dataset\\training set\\")
    if "test set" not in os.listdir(os.getcwd() + "\\dataset"):
        os.mkdir(os.getcwd() + "\\dataset\\test set\\")

    rfiles = os.listdir(path)
    #print(rfiles)
    for f in rfiles:
        for i in range(30):
            read_brainweb("dataset\\training set",path+f,i*3)
            read_brainweb("dataset\\test set", path+f, i*3+1)
