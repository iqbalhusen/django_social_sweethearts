from django.db import models
from django.dispatch import receiver
from allauth.socialaccount.signals import pre_social_login  # social_account_updated


@receiver(pre_social_login)
def social_account_added(request, sociallogin, **kwargs):
    if not sociallogin.user.is_active:  # Re-activate if inactive
        sociallogin.user.is_active = True
        sociallogin.user.save()
