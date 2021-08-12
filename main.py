import time
from datetime import datetime as dt
import collect
import collect_emmendingen

# every hour
seconds_until_next_check = 60*60

def wait(last_stamp):
    time_diff = dt.now() - last_stamp
    time_diff = time_diff.total_seconds()
    waiting_time = max(0, seconds_until_next_check-time_diff)
    time.sleep(waiting_time)

def run():
    # init
    should_running = True
    bad_krozingen_collector = collect.Collector()
    emmendingen_collector = collect_emmendingen.Collector()
    # run
    while should_running:
        last_stamp = dt.now()
        bad_krozingen_collector.run()
        emmendingen_collector.run()
        #wait(last_stamp)
        time.sleep(seconds_until_next_check)


if __name__ == '__main__':
    run()