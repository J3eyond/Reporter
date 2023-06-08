import mimetypes
import os
import smtplib
import ssl
from email.message import EmailMessage

from dotenv import load_dotenv


class Reporter:

    load_dotenv()

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
        if len(self.files) > 1:
            print("[*] Attaching files to email.")
            for file in self.files:
                if file == "README.md":
                    pass
                else:
                    mime_type, _ = mimetypes.guess_type(file)
                    mime_type, mime_subtype = mime_type.split("/")
                    with open(
                        f"{os.getenv('REPORT_FOLDER')}{file}", "rb"
                    ) as attachment:
                        self.msg.add_attachment(
                            attachment.read(),
                            maintype=mime_type,
                            subtype=mime_subtype,
                            filename=file,
                        )
        else:
            print("[-] Attachment files not found.")

    def send_email(self):
        with smtplib.SMTP(self.smtp_server, self.port) as server:
            server.starttls(context=self.context)
            server.login(self.login, self.password)
            server.send_message(self.msg)


if __name__ == "__main__":
    reporter = Reporter()
    try:
        print("[*] Connecting to smtp server.")
        reporter.attach_files()
        print("[*] Sending email.")
        reporter.send_email()
        print("[+] Email successfully sent.")
    except (Exception) as e:
        print(e)
        print("[-] Email not sent.")
