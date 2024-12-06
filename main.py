import telebot

API_TOKEN = '<api_token>'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help',"start"])
def send_welcome(message):
    bot.reply_to(message, """\
Здравствуйте, вы обратились в бота поддержки онлайн магазина - "" тут вы найдете ответ для большинства популярных вопросов пользователей
либо вам ответит поддержка на ваш вопрос.
                 
Список вопросов с авто-ответом бота:

1. Не знаете как оформить заказ? Пишите /a1
                 
2. Не знаете как узнать статус вашего текущего заказа? Пишите /a2
                 
3. Не знаете как отменить ваш заказ? Пишите /a3
                 
4. Не знаете что делать, если товар пришел поврежденным? Пишите /a4
                 
5. Не знаете как связаться с технической поддержкой? Пишите /a5
                 
6. Не знаете как узнать информацию о доставке? Пишите /a6
                 
    Если у вас есть вопросы отличные от данных, вам с радостью ответит служба поддержки,
    напишите команду /question (Представители поддержки отвечают так быстро как только могут)
\
""")

@bot.message_handler(commands=['a1'])
def answer_one(message):
    bot.reply_to(message, """\
Для оформления заказа, пожалуйста, выберите интересующий вас товар и нажмите кнопку "Добавить в корзину", затем перейдите в корзину и следуйте инструкциям для завершения покупки.
\
""")

@bot.message_handler(commands=['a2'])
def answer_two(message):
    bot.reply_to(message, """\
Вы можете узнать статус вашего заказа, войдя в свой аккаунт на нашем сайте и перейдя в раздел "Мои заказы". Там будет указан текущий статус вашего заказа.
""")
    
@bot.message_handler(commands=['a3'])
def answer_three(message):
    bot.reply_to(message, """\
Если вы хотите отменить заказ, пожалуйста, свяжитесь с нашей службой поддержки как можно скорее. Мы постараемся помочь вам с отменой заказа до его отправки.
\
""")
    
@bot.message_handler(commands=['a4'])
def answer_four(message):
    bot.reply_to(message, """\
При получении поврежденного товара, пожалуйста, сразу свяжитесь с нашей службой поддержки и предоставьте фотографии повреждений. Мы поможем вам с обменом или возвратом товара.
""")

@bot.message_handler(commands=['a5'])
def answer_five(message):
    bot.reply_to(message, """\
Вы можете связаться с нашей технической поддержкой через телефон на нашем сайте или написать нам в чат-бота.
""")

@bot.message_handler(commands=['a6'])
def answer_six(message):
    bot.reply_to(message, """\
Информацию о доставке вы можете найти на странице оформления заказа на нашем сайте. Там указаны доступные способы доставки и сроки.
""")


@bot.message_handler(commands=['question'])
def answer_six(message):
    bot.reply_to(message, """\
Здравствуйте, если у вас появилисб вопросы которые отличаются от тех, что написаны в команде /help, 
то обратитесь пожалуйста к создателям @gleb101210 или @nasirovramin , мы постараемся ответить как можно быстрее, с уважением, 
служба поддержки "название магазина store"
""")
    

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()