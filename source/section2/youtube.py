import os
import subprocess

import pytube

yt = pytube.YouTube("https://www.youtube.com/watch?v=CTRO5NXmAp8")

videos= yt.streams.all()

 # print('videos',videos)

for i in range(len(videos)): # 다운로드 type 모두 출력
    print(i,', ',videos[i])

parent_dir = "D:/BIG_DATA/youtube/"
videos[0].download(parent_dir) # 화질이 제일 좋은 0번을 선택해서 저장
