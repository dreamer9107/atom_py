import os
import subprocess

import pytube

yt = pytube.YouTube("https://youtu.be/CTRO5NXmAp8")
vids= yt.streams.all()


for i in range(len(vids)): # 다운로드 type 모두 출력
    print(i,', ',vids[i])


parent_dir = "D:/youtube"
vids[0].download(parent_dir)



print('동영상 다운로드 완료!')
