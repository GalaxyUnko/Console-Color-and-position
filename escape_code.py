from __future__ import print_function
# ↑を書いとくとpython2.xでも3みたいにかける
# たとえば改行しないやつprint(~,end="")とか
# ただし一番最初に宣言する

s1 = 'Hello'
s2 = 'world'

print ('%s, %s' % (s1, s2))  # Hello, worldと表示


# Terminalの色とか表示位置とか
# シェルスクリプト　→　https://qiita.com/PruneMazui/items/8a023347772620025ad6
# https://www.mm2d.net/main/prog/c/console-02.html

x = 1
print("\033[2A%d" % x) # 一行上にxと表示(2.xでも可)
print("\033[%dG%d" % (x,x)) # 左からx文字目にxと表示(2.xでも可)
print("\033[10;100H--unko--") # 絶対的な位置(10,100)に--unko--と表示(上から10行目左から100文字目)

# 文字色は\033[38;5;(0~255)m
# 背景色は\033[48;5;(0~255)m
# 実行すると色の変化が見れる
for i in range(256):
    print("\033[38;5;%dm %d"% (i,i))
