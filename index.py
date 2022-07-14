from datetime import datetime
import schedule
import time
from utils.main import Batch



def countDown():
    localTime = datetime.now()
    actionTime = localTime.strftime("%H:%M")
    print(actionTime)
    if actionTime == "08.30":
        b = Batch()
        schedule.every().day.at("08:30").do(b)
        return
    while True:
        schedule.run_pending()
        time.sleep(1)
        pass


if __name__ == "__main__":
    countDown()
