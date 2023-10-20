from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.cache import cache

@receiver(user_logged_in, sender=User)               #Decorator syntax: @receiver(signal or list of signal, sender)
def looged_success(sender, request, user, **kwargs):        #signals  user_logged_in

    ct = cache.get('count', 0, version=user.pk)              #cache.get(key, default=None, version=None) 
    newcount = ct + 1
    cache.set('count', newcount, 60*60*24, version=user.pk)  #cache.set(key, value, timeout=DEFAULT_TIMEOUT, version=None)
    