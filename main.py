import time
import telepot
import sys
from telepot.loop import MessageLoop

def handle(msg):
    chat_id=msg['chat']['id']
    command=msg['text']

    print("Got command",command)
    if command=='/help':
        bot.sendMessage(chat_id,"Type /list to list all tasks")
    if command.
    elif command=='/list':
        bot.sendMessage(chat_id,"Listing all items")
    elif command=='/about':
        bot.sendMessage(chat_id,"Created by Sathish")

TOKEN=sys.argv[1]
bot=telepot.Bot(TOKEN)

MessageLoop(bot,handle).run_as_thread()
print('I am listening ...')

while 1:
    time.sleep(10)
