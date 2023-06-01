from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import FollowEvent, MessageEvent, TextMessage, TextSendMessage

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)

def index(request):
    return HttpResponse(status=200)

@csrf_exempt
def line_webhook(request):
    if request.method == 'POST':
        signature = request.headers['X-Line-Signature']
        body = request.body.decode('utf-8')

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            return HttpResponse(status=400)
        return HttpResponse(status=200)

@handler.add(FollowEvent)
def handle_follow(event):
    print(event)

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    print(type(event))
    print(event)
    print('message' in event)
    print('id' in event.message)
    # message = event.message.text
    # メッセージの処理ロジックをここに追加
    # 例: 応答メッセージを送信
    # line_bot_api.reply_message(
    #     event.reply_token,
    #     TextMessage(text='Received: ' + message)
    # )