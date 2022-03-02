import time
from datetime import datetime as dt
from datetime import date
import os
import threading

import Freiburg.collect_freiburg

os.environ['MOZ_HEADLESS'] = '1'

# every hour
seconds_until_next_check = 60 * 60
daily_backup = False
last_backup = None
last_stamp = None



def wait(last_stamp):
    time_diff = dt.now() - last_stamp
    time_diff = time_diff.total_seconds()
    waiting_time = min(seconds_until_next_check,
                       seconds_until_next_check - time_diff)
    time.sleep(waiting_time)


def run():
    global last_stamp, seconds_until_next_check
    # init
    should_running = True
    #offenburg_collector = collect.Collector()
    freiburg_collector = Freiburg.collect_freiburg.Collector()
    # run
    while should_running:
        if last_stamp == None or (dt.now() - last_stamp).total_seconds(
        ) >= seconds_until_next_check:
            last_stamp = dt.now()
            #offenburg_collector.run()
            freiburg_collector.run()
            print(f"\n- {dt.now()} collected data")
            create_backup(freiburg_collector)
            #wait(last_stamp)
            #time.sleep(seconds_until_next_check)

            time.sleep(30)


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
	#server.start_server()
	run()
