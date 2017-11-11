# !/usr/bin/env python
# coding: utf-8

'''
my_grep.pyのモジュールだよ。
'''

from my_grep import *
#################### FINDの処理 ####################
def searchName(thing):
    ### ファイル名に検索語が含まれてたらTrueを返す ###
    if RE == 1:
        if CS == 0:
            reFW = re.compile(FW, re.IGNORECASE)
            if re.findall(reFW, thing):
                return True                     # 正規表現使う 大文字小文字区別なし
        else:
            if re.search(FW, thing):
                return True                     # 正規表現使う 大文字小文字区別する
    else:
        if CS == 0:
            reFW = re.compile(FW, re.IGNORECASE)
            if re.findall(reFW, thing):
                return True                     # 正規表現使わない 大文字小文字区別なし
        else:
            if FW in thing:
                return True                     # 正規表現使わない 大文字小文字区別する

def searchText(find, path, yeah):
    ### ファイルのテキストに検索語が含まれてたらパスとその行が書かれた文字列を返す ###
    fopen = open(path, encoding="utf-8")
    lines = fopen.readlines()
    fopen.close()
    for i in range(len(lines)):
        if RE == 1:
            if CS == 0:
                reFW = re.compile(FW, re.IGNORECASE)
                if re.findall(reFW, lines[i]):
                    find += "    [%d] %s" % (i+1, lines[i])
                    yeah  = True                # 正規表現使う 大文字小文字区別なし
            else:
                if re.search(FW, lines[i]):
                    find += "    [%d] %s" % (i+1, lines[i])
                    yeah  = True                # 正規表現使う 大文字小文字区別する
        else:
            if CS == 0:
                reFW = re.compile(FW, re.IGNORECASE)
                if re.findall(reFW, lines[i]):
                    find += "    [%d] %s" % (i+1, lines[i])
                    yeah  = True                # 正規表現使わない 大文字小文字区別なし
            else:
                if lines[i].find(FW) >= 0:
                    find += "    [%d] %s" % (i+1, lines[i])
                    yeah  = True                # 正規表現使わない 大文字小文字区別する
    return(find, yeah)

def searchFile(thing, path):
    ### もし検索語が含まれてたら、パスとその行が書かれた文字列を返す ###
    yeah = False
    find = "%s\n" % path
    if NAME == 1:                       # ファイル名検索するなら続行する
        yeah = searchName(thing)
    if os.path.isfile(path):            # それがファイルなら開いて検索する
        find, yeah = searchText(find, path, yeah)
    if yeah == True:
        return find
