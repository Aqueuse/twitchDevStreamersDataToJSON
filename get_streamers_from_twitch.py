from twitchAPI.twitch import Twitch
twitch = Twitch('clientId', 'secret')


def get_streamers():
    data = twitch.get_streams(game_id=["1469308723"], language=["fr"])
    streamers_list = []
    for streamer in data["data"]:
        streamers_list.append({"name": streamer["user_name"], "titles": streamer["title"]})
    return streamers_list
