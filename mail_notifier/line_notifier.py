import requests
from config import LINE_TOKEN, LINE_USER_ID

def send_line_message(text):
    # LINE Messagin API エンドポイント
    url = "https://api.line.me/v2/bot/message/push"

    # ヘッダー情報
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {LINE_TOKEN}"
    }

    # リクエストボディ
    payload = {
        "to": LINE_USER_ID,
        "messages": [
            {
                "type": "text",
                "text": text
            }
        ]
    }

    # POSTリクエストを送信
    response = requests.post(url, headers=headers, json=payload)
    return response.status_code, response.text
        


# 結果を表示
# print("送信ステータス:", response.status_code)
# print("レスポンス:", response.text)




