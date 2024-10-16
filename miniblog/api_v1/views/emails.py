from django.http import HttpResponse
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_test_email(request):
    asunto = "Probando el envio de emails"
    mensaje = "Enviando emails desde Django"
    receptores = ["matias@matias.com", "huck@itec.com"]
    from_email = "saliodeaca@google.com"
    send_mail(
        subject=asunto,
        message=mensaje,
        recipient_list=receptores,
        from_email=from_email
    )

    return HttpResponse("Email Enviado Correctamente")

def email_products_sender(request):
    usuario = "Jonh Doe"
    products =[
        {
            'name': 'producto 1',
            'price': 123455
        },
        {
            'name': 'producto 2',
            'price': 4564554
        },
        {
            'name': 'producto 3',
            'price': 12
        },
    ]

    asunto = "Tenemos ofertas para vos"
    html_content = render_to_string(
        'emails/products_email.html',
        dict(usuario=usuario, products=products)
    )
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(
        subject=asunto,
        body=text_content,
        from_email='saliodeaca@email.com',
        to=['Carlito@carlos.com'],
    )

    email.attach_alternative(html_content, 'text/html')
    email.send()
    return HttpResponse("Email Enviado Correctamente")
