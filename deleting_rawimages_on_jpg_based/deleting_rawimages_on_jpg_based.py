###################################################
# Title: RAW写真仕分けくん_v0.1
# Created by: ykaito39
# Description:
#  jpgとRaw画像が混在するディレクトリで、jpgのみ削除した後に
#  このスクリプトを実行することで同名のRawが消えます。
# Attention: 必ずバックアップをとってから実行してください。
###################################################

# -*- coding: utf-8 -*-

import sys
import os

#デフォルトのディレクトリ
#この中に入っている画像が対象
DIR = './'
if len(sys.argv) == 2:
    DIR == sys.argv[1]

#ディレクトリ内のファイル一覧を取得
#DIRが不正ならここで終了する
try:
    file_list_org = os.listdir(DIR)
except os.error:
    exit(-1)

file_list = sorted(file_list_org)

"""
#実験コード:ファイルを消すとリストの中はどうなるのか...?
print(file_list)

print(file_list[0] + "を削除します。")
os.remove(os.path.abspath(file_list[0]))
"""  
print(file_list) #:List内には居座ったまま


"""
print(file_list[1][-3:]) #:"RAF"
"""


"""
tmp = ""
for file_name in file_list:
    if file_name[-3:] == ".py":
        continue
    
    if (file_name[:-4] == tmp) or ( file_name[:-4]+".RAF" in file_list ):
        print(file_name[:-4] + "は2つあるよ!さくじょしないよ")
    else:
        print(file_name + "は一個しか無いから削除します(無慈悲)。")
        #os.remove(os.path.abspath(file_list[i]))
    tmp = file_name[:-4]
    
"""
print(file_list[0][-3:])

#とりあえず動くけど本当にクソコードですありがとうございました。
i = 0
while True:
    #print(i) #:0~N
    
    try:
        if file_list[i][-3:] == ".py":
            i += 1
            continue
    except IndexError:
        break

    if file_list[i][:-4] == file_list[i+1][:-4]:
        print("削除非対象:" + file_list[i] + " " + file_list[i+1])
        i += 1 #なぜ足し算されない??? = i in range()はループ回数目毎にrangeを呼んでiに代入しているのでは...
    else: #RAFもJPEGも存在するやつは残しておく
        print("ファイル名不一致:" + file_list[i] + "を削除します。")
        os.remove(os.path.abspath(file_list[i]))
    
    if i == len(file_list):
        break
    
    i += 1
    
    
"""
for i in range(len(file_list)):
    print(i) #:0~N
    
    if file_list[i][-3:] == ".py":
        continue

    if file_list[i][:-4] == file_list[i+1][:-4]:
        print("削除非対象:" + file_list[i] + " " + file_list[i+1])
        i += 2 #なぜ足し算されない??? = i in range()はループ回数目毎にrangeを呼んでiに代入しているのでは...
    else: #RAFもJPEGも存在するやつは残しておく
        print("ファイル名不一致:" + file_list[i] + "を削除します。")
        #os.remove(os.path.abspath(file_list[i]))
    """        
#    except IndexError:
#        print("pass")
#        break
