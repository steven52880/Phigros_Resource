import os
import zipfile
import csv
import math

# main
if __name__ == "__main__":
    # make new dirs
    os.makedirs("temp", exist_ok=True)
    os.makedirs("zip", exist_ok=True)
    # read info.csv
    songinfo = {}
    with open("info.csv", "r", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter="\\")
        for row in reader:
            info = {}
            info["filename"] = row[0]
            info["songname"] = row[1]
            info["artist"] = row[2]
            info["illustrator"] = row[3]
            info["charter"] = {}
            info["charter"]["EZ"] = row[4]
            info["charter"]["HD"] = row[5]
            info["charter"]["IN"] = row[6]
            if len(row) == 8:
                info["charter"]["AT"] = row[7]
            songinfo[info["filename"]] = info
    # read difficulty.csv
    with open("difficulty.csv", "r", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            filename = row[0]
            songinfo[filename]["difficulty"] = {}
            songinfo[filename]["difficulty"]["EZ"] = row[1]
            songinfo[filename]["difficulty"]["HD"] = row[2]
            songinfo[filename]["difficulty"]["IN"] = row[3]
            if len(row) == 5:
                songinfo[filename]["difficulty"]["AT"] = row[4]
    # pack each song
    for filename in songinfo:
        song = songinfo[filename]
        print(song)
        for level in song["difficulty"]:
            # filename and dirs
            csv_file = "info.csv"
            chart_file =  f"{filename}.0.json"
            music_file = f"{filename}.mp3"
            illustration_file = f"{filename}.jpg"
            zip_file = f"{filename}_{level}.zip"

            csv_dir = os.path.join("temp",csv_file)
            chart_dir = os.path.join(f"Chart_{level}", chart_file)
            music_dir = os.path.join("music_mp3_128k", music_file)
            illustration_dir = os.path.join("illustration_jpg", illustration_file)
            zip_dir = os.path.join("zip", zip_file)
            # write info.csv
            # ,Chart,Music,Image,Name,Artist,Level,Illustrator,Charter,AspectRatio,NoteScale,GlobalAlpha
            with open(csv_dir, "w", encoding="utf-8", newline="") as csvfile:
                writer = csv.writer(csvfile)
                levelstr = f"{level} ({song['difficulty'][level]}) Lv.{math.floor(float(song['difficulty'][level]))}"
                writer.writerow(["Chart", "Music", "Image", "Name", "Artist", "Level", "Illustrator", "Charter", "AspectRatio", "NoteScale", "GlobalAlpha"])
                writer.writerow([chart_file, music_file, illustration_file, song["songname"], song["artist"], levelstr, song["illustrator"], song["charter"][level]])
            # print
            print(f"Pack {zip_file}...")
            # pack to zip (level:0)
            with zipfile.ZipFile(zip_dir, "w") as zf:
                zf.write(csv_dir, os.path.basename(csv_dir))
                zf.write(chart_dir, os.path.basename(chart_dir))
                zf.write(music_dir, os.path.basename(music_dir))
                zf.write(illustration_dir, os.path.basename(illustration_dir))