from email.message import EmailMessage
import ssl
import smtplib
from decouple import config

def send_email(subject, body, to_address):
    from_address =config('EMAIL')
    password = config('EMAIL_PASS')
    to_address_new = config('TO_EMAIL')
    
    message = f"""
        <h2>El usuario {to_address} ha enviado un mensaje</h2>
        <p>{body}</p>
    """

    try:

        em = EmailMessage()

        em['From'] = from_address
        em['To'] = to_address_new
        em['Subject'] = subject
        em.set_content(message, subtype='html')

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(from_address, password)
            smtp.sendmail(from_address, to_address_new, em.as_string())

        return True
    except Exception as e:
        print(e)
        return False
