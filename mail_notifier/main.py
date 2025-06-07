import schedule
import time
from imap_client import MailClient
from line_notifier import send_line_message
from config import EMAIL_ACCOUNTS

def job():
    
    try:
        keywords = ["重要", "paiza"]
        client = MailClient(**EMAIL_ACCOUNTS[0])
        client.connect()
        matched = client.search_emails(keywords)
        for subject in matched:
            message = f"新着メール\n {subject}"
            send_line_message(message)
            client.disconnect()

    except Exception as e:
        print("[ERROR] エラーが発生:", e)

schedule.every(3).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
    