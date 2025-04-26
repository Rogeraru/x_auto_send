import settings
import random
import os


def choose_rdn_img() -> str:
    folder_path = settings.post_img_dir_path
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    img_path = random.choice(files)
    post_img_path= img_path
    return post_img_path


def sent_img_recording(post_img_path):
    record_path = "./posted_img_record.txt"
    with open(record_path, "a", encoding="utf-8") as f:
        f.write(post_img_path + "\n")
