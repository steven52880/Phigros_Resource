import os
import csv
import math

def mdstr(str):
    str = str.replace("\\", "\\\\")
    str = str.replace("|", "\|")
    return str

def generate_md(songinfo, mdfilename):
    # generate markdown
    with open(mdfilename+".md", "w", encoding="utf-8") as mdfile:
        mdfile.write("""# Songs
- [default order](default.md)  
- [sort by songname](songname.md)  
- [sort by difficulty(EZ)](difficulty_ez.md)  
- [sort by difficulty(HD)](difficulty_hd.md)  
- [sort by difficulty(IN)](difficulty_in.md)  
- [sort by difficulty(AT)](difficulty_at.md)  
  
| Song  | Artist   | EZ   | HD   | IN   | AT   |  
| ----- | -------- | ---- | ---- | ---- | ---- |  
""")
        for filename in songinfo:
            song = songinfo[filename]
            songname = song["songname"]
            artist = song["artist"]
            filename = song["filename"]
            mdfile.write(f"| {mdstr(songname)} | {mdstr(artist)} |")
            for level in song["difficulty"]:
                levelstr = f"{level} ({song['difficulty'][level]}) Lv.{math.floor(float(song['difficulty'][level]))}"
                mdfile.write(f" [{levelstr}](zip/{filename}_{level}.zip) |  ")
            mdfile.write("\n")
    """
    with open(mdfilename+".html", "w", encoding="utf-8") as htmlfile:
        mdfile = open(mdfilename+".md", "r", encoding="utf-8")
        htmlfile.write(markdown.markdown(mdfile.read()))
    """

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
            songinfo[filename]["difficulty"]["EZ"] = float(row[1])
            songinfo[filename]["difficulty"]["HD"] = float(row[2])
            songinfo[filename]["difficulty"]["IN"] = float(row[3])
            if len(row) == 5:
                songinfo[filename]["difficulty"]["AT"] = float(row[4])

    # create dir
    os.makedirs("md", exist_ok=True)
    # default order
    generate_md(songinfo, "md/default")
    # sort by songname
    songinfo_sorted = dict(sorted(songinfo.items(), key=lambda x: x[1]["songname"]))
    generate_md(songinfo_sorted, "md/songname")
    # sort by difficulty(EZ) (reverse order)
    songinfo_sorted = dict(sorted(songinfo.items(), key=lambda x: x[1]["difficulty"]["EZ"], reverse=True))
    generate_md(songinfo_sorted, "md/difficulty_ez")
    # sort by difficulty(HD) (reverse order)
    songinfo_sorted = dict(sorted(songinfo.items(), key=lambda x: x[1]["difficulty"]["HD"], reverse=True))
    generate_md(songinfo_sorted, "md/difficulty_hd")
    # sort by difficulty(IN) (reverse order)
    songinfo_sorted = dict(sorted(songinfo.items(), key=lambda x: x[1]["difficulty"]["IN"], reverse=True))
    generate_md(songinfo_sorted, "md/difficulty_in")
    # sort by difficulty(AT) (reverse order)
    songinfo_sorted = dict(sorted(songinfo.items(), key=lambda x: x[1]["difficulty"]["AT"] if "AT" in x[1]["difficulty"] else 0, reverse=True))
    generate_md(songinfo_sorted, "md/difficulty_at")