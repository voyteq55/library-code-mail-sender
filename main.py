from mail_sender import MailSender
from email.message import EmailMessage
import dotenv
import os


def main():
    dotenv.load_dotenv()
    sender_email = os.environ["SENDER_EMAIL"]
    sender_password = os.environ["SENDER_PASSWORD"]
    recipient_email = os.environ["RECIPIENT_EMAIL"]

    msg = EmailMessage()
    msg.set_content('jol test')

    msg['Subject'] = 'temat maila'
    msg['From'] = sender_email
    msg['To'] = recipient_email

    sender = MailSender(from_mail=sender_email, mail_password=sender_password)
    sender.send_mail(message=msg.as_string(), to_mail=recipient_email)


if __name__ == "__main__":
    main()
