# !/usr/bin/env python
# coding: utf-8

'''
my_grep.pyのモジュールだよ。
'''

from my_grep import *
#################### REPLの処理 ####################
def replaceName(directory, thing, yeah):
    ### ファイル名に検索語が含まれてたら、置換してTrueを返す ###
    if RE == 1:
        if CS == 0:
            reFW = re.compile(FW, re.IGNORECASE)
            if re.findall(reFW, thing):
                yeah = True                     # 正規表現使う 大文字小文字区別なし
        else:
            if re.search(FW, thing):
                yeah = True                     # 正規表現使う 大文字小文字区別する
    else:
        if CS == 0:
            reFW = re.compile(FW, re.IGNORECASE)
            if re.findall(reFW, thing):
                yeah = True                     # 正規表現使わない 大文字小文字区別なし
        else:
            if FW in thing:
                yeah = True                     # 正規表現使わない 大文字小文字区別する
    if yeah == True:
        newthing = thing.replace(FW, RW)
        os.rename(directory + "/" + thing, directory + "/" + newthing)
    else:
        newthing = thing
    return newthing, yeah

def replaceText(repl, directory, thing, yeah):
    ### もし検索語が含まれてたら、置換して、パスとその行が書かれた文字列を返す ###
    path  = directory + "/" + thing
    fopen = open(path, encoding="utf-8")
    lines = fopen.readlines()
    fopen.close()
    for i in range(len(lines)):
        if RE == 1:
            if CS == 0:
                reFW = re.compile(FW, re.IGNORECASE)
                if re.findall(reFW, lines[i]):
                    for element in re.findall(reFW, lines[i]):
                        lines[i] = lines[i].replace(element, RW)
                    repl    += "    [%d] %s" % (i+1, lines[i])
                    yeah     = True                # 正規表現使う 大文字小文字区別なし
            else:
                if re.search(FW, lines[i]):
                    lines[i] = lines[i].replace(FW, RW)
                    repl    += "    [%d] %s" % (i+1, lines[i])
                    yeah     = True                # 正規表現使う 大文字小文字区別する
        else:
            if CS == 0:
                reFW = re.compile(FW, re.IGNORECASE)
                if re.findall(reFW, lines[i]):
                    for element in re.findall(reFW, lines[i]):
                        lines[i] = lines[i].replace(element, RW)
                    repl    += "    [%d] %s" % (i+1, lines[i])
                    yeah     = True                # 正規表現使わない 大文字小文字区別なし
            else:
                if lines[i].find(FW) >= 0:
                    lines[i] = lines[i].replace(FW, RW)
                    repl    += "    [%d] %s" % (i+1, lines[i])
                    yeah     = True                # 正規表現使わない 大文字小文字区別する
    if yeah == True:
        ### 置換したものを上書き処理 ###
        temp = ""
        for i in range(len(lines)):
            temp += lines[i]
        fopen = open(path, "w", encoding="utf-8")
        fopen.write(temp)
        fopen.close()
    return repl, yeah

def replaceFile(directory, thing):
    ### もし検索語が含まれてたら、パスとその行が書かれた文字列を返す ###
    yeah = False
    path = directory + "/" + thing
    repl = "%s\n" % path
    if NAME == 1:                                   # ファイル名検索するなら続行する
        thing, yeah = replaceName(directory, thing, yeah)
        path = directory + "/" + thing              # ファイル開くためにrename済みのパスを作っとく
        repl = "%s\n" % path                        # 置換済みのパスを記述しとく
    if os.path.isfile(path):                        # それがファイルなら開いて検索する
        repl, yeah = replaceText(repl, directory, thing, yeah)
    if yeah == True:
        return repl
