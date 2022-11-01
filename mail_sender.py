import smtplib
import ssl


class MailSender:

    def __init__(self, from_mail, mail_password):
        self.from_mail = from_mail
        self.mail_password = mail_password

    def send_mail(self, message, to_mail):
        context = ssl.create_default_context()
        try:
            server = smtplib.SMTP("smtp.gmail.com", port=587)
            server.starttls(context=context)  # Secure the connection
            server.login(self.from_mail, self.mail_password)
            server.sendmail(
                from_addr=self.from_mail,
                to_addrs=to_mail,
                msg=message
            )
        except Exception as e:
            # Print any error messages to stdout
            print(e)
        finally:
            server.quit()
