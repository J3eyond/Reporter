import mimetypes
import os
import smtplib
import ssl
from email.message import EmailMessage

from dotenv import load_dotenv


class Message:
    def __init__(self):
        self.msg = EmailMessage()
        self.msg["Subject"] = os.getenv("SUBJECT")
        self.msg["From"] = os.getenv("EMAIL")
        self.msg["To"] = os.getenv("RECEIVER")
        self.msg.set_content(os.getenv("MESSAGE"))


class Sender:
    def __init__(self):
        self.smtp_server = os.getenv("SMTP_SERVER")
        self.port = os.getenv("PORT")
        self.login = os.getenv("LOGIN")
        self.password = os.getenv("PASSWORD")

    def send_message(self):
        pass


def attach_files():
    pass


def search_files(folder):

    return [
        file
        for file in os.listdir(folder)
        if os.path.isfile(os.path.join(folder, file))
    ]


if __name__ == "__main__":
    load_dotenv()
    search_files(os.getenv("REPORT_FOLDER"))
    print(search_files(os.getenv("REPORT_FOLDER")))
