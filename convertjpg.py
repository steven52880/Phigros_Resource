import os

srcdir = "illustration"
dstdir = "illustration_jpg"
if not os.path.exists(dstdir):
    os.makedirs(dstdir)
for root, dirs, files in os.walk(srcdir):
    for file in files:
        print(file)
        # convert to jpg
        stem, ext = os.path.splitext(file)
        if ext != ".png":
            continue
        pngpath = os.path.join(root, file)
        jpgpath = os.path.join(dstdir, stem + ".jpg")
        # check exist
        if os.path.exists(jpgpath):
            continue
        os.system(f"ffmpeg -i {pngpath} {jpgpath}")
        print (f"ffmpeg -i {pngpath} {jpgpath}")