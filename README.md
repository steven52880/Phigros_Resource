# Phigros_Resource
本项目可从Phigros的apk文件获取资源

资源包括

定数，收藏品id对应中文标题，头像id，tips

曲id，曲名，曲师，画师，谱师

头像图片，谱面文件，曲子音乐文件，曲绘(模糊)，曲绘(低质量)，曲绘
# 介绍

`gameInformation.py`可从apk获取定数表，tips，收藏品id，头像id，曲id，曲名，曲师，画师，谱师

定数表输出为difficulty.csv，收藏品输出为collection.csv，头像输出为avatar.txt，tips输出为tips.txt，其余输出为info.csv

`resource.py`依赖difficulty.csv和avatar.csv，从apk内解压出头像、谱面、曲绘、音乐资源，为png，wav，json

# 配置文件 config.ini
```ini
[TYPES]
avatar = true
Chart = true
illustrationBlur = true
illustrationLowRes = true
illustration = true
music = true
[UPDATE]
# 主线
main_story = 0
# 单曲和合集
other_song = 0
# 支线
side_story = 0
```
TYPES section为设定你需要哪些种类的资源，见README.md开头

当UPDATE section全为0时，默认获取全部歌曲的资源

当UPDATE section不是全为0时，会通过difficulty.csv获取最近的歌曲，当Phigros更新时使用，更新了哪个部分，更新了几首，运行resource.py时只会提取最近几首的资源
# 使用示例
安装所需的库(如果手动安装请注意pyfmodex<=0.7.0)
```shell
pip install -r requirement.txt
```
taptap下载的apk
```shell
pip3 install UnityPy
git clone --depth 1 https://github.com/7aGiven/PhigrosLibrary_Resource/
cd PhigrosLibrary_Resource
python3 gameInformation.py Phigros.apk
python3 resource.py Phigros.apk
```
https://616.sb下载的apk和obb
```shell
pip3 install UnityPy
git clone --depth 1 https://github.com/7aGiven/PhigrosLibrary_Resource/
cd PhigrosLibrary_Resource
python3 gameInformation.py Phigros.apk
python3 resource.py Phigros.obb
```
