from flask import Flask, request, abort

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

line_bot_api = LineBotApi('RCv/FsHlcY/72TkwFtRLTL7JvnjsL5Y3FhTeqdPuDBKjKX76z7ljPQZ2xrHHPjMU1PiNRC+f2eQ76O0lGHWgP+qfIj/cvuI3JPiBHqsiW+aYlCGxpV4/Rk5RVQ/QKCUF/nvmb20HiSjgklBWkQGK7AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('a2692aff1ed6c3c5a9c079e0718fe9ec')


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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='你吃飯了嗎'))


if __name__ == "__main__":
    app.run()