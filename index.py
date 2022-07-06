from datetime import datetime
import schedule
import time
from utils import main


def countDown():
    localTime = str(datetime.now())
    hour = str(datetime.strptime(localTime, "%d %m %y %H %M").hour)
    minute = str(datetime.strptime(localTime, "%d %m %y %H %M").minute)
    convertedTime = (f"{hour}:{minute}")
    convertedTime == localTime
    while True:
        schedule.every().day.at("08:30").do(main())
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    countDown()
