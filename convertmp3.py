import os
# walk through music folder
srcdir = "music"
dstdir = "music_mp3_128k"
if not os.path.exists(dstdir):
    os.makedirs(dstdir)
for root, dirs, files in os.walk(srcdir):
    for file in files:
        print(file)
        # convert to mp3
        stem, ext = os.path.splitext(file)
        if ext != ".wav":
            continue
        wavpath = os.path.join(root, file)
        mp3path = os.path.join(dstdir, stem + ".mp3")
        # check exist
        if os.path.exists(mp3path):
            continue
        os.system(f"ffmpeg -i {wavpath} -ab 128k {mp3path}")
        print (f"ffmpeg -i {wavpath} -ab 128k {mp3path}")