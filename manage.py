import bot_app.main
import project
import bot_app
import threading
if __name__ == '__main__':
    threading.Thread(target=bot_app.main.bot.infinity_polling, args=(20,True)).start()
    
    project.project.run(debug=False)
print(121)
print(1212)

