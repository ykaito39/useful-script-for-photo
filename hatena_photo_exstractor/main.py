import os
import sys
import re
import requests
from tqdm import tqdm
import time

dst = os.path.join(os.path.dirname(__file__), "output")
patterns = [r"https://cdn\-ak\.f\.st\-hatena\.com/images/fotolife.*?\.png",
            r"https://cdn\-ak\.f\.st\-hatena\.com/images/fotolife.*?\.gif",
            r"https://cdn\-ak\.f\.st\-hatena\.com/images/fotolife.*?\.jpg",
            r"https://cdn\-ak\.f\.st\-hatena\.com/images/fotolife.*?\.webp",
            r"https://cdn\-ak\.f\.st\-hatena\.com/images/fotolife.*?\.jpeg",
            r"https://cdn\-ak\.f\.st\-hatena\.com/images/fotolife.*?\.svg",
            r"https://cdn\-ak\.f\.st\-hatena\.com/images/fotolife.*?\.ico"]

def get_dir_size(path='.'):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total


def main():
    with open(sys.argv[1]) as f:
        text = f.read()

    matched = []
    for p in patterns:
        try:
            matched.extend( re.findall(p, text) )
        except:
            continue

    print(f"matched url: {len(matched)}")
    print(f"set: {len(set( matched ))}")

    i = input("Would you like to dwonload?[y/n]: ")
    if not(i in ["y", "yes", "Yes", "YES"]):
        print("download canseled")
        exit()
    else:
        # extract item not downloaded
        #target = [url.split("/")[-1] for url in matched]
        downloaded = os.listdir(dst)
        #list( set(target) - set(downloaded) )

        # download
        for url in tqdm(matched):
            if url.split("/")[-1] in downloaded:
                continue

            time.sleep(1)
            d = requests.get(url).content

            if not os.path.exists(dst):
                os.mkdir(dst)

            with open(os.path.join(dst, url.split("/")[-1]), mode="wb") as f:
                f.write(d)

    print ("total: " + str ( get_dir_size(dst) / 1000000 ) + " MB" )

if __name__ == "__main__":
    while(True):
        try:
            main()
        except:
            continue