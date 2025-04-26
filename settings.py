from configparser import ConfigParser

config = ConfigParser()
config.read('./config.ini')

post_msg = config.get('POST','message')
post_img_dir_path = config.get('PATH','img')