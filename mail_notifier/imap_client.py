import imaplib
import email
import os
from email.header import decode_header
from datetime import datetime, timedelta

today = datetime.now().strftime("%d-%b-%Y")
since_date = (datetime.now() - timedelta(days=10)).strftime("%d-%b-%Y")
before_date = (datetime.now() + timedelta(days=1)).strftime("%d-%b-%Y")  # 今日の次の日（IMAPの仕様）

class MailClient:
    def __init__(self, name, server, port, email, password):
        self.name = name
        self.server = server
        self.port = port
        self.email_addr = email
        self.password = password
        self.connection = None
    
    # IMAPサーバーに接続
    def connect(self):
        self.connection = imaplib.IMAP4_SSL(self.server, self.port)
        self.connection.login(self.email_addr, self.password)
    
    def disconnect(self):
        if self.connection:
            self.connection.logout()
    
    def search_emails(self, keyword_list, folders=["INBOX", "Junk"]):
        matched_messages = []
        for folder in folders:
            try:
                self.connection.select(folder)
            except Exception as e:
                print(f"[WARNING] フォルダ {folder} を開けませんでした: {e}")
                continue
            result, data = self.connection.search(None, f'(SINCE {since_date} BEFORE {before_date})')
            if result != "OK":
                print(f"[ERROR] {self.name}: {folder} でメール検索に失敗")
                continue
            for mail_id in data[0].split():
                result, msg_data = self.connection.fetch(mail_id, '(BODY[HEADER])')
                if result != "OK":
                    continue
                msg = self._get_message_from_data(msg_data)
                if not msg:
                    continue
                subject = self._decode_subject(msg["Subject"])
                if any(keyword in subject for keyword in keyword_list):
                    # print("==== 件名 ====")
                    # print(subject)
                    matched_messages.append((subject))
        return matched_messages
    
    def _get_message_from_data(self, msg_data):
        for response_part in msg_data:
            if isinstance(response_part, tuple) and isinstance(response_part[1], bytes):
                return email.message_from_bytes(response_part[1])
        return None
    
    def _decode_subject(self, subject_header):
        if subject_header is None:
            return "(No Subject)"
        subject, encoding = decode_header(subject_header)[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding or "utf-8", errors="ignore")
        return subject
    
    def download_attachments(self, msg, save_dir="attachments"):
        os.makedirs(save_dir, exist_ok=True)
        for part in msg.walk():
            if part.get_content_disposition() == "attachment":
                filename = part.get_filename()
                if filename:
                    filepath = os.path.join(save_dir, filename)
                    with open(filepath, "wb") as f:
                        f.write(part.get_payload(decode=True))



        
