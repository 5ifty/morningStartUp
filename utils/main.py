import os
import subprocess


def Batch():

    os.startfile('bat.bat')
    print(subprocess.check_output("bat.bat"))
    return Batch()

if __name__ == "__main__":
    Batch()
