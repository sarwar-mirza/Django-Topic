from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init, pre_save, pre_delete, post_init, post_save, post_delete, pre_migrate, post_migrate
from django.core.signals import request_started, request_finished, got_request_exception

# user_logged_in
@receiver(user_logged_in, sender=User) 
def logged_success(sender, request, user, **kwargs):
    print('-----------------------------')
    print('user_logged_in------ run intro')
    print('Sender:', sender)
    print('Request:', request)
    print('User:', user)
    print('user password: ', user.password)
    print(f"kwargs: {kwargs}")
#user_logged_in.connect(logged_success, sender=User)

# user_logged_out
@receiver(user_logged_out, sender=User) 
def log_out(sender, request, user, **kwargs):
    print('-----------------------------')
    print('user_logged_out------run outro')
    print('Sender:', sender)
    print('Request:', request)
    print('User:', user)
    print(f"kwargs: {kwargs}")
#user_logged_out.connect(log_out, sender=User)

# user_login_failed
@receiver(user_login_failed) 
def login_failed(sender, credentials , request,  **kwargs):
    print('-----------------------------')
    print('user_login_failed------')
    print('Sender:', sender)
    print('Credentials: ', credentials)
    print('Request:', request)
    print(f"kwargs: {kwargs}")
#user_login_failed.connect(login_failed)


# pre_save
@receiver(pre_save, sender=User) 
def at_beginning_save(sender, instance , **kwargs):
    print('-----------------------------')
    print('Pre save signals------')
    print('Sender:', sender)
    print('Instance: ', instance)
    print(f"kwargs: {kwargs}")
#pre_save.connect(at_beginning_save, sender=User)


# post_save
@receiver(post_save, sender=User) 
def at_ending_save(sender, instance, created, **kwargs):
    if created:
        print('-----------------------------')
        print('Post save signals------')
        print('New Record in Now')
        print('Sender:', sender)
        print('Instance: ', instance)
        print('Created: ', created)
        print(f"kwargs: {kwargs}")
    else:
        print('-----------------------------')
        print('Post save signals------')
        print('Update data')
        print('Sender:', sender)
        print('Instance: ', instance)
        print('Created: ', created)
        print(f"kwargs: {kwargs}")

#post_save.connect(at_ending_save, sender=User)


#pre delete
@receiver(pre_delete, sender=User)
def at_beginning_delete(sender, instance, **kwargs):
    print('-----------------------------')
    print('Pre delete signals------')
    print('Sender:', sender)
    print('Instance: ', instance)
    print(f"kwargs: {kwargs}")
#pre_delete.connect(at_beginning_delete, sender=User)

#post delete
@receiver(post_delete, sender=User)
def at_ending_delete(sender, instance, **kwargs):
    print('-----------------------------')
    print('post delete signals------')
    print('Sender:', sender)
    print('Instance: ', instance)
    print(f"kwargs: {kwargs}")
#post_delete.connect(at_ending_delete, sender=User)
    
#pre init
@receiver(pre_init, sender=User)
def at_beginning_init(sender, *args, **kwargs):
    print('-----------------------------')
    print('pre init signals------')
    print('Sender:', sender)
    print(f'args: {args}')
    print(f"kwargs: {kwargs}")
#pre_init.connect(at_beginning_init, sender=User)

#post init
@receiver(post_init, sender=User)
def at_ending_init(sender, *args, **kwargs):
    print('-----------------------------')
    print('post init signals------')
    print('Sender:', sender)
    print(f'args: {args}')
    print(f"kwargs: {kwargs}")
#pre_init.connect(at_beginning_init, sender=User)

#request started
@receiver(request_started)
def at_beginning_request(sender, environ, **kwargs):
    print('-----------------------------')
    print('At Beginning request signals------')
    print('Sender:', sender)
    print('Environ: ', environ)
    print(f"kwargs: {kwargs}")
#request_started.connect(at_beginning_request)

#request finished
@receiver(request_finished)
def at_ending_request(sender, **kwargs):
    print('-----------------------------')
    print('At ending request signals------')
    print('Sender:', sender)
    print(f"kwargs: {kwargs}")
#request_finished.connect(at_ending_request)
    
#request finished
@receiver(got_request_exception)
def at_req_exception(sender, request, **kwargs):
    print('-----------------------------')
    print('At request Exception signals------')
    print('Sender:', sender)
    print('Request: ', request)
    print(f"kwargs: {kwargs}")
#got_request_exception.connect(at_req_exception)

#pre migrate
@receiver(pre_migrate)
def before_install_app(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print('-----------------------------')
    print('Befor install App------')
    print('Sender:', sender)
    print('App_config: ', app_config)
    print('Verbosity: ', verbosity)
    print('Interactive: ', interactive)
    print('Using: ', using)
    print('Plan: ', plan)
    print('Apps: ', apps)
    print(f"kwargs: {kwargs}")
#pre_migrate.connect(befor_install_app)
#post migrate
@receiver(post_migrate)
def at_end_migrate_flush(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print('-----------------------------')
    print('At end migrate flush------')
    print('Sender:', sender)
    print('App_config: ', app_config)
    print('Verbosity: ', verbosity)
    print('Interactive: ', interactive)
    print('Using: ', using)
    print('Plan: ', plan)
    print('Apps: ', apps)
    print(f"kwargs: {kwargs}")
#post_migrate.connect(at_end_migrate_flush)


    