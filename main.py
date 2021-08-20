import time
from datetime import datetime as dt
from datetime import date
import os
import threading

import Freiburg.collect_freiburg
import server

os.environ['MOZ_HEADLESS'] = '1'

# every hour
seconds_until_next_check = 60*60
daily_backup = False
last_backup = None

def wait(last_stamp):
    time_diff = dt.now() - last_stamp
    time_diff = time_diff.total_seconds()
    waiting_time = max(0, seconds_until_next_check-time_diff)
    time.sleep(waiting_time)

def run():
    # init
    should_running = True
    #offenburg_collector = collect.Collector()
    freiburg_collector = Freiburg.collect_freiburg.Collector()
    # run
    while should_running:
        last_stamp = dt.now()
        #offenburg_collector.run()
        freiburg_collector.run()
        print(f"\n- {dt.now()} collected data")
        create_backup(freiburg_collector)
        #wait(last_stamp)
        time.sleep(seconds_until_next_check)

def start_server():
    thread = threading.Thread(target=run)
    thread.start()

def create_backup(collector):
    global daily_backup, last_backup

    if last_backup != None:
        diff = date.today() - last_backup
        if diff.days >= 1:
            daily_backup = False

    if daily_backup == False:
        collector.create_backup()
        daily_backup = True
        last_backup = date.today()
        print(f"\n- {dt.now()} create backup")


if __name__ == '__main__':
    print(f"\n- {dt.now()} bot now online")
    server.start_server()
    run()