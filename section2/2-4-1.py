import os
import subprocess
import pytube
import sys


yt=pytube.YouTube("https://youtu.be/SlPhMPnQ58k")
vids=yt.streams.all()

for i in range(len(vids)):
    print(i,vids[i])

down_dir="D:/atom_py/section2/mp4/"

x=int(input("화질을 선택해라 1~21번까지 있다"))
vids[x].download(down_dir)


new_filename=input("저장할 파일의 이름을 입력해라")
new2=new_filename+".mp3"
default_filename=vids[x].default_filename
subprocess.call(['ffmpeg',"-i",os.path.join(down_dir,default_filename),os.path.join(down_dir,new2)])

print("동영상 다운로드 및 변환 완료")
print(new_filename)
