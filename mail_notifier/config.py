import os
from dotenv import load_dotenv

# .envファイルを読み込み
load_dotenv()

# icloud
icloud_account = {
    "name": "icloud",
    "email": os.getenv("ICLOUD_ADDRESS"),
    "password": os.getenv("ICLOUD_PASSWORD"),
    "server": os.getenv("ICLOUD_IMAP_SERVER"),
    "port": int(os.getenv("ICLOUD_IMAP_PORT", 993))
}

#Outlook
outlook_account = {
    "name": "Outlook",
    "email": os.getenv("OUTLOOK_ADDRESS"),
    "password": os.getenv("OUTLOOK_PASSWORD"),
    "server": os.getenv("OUTLOOK_IMAP_SERVER"),
    "port": int(os.getenv("OUTLOOK_IMAP_PORT", 993))
}

# アカウントリストとして一括管理
EMAIL_ACCOUNTS = [icloud_account, outlook_account]

# LINE通知トークン
LINE_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
LINE_USER_ID = os.getenv("LINE_USER_ID")