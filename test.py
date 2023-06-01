event = {
    "deliveryContext": {
        "isRedelivery": False
    },
    "message": {
        "id": "457694501357224417",
        "text": "\u3082\u3057\u304b\u3057\u305f\u3089bot\u304c\u4f55\u304b\u8a00\u3046\u304b\u3082\u3057\u308c\u306a\u3044\u3051\u3069\u3001\u6c17\u306b\u3057\u306a\u3044\u3067\u306d\u30fc",
        "type": "text"
    },
    "mode": "active",
    "replyToken": "a0db9b7bea8740d5af00f7ca51d6551a",
    "source": {
        "roomId": "R341eaf29e100a0cb580507d0ae52b7c8",
        "type": "room",
        "userId": "Ue4639d9f1cb95119d1807e6fedf5d2a1"
    },
    "timestamp": 1685638485708,
    "type": "message",
    "webhookEventId": "01H1VY466CYSDY1Y9DVP3H95E6"
}

print('id' in event.message)