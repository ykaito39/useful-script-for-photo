#Twitterでとってきた_largeつき画像のファイル名を直すプログラム
#作った人:ykaito39

# coding: UTF-8
import sys
import os

#デフォルトのディレクトリ
#この中に入っている画像が対象
if len(sys.argv) == 2:
    DIR == sys.argv[1]
elif os.name == 'nt':
    # DIR = 'C:\\Users\\' + os.getlogin() + '\\Downloads\\' #書き換えてください
    DIR = './'
else:
    DIR = '~/Downloads/'

#ディレクトリ内のファイル一覧を取得
#DIRが不正ならここで終了する
try:
    file_list = os.listdir(DIR)
except os.error:
    exit(-1)

for file in file_list:
    print(file)
    if file[-6:] == '_large':
        #変更対象のフルパスを取得
        full_path = os.path.join(DIR, file)

        #ファイル名から末尾の_largeを消す
        replaced_path = file[:-6] + ''
        replaced_full_path = os.path.join(DIR, replaced_path)

        #ファイル名の書き換え
        os.rename(full_path, replaced_full_path)
        print('[REPLACE]  ' + file + ' >> ' + replaced_path)
