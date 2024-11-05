# 介绍
一个批量将图片转成视频的工具，可以一次性上传多张图片，然后将这些图片生成一个视频，而不是一张图片一个视频！

# 使用方法
如果你本机有Python环境的话，可以直接运行 `python ptv.py`
如果你想打包成exe并且分布到其他x64的windows机子上使用的话，可以使用下面命令来打包
```
pyinstaller --onefile --add-data "C:\Users\admin\Desktop\ffmpeg-2023-08-20-git-f0b1cab538-full_build\bin\ffmpeg.exe;." --add-data "C:\Users\admin\Desktop\testpic\icon.ico;." --add-data "C:\Users\admin\Desktop\qrcode.jpg;." --icon "icon.ico" ptv.py
```
# 其他
不会打包和运行？
那就直接下载我打包好的exe直接使用叭！
