import threading
import get_streamers_from_twitch
import update_json_file
from log import write_log


def repeat_each_hour():
    threading.Timer(3600.0, repeat_each_hour).start()
    try:
        data = get_streamers_from_twitch.get_streamers()
        streamers_number = update_json_file.update_file(data)
        write_log(str(streamers_number) + " streamers added !")
    except Exception as Argument:
        write_log(Argument)


if __name__ == '__main__':
    repeat_each_hour()
