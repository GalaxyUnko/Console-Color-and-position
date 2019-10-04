from __future__ import print_function
# ↑を書いとくとpython2.xでも3みたいにかける
# たとえば改行しないやつprint(~,end="")とか

s1 = 'Hello'
s2 = 'world'

print ('%s, %s' % (s1, s2))  # Hello, worldと表示

# 一行上に
print("\033[2A") 

# ??G → 左から??行
print("\033[%dG\033[38;5;%dm%d"% (x,200+x,x))
