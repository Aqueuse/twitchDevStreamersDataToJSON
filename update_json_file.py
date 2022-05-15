import json


def update_file(actual_streamers_list):
    streamers = read_streamer_file_to_list()

    for actual_streamer in actual_streamers_list:
        if not is_streamer_exist(streamers, actual_streamer["name"]):
            new_streamer = {"name": actual_streamer["name"], "titles": [actual_streamer["titles"]]}
            streamers.append(new_streamer)
        else:
            streamers = update_streamer_titles(streamers, actual_streamer["name"], actual_streamer["titles"])

    write_file(json.dumps(streamers, indent=2))
    return len(actual_streamers_list)


def is_streamer_exist(actual_data, streamer_name):
    for streamer in actual_data:
        if streamer["name"] == streamer_name:
            return True
    return False


def update_streamer_titles(streamers, username, title):
    for streamer in streamers:
        if streamer["name"] == username:
            streamer["titles"].append(title)
    return streamers


def read_streamer_file_to_list():
    streamers_file = open("./streamers.json", "r", encoding='utf-8')
    data = json.load(streamers_file)
    return data


def write_file(streamers_dict):
    streamers_json = open("streamers.json", "w")
    streamers_json.write(streamers_dict)
    streamers_json.close()
