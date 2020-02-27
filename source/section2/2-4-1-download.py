import os
import subprocess

import pytube

yt = pytube.YouTube("https://www.youtube.com/watch?v=WH7xsW5Os10")
vids= yt.streams.all()


for i in range(len(vids)): # 다운로드 type 모두 출력
    print(i,', ',vids[i])

vnum = int(input("다운 받을 화질을 입력하세요(0~21) : "))

parent_dir = "D:\BIG_DATA\youtube"
vids[vnum].download(parent_dir)

new_filename = input("변환할 MP3 파일명을 입력하세요 : ")

default_filename = vids[vnum].default_filename
subprocess.call(['ffmpeg', '-i',                 #cmd 실행 가능한 명령어 모두 사용가능
    os.path.join(parent_dir, default_filename),
    os.path.join(parent_dir, new_filename)
])

print('동영상 다운로드 및 mp3 Convert 완료!')
