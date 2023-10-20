from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(user_logged_in, sender=User)
def looged_success(sender, request, user, **kwargs):

    ip = request.META.get('REMOTE_ADDR')  # trace ip address
    
    request.session['ip'] = ip       # session 
    