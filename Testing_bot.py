    # import os, re, json
    # from datetime import datetime, date, timedelta
    # from flask import Flask, request, abort
    # import requests
    # from linebot import (
    # LineBotApi, WebhookHandler
    # )
    # from linebot.exceptions import (
    # InvalidSignatureError
    # )
    # from linebot.models import (
    # MessageEvent, TextMessage, TextSendMessage,
    # )
    #
    # app = Flask(__name__)
    #
    # channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
    # channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
    #
    # line_bot_api = LineBotApi('2GCjJv9Ezo3T6uiqrd0bxGRz7YkQ68cmbmdwWhIyn09tdBhbrJWHzfEbxL9StEj1WvZVGkZoevZV39yg9Pv1kIWXpJ+uHcma00UNpDKAQfpF2RrgsH64T/Ce7C0vjqvt3i8x3nWSCu+wLrXC8395iwdB04t89/1O/w1cDnyilFU=')
    # handler = WebhookHandler('c7cfc2bca7ff78c0e521b5a14cffef42')
    #
    #
    # @app.route('/')
    # def homepage():
    # the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
    #
    # return """
    # <h1>Hello Translator-Bot</h1>
    # <p>It is currently {time}.</p>
    # <img src="http://loremflickr.com/600/400">
    # """.format(time=the_time)
    #
    #
    # @app.route("/callback", methods=['POST'])
    # def callback():
    # # get X-Line-Signature header value
    # signature = request.headers['X-Line-Signature']
    #
    # # get request body as text
    # body = request.get_data(as_text=True)
    # app.logger.info("Request body: " + body)
    #
    # # handle webhook body
    # try:
    #     handler.handle(body, signature)
    # except InvalidSignatureError:
    #     abort(400)
    #
    # return 'OK'
    #
    #
    # @handler.add(MessageEvent, message=TextMessage)
    # def handle_message(event):
    # text = event.message.text
    # line_bot_api.reply_message(
    #     event.reply_token,
    #     TextSendMessage(text=text))
    #
    #
    # if __name__ == "__main__":
    # app.run(debug=True, use_reloader=True)

# from flask import Flask, request, abort
# from linebot import (LineBotApi, WebhookHandler)
# from linebot.exceptions import (InvalidSignatureError)
# from linebot.models import (MessageEvent, TextMessage, TextSendMessage)
#
# app = Flask(__name__)
#
# line_bot_api = LineBotApi('KAhNUT+ta6Zsloe0h3B0gTphnggXLjtjpwA/tw5D0q8C322NztcJRb4oZ+X6n0f+WvZVGkZoevZV39yg9Pv1kIWXpJ+uHcma00UNpDKAQfosG+F+9D2L8tdH1Yy4+zH24M40gfHX8nlZaeMNmuVz4AdB04t89/1O/w1cDnyilFU=')   #I put my TOKEN
# handler = WebhookHandler('c7cfc2bca7ff78c0e521b5a14cffef42')
#
#
# @app.route("/callback", methods=['POST'])
# def callback():
#     # get X-Line-Signature header value
#     signature = request.headers['X-Line-Signature']
#
#     # get request body as text
#     body = request.get_data(as_text=True)
#     app.logger.info("Request body: " + body)
#
#     # handle webhook body
#     try:
#         events = parser.parse(body, signature)
#         for event in events:
#             if not isinstance(event, MessageEvent):
#                 continue
#             if not isinstance(event.message, TextMessage):
#                 continue
#
#             line_bot_api.reply_message(
#                 event.reply_token,
#                 TextSendMessage(text=event.message.text)
#             )
#     except:
#         # handle all exception
#         print("Unexpected error:", sys.exc_info()[0])
#     #     handler.handle(body, signature)
#     # except InvalidSignatureError:
#     #     abort(400)
#
#     return 'OK'
#
#
# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage(text=event.message.text))
#
# if __name__ == "__main__":
#     app.run()

    import os, re, json
    from datetime import datetime, date, timedelta
    from flask import Flask, request, abort
    from googletrans import Translator
    import requests
    from linebot import (
        LineBotApi, WebhookHandler
    )
    from linebot.exceptions import (
        InvalidSignatureError
    )
    from linebot.models import (
        MessageEvent, TextMessage, TextSendMessage,
    )

    app = Flask(__name__)
    translator = Translator()

    channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
    channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)

    line_bot_api = LineBotApi(channel_access_token)
    handler = WebhookHandler(channel_secret)


    @app.route('/')
    def homepage():
        the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

        return """
    <h1>Hello Translator-Bot</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400">
    """.format(time=the_time)


    @app.route("/callback", methods=['POST'])
    def callback():
        # get X-Line-Signature header value
        signature = request.headers['X-Line-Signature']

        # get request body as text
        body = request.get_data(as_text=True)
        app.logger.info("Request body: " + body)

        # handle webhook body
        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return 'OK'


    def translate_text(text):
        en_text = translator.translate(text, dest='en').text
        return en_text


    @handler.add(MessageEvent, message=TextMessage)
    def handle_message(event):
        text = event.message.text
        translated = translate_text(text)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=translated))


    if __name__ == "__main__":
        app.run(debug=True, use_reloader=True)