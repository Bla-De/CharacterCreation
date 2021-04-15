from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.types import AuthScope

from twitchAPI.pubsub import PubSub
from uuid import UUID
from pprint import pprint

import json

with open('TwitchSettings.json','r') as f:
    twitchSettings = json.load(f)

# Need to read and update channel redemptions
scopes = [AuthScope.CHANNEL_READ_REDEMPTIONS,AuthScope.CHANNEL_MANAGE_REDEMPTIONS]

twitch = Twitch(twitchSettings["TwitchAppId"],app_secret=None,authenticate_app=False,target_app_auth_scope=scopes)
auth = UserAuthenticator(twitch, scopes, force_verify=False)

# this will open your default browser and prompt you with the twitch verification website
token, refresh_token = auth.authenticate()

# add User authentication
twitch.set_user_authentication(token, scopes, refresh_token)
user_id = twitch.get_users()

def channel_points(uuid: UUID, data: dict) -> None:
    print('got callback for UUID ' + str(uuid))
    pprint(data)

# starting up PubSub
pubsub = PubSub(twitch)
pubsub.start()
# you can either start listening before or after you started pubsub.
uuid = pubsub.listen_channel_points(user_id, channel_points)