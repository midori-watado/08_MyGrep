# !/usr/bin/env python
# coding: utf-8

'''MyGrep

ぶっちゃけこれよりスゴイことがsublime text3のgrep機能でできる。
ただ作ってみたかったので作った。

========================================
バージョン1.0(2016-01-14)
    完成。
バージョン1.1(2017-09-26)
    docとかつけた。
    モジュール同士でimportしてるのになんで動くんだ、これ??
'''

RE   = 0   # 1にすると正規表現ON
CS   = 0   # 1にすると大文字小文字区別ON
FIND = 1   # 1にすると検索結果を一覧に出す
REPL = 0   # 1にすると置換する
NAME = 0   # 1にするとファイル名・フォルダ名も検索あるいは置換する

DIR  = "/Users/username/Desktop/targetFolder"   # 末尾にスラッシュ入れないこと
FW   = "search words"
RW   = ""
EXT  = [".jpg", ".tpl", ".png", ".tmp"]   # 対象にしないファイル拡張子

import os, re
import sys, traceback
import my_grep_searchFile as s
import my_grep_replaceFile as r

def makeDirs():
    ### 全ディレクトリのパスをdirsに格納する ###
    dirs = []
    dirs.append(DIR)
    for directory in dirs:
        files = os.listdir(directory)
        for f in files:
            path = directory + "/" + f
            if os.path.isdir(path):
                dirs.append(path)
    return dirs

def checkExt(path):
    ### ハブく拡張子だったらTrueを返す ###
    root, ext = os.path.splitext(path)
    if ext in EXT:
        return True
    else:
        return False

### FINDが1だったときやること ###
def find(dirs):
    finds   = []
    errorsF = []
    for directory in dirs:
        things = os.listdir(directory)
        for thing in things:
            path = directory + "/" + thing
            try:
                if not checkExt(path):                   # 指定した拡張子が含まれてなければ続行
                    find = s.searchFile(thing, path)     # 見つからないときはNoneが返ってくる
                    if find:                             # ワードが見つかったなら続行
                        find = find[:-1]
                        finds.append(find)
            except Exception as e:
                # この部分は、このスクリプトそのものをデバックするときONにしてね
                # info = sys.exc_info()
                # tbinfo = traceback.format_tb(info[2])
                # for tbi in tbinfo:
                #     print(info[1])
                #     print(tbi)
                # exit()
                errorsF.append("%s\n    %s" % (path, e))
    print("検索結果は")
    if not finds:
        print("アリマセン。")
    else:
        for find in finds:
            print(find)
    print("\n検索でエラーが出たファイルは")
    if not errorsF:       print("アリマセン。")
    for error in errorsF: print(error)

### REPLが1だったときやること ###
def repl(dirs):
    dirs.reverse()
    repls   = []
    errorsR = []
    for directory in dirs:
        things = os.listdir(directory)
        for thing in things:
            path = directory + "/" + thing
            try:
                if not checkExt(path):
                    repl = r.replaceFile(directory, thing)
                    if repl:
                        repl = repl[:-1]
                        repls.append(repl)
            except Exception as e:
                # この部分は、このスクリプトそのものをデバックするときONにしてね
                # info = sys.exc_info()
                # tbinfo = traceback.format_tb(info[2])
                # for tbi in tbinfo:
                #     print(info[1])
                #     print(tbi)
                # exit()
                errorsR.append("%s\n    %s" % (path, e))
    print("置換結果は")
    if not repls:
        print("アリマセン。")
    else:
        repls.reverse()
        for repl in repls:
            print(repl)
    print("\n置換でエラーが出たファイルは")
    if not errorsR:
        print("アリマセン。")
    else:
        errorsR.reverse()
        for error in errorsR:
            print(error)

def main():
    ### これがトップレベル関数だよ ###
    dirs    = makeDirs()
    if FIND == 1:
        find(dirs)
    if REPL == 1:
        repl(dirs)

if __name__ == "__main__":
    main()
