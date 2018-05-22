from wxpy import *

bot = Bot()
my_friend = bot.friends().search('陈阳')[0]
print(my_friend.uin())
@bot.register()
def print_messages(msg):
    print(msg)

# 堵塞线程，并进入 Python 命令行
embed()