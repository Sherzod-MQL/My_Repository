from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters, InlineQueryHandler


TOKEN = '6139764907:AAHKWE99mhg3pT6xqDkdDRQjcwS-FC9WfYI'
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher


# функция обработки команды '/start'
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="I'm a bot, please talk to me!")


# функция обработки текстовых сообщений
def echo(update, context):
    text = 'ECHO: ' + update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=text)


# функция обработки команды '/caps'
def caps(update, context):
    s = update.message.text.split(' ')
    text_caps = ' '.join(s).upper()
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=text_caps)
    if context.args:
        text_caps = ' '.join(context.args).upper()
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=text_caps)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='No command argument')
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='send: /caps argument')


def summa(update, context):
    s = update.message.text.split(' ')
    if len(s) != 3:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='No command argument')
    else:
        a = int(s[1])
        b = int(s[2])
        c = a+b
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=c)


# функция обработки встроенного запроса
def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Convert to UPPER TEXT',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)


# функция обработки не распознных команд
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Sorry, I didn't understand that command.")

def kopaytma(update, context):
    s = update.message.text.split(' ')
    if len(s) != 4:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Xatolik")
    else:
        a = int(s[1])
        b = int(s[2])
        c = int(s[3])
        d = a*b*c
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=d)

def main() -> None:

    kopaytma_handler = CommandHandler('kopaytma', kopaytma)
    dispatcher.add_handler(kopaytma_handler)

    # обработчик команды '/start'
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # обработчик текстовых сообщений
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    # обработчик команды '/caps'
    caps_handler = CommandHandler('caps', caps)
    dispatcher.add_handler(caps_handler)

    ekub_handler = CommandHandler('summa', summa)
    dispatcher.add_handler(ekub_handler)

    # обработчик встроенных запросов
    inline_caps_handler = InlineQueryHandler(inline_caps)
    dispatcher.add_handler(inline_caps_handler)

    # обработчик не распознанных команд
    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)

    # запуск прослушивания сообщений
    updater.start_polling()
    # обработчик нажатия Ctrl+C
    updater.idle()


if __name__ == "__main__":
    main()