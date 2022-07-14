import subprocess
import time


def Batch():
    batchcli = subprocess.Popen(r"C:\Users\oem\Documents\Recent Code\Startup\utils\bat.bat")
    # print(subprocess.check_output(r"C:\Users\oem\Documents\Recent Code\Startup\utils\bat.bat"))
    # This is used for debugging the cmd script
    time.sleep(5)
    batchcli.kill()


if __name__ == "__main__":
    Batch()
