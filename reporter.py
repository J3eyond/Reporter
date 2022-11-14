import mimetypes
import os
import smtplib
import ssl
from email.message import EmailMessage

from dotenv import load_dotenv


class Reporter:
    def __init__(self):
        self.msg = EmailMessage()
        self.msg["Subject"] = os.getenv("SUBJECT")
        self.msg["From"] = os.getenv("EMAIL")
        self.msg["To"] = os.getenv("RECEIVER")
        self.msg.set_content(os.getenv("MESSAGE"))
        self.smtp_server = os.getenv("SMTP_SERVER")
        self.port = os.getenv("PORT")
        self.login = os.getenv("LOGIN")
        self.password = os.getenv("PASSWORD")
        self.files = [
            file
            for file in os.listdir(os.getenv("REPORT_FOLDER"))
            if os.path.isfile(os.path.join(os.getenv("REPORT_FOLDER"), file))
        ]
        self.context = ssl._create_unverified_context()

    def attach_files(self):
        for file in self.files:
            mime_type, _ = mimetypes.guess_type(file)
            mime_type, mime_subtype = mime_type.split("/")
            with open(
                os.path.join(os.getenv("REPORT_FOLDER"), file), "rb"
            ) as attachment:
                self.msg.add_attachment(
                    attachment.read(),
                    maintype=mime_type,
                    subtype=mime_subtype,
                    filename=file,
                )

    def send_email(self):
        with smtplib.SMTP(self.smtp_server, self.port) as server:
            server.starttls(context=self.context)
            server.login(self.login, self.password)
            server.send_message(self.msg)


if __name__ == "__main__":
    load_dotenv()
    reporter = Reporter()
    try:
        reporter.attach_files()
        reporter.send_email()
        print("[+] Email sent successfully.")
    except (Exception) as e:
        print(e)
        print("[-] Email not sent.")
