from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import FollowEvent, MessageEvent, TextMessage, TextSendMessage

from django.contrib.auth.models import User
from linebotapp.models import Room, Message

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
    User.objects.create_user(username=event.source.userId, password=event.source.userId)

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    if event.source.type == "room":
        room = Room.objects.create(room_id=event.source.roomId)
    else:
        room = Room.objects.create(room_id=event.source.userId)
    
    room.user.add(event.source.userId)
    # message = event.message.text
    # メッセージの処理ロジックをここに追加
    # 例: 応答メッセージを送信
    # line_bot_api.reply_message(
    #     event.reply_token,
    #     TextMessage(text='Received: ' + message)
    # )