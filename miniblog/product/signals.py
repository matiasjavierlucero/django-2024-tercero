from django.core.mail import send_mail
from django.db.models.signals import post_save, pre_save, post_delete, m2m_changed
from django.dispatch import receiver

from .models import Product


@receiver(post_save, sender=Product)
def product_create(sender, instance, created, **kwargs):
    if created:
        print(f"Se ha creado un producto nuevo llamado {instance}")

@receiver(pre_save, sender=Product)
def set_product_upper_name(sender, instance, **kwargs):
    instance.name = instance.name.upper()

@receiver(post_delete, sender=Product)
def delete_product_notify_admin(sender, instance, **kwargs):
    asunto = "Alerta se borro un producto"
    mensaje = f"Se ha borrado el producto {instance}"
    receptor = ['matias@matias.com']
    enviado_desde = "test@email.com"
    try:
        send_mail(
            subject=asunto,
            message=mensaje,
            recipient_list=receptor,
            from_email=enviado_desde
        )
        print("Producto borrado y email enviado")
    except:
        print("No se ha podido enviar el email")
