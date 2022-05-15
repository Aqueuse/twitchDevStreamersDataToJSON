import datetime


def write_log(log_message):
    time_now = datetime.datetime.now()
    log_file = open("log.txt", "a")

    log_message = "[" + str(time_now.strftime("%d-%m-%Y %H:%M:%S")) + "] " + str(log_message)+"\n"
    print(log_message)
    log_file.write(log_message)
    log_file.close()
