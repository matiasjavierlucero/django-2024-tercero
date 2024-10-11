from django.http import HttpResponse
from django.core.mail import send_mail, EmailMultiAlternatives

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
