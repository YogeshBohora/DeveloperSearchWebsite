from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .models import Profile
#from django.dispatch import receiver
#@receiver(post_save, sender=Profile)
#def profileUpdated(sender, instance, created, **kwargs):
 #   print('Profile Created') #  print('Instance:' , instance)   # print('Created:' , created)

#def profileDeleted(sender, instance, **kwargs):
 #   print("Profile is Deleted!!!")    

def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email= user.email,
            name = user.first_name)

def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()        
post_delete.connect(deleteUser, sender=Profile)  
post_save.connect(createProfile, sender=User)
  