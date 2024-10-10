from celery import shared_task
from mail_templated import EmailMessage

@shared_task
def SendEmail(token, email):
    EmailMessage(
        "email/verify.tpl",
        {"token": token},
        "benxfoxy@gmail.com",
        to=[email],
    ).send()
