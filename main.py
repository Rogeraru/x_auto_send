import yaml
from api import auth
import settings
creds = yaml.load(open('social_credentials.yml'), Loader=yaml.FullLoader)

client = auth.twit_connection(creds)
client_v1 = auth.twit_connection_v1(creds)

myMedia = r'C:\Users\User\Downloads\ComfyUI_windows_portable_nvidia\ComfyUI_windows_portable\ComfyUI\output\animate\NSFW\ComfyUI_temp_ripnk_00005_.png'

media = client_v1.media_upload(filename=myMedia)
media_id = media.media_id

msg = settings.post_msg
response = client.create_tweet(text = msg, media_ids = [media_id])
