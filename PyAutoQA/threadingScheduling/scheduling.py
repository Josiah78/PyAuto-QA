import schedule
import time

def helloWorld():
    print('Hello World')

schedule.every().day.at("19:11").do(helloWorld)
schedule.every(5).minutes.do(helloWorld)
schedule.every().hour.do()
schedule.every().monday.do()
schedule.every().monday.at("10:00").do()

while True:
    schedule.run_pending()
    time.sleep(1)