import schedule
import time
from datetime import datetime
from instagrapi import Client

print('[*] ---------------------------- insta-scheduler start...')

def post_job():
    str_time = datetime.now().strftime('%Y%m%d')
    file_path = "./" + str_time + "/job"
    
    print("[*] ---------------------------- day: ", str_time)
    with open(file_path, 'r') as job_file:
        lines = job_file.readlines()
        for job in lines:
            job_info = job.split('  ')
            id = job_info[0]
            password = job_info[1]
            img_path = job_info[2]
            msg = job_info[3]
            msg.replace('\\n', '\n')
            
            print('id": ', id, ' password: ', password, ' img_path: ', img_path)
            print('msg: ', msg)
    
            cl = Client()
            cl.login(id, password)

            media = cl.photo_upload(img_path, msg)
            print('media: ', media.dict())

schedule.every().day.at('07:00:00').do(post_job)

while True:
    schedule.run_pending()
    time.sleep(1)
