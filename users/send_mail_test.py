from django.core.mail import send_mail

subject = 'Тестовое письмо'
message = 'Привет! Это тестовое письмо от Django.'
from_email = 'martyn8v@ya.ru'  # Укажите ваш действительный email
recipient_list = ['martyn8v@gmail.com']  # Укажите действительный email получателя

send_mail(subject, message, from_email, recipient_list)
