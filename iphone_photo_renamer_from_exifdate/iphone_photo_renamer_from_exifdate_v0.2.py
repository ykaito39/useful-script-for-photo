######################################################################
#
# 知っているか..?
# iPhoneの画像ってIMG_XXXX.JPGの連番なんだぜ?
# これじゃ気づかないうちにファイル名がかぶっちまうよな......?
# ...
# そんなあなたにこのスクリプト!
# Python3.Xをインストールして、iphoneの画像があるフォルダで実行するだけ!!
# Exifかファイルの更新日時からファイル名を書き換えてくれます!!!!
# 
######################################################################


# -*- coding: utf-8 -*-
import os
import datetime
import pathlib
import re

from PIL import Image
from PIL.ExifTags import TAGS

import inspect #調べる

#対象画像フォルダとプログラム・カレントディレクトリの移動
#iphone_pic_dir = 'C:\\Users\\user\\Desktop\\pic3\\'
iphone_pic_dir = "./"
os.chdir(iphone_pic_dir)

def ShottimeFromExiftime(date_time_original_exif):
    return re.sub(r':', '', date_time_original_exif[:-9])

def GetFileUpdateDateTime(file_path):
    with pathlib.Path(file_path) as p:
        update_time = datetime.datetime.fromtimestamp(p.stat().st_mtime) #datetimeに変換
        return update_time.strftime("%Y%m%d")
    

for file_name in os.listdir(iphone_pic_dir):
    fullpath = iphone_pic_dir + file_name
    
    if not ("IMG_" == file_name[-12:-8]) & (file_name[-8:-4].isdecimal()):
        print(file_name + " is not a iPhone Photo.")
        continue
    
    ################################################################
    # shottime(ファイル名の先頭につくやつ)を決定する
    ################################################################
    #画像読み込みとEXIF読み込み
    try:
        with Image.open(file_name) as img:
            exif = img._getexif()
            
            #exifのデコード
            exif_table = {}
            for id, val in exif.items():
                tag = TAGS.get(id, id)
                #print(tag)
                exif_table[tag] = val
         
            if 'DateTimeOriginal' not in exif_table:
                #print("hoge")
                shot_time = GetFileUpdateDateTime(fullpath)
            else:
                shot_time = ShottimeFromExiftime(exif_table['DateTimeOriginal'])

    except OSError:
        continue
    except AttributeError:
        #更新日時をもとに日付を決定
        shot_time = GetFileUpdateDateTime(fullpath)
        
    ################################################################
    # ファイル名を書き換え
    ################################################################
    #もしも先頭にYYmmdd形式のファイル名記述があればパスする
    if file_name[6:].isdecimal():
        continue
    
    after_name = shot_time + "_" + file_name
    
    os.rename(fullpath, iphone_pic_dir + after_name)
    print(file_name + " > " + iphone_pic_dir + after_name)