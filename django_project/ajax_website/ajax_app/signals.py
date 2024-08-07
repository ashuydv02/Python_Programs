from django.db.models.signals import post_save, post_delete
from .models import Orders,CustomUser
from django.db.models import Sum
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

import os


@receiver(post_delete, sender=CustomUser)
def delete_user_image(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


@receiver(post_save, sender=Orders)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        total_amount = Orders.objects.filter(user=user).aggregate(total=Sum('total'))
        receiver_mail = CustomUser.objects.get(username=user).email
        mail_content = "Your Order has been succesfully placed..."
        html_message = f'''<br><p>You can Track your orders in your account.<br>
                        <strong>Your Total Payable amount is : {total_amount['total']}</strong>
                        <br><br><br>
                        Thank you<br>Regards<br>Get Your Food Team</p>'''
        send_mail(
            "Order Confirmation Mail",
            mail_content,
            settings.DEFAULT_FROM_EMAIL,
            [receiver_mail],
            html_message=html_message
        )