from celery import shared_task
from mail_templated import EmailMessage
from time import sleep

@shared_task
def SendEmail(token,email):
    sleep(10)
    EmailMessage(
    "email/verify.tpl",
    {"token": token},
    "benxfoxy@gmail.com",
    to=[email],
    ).send()