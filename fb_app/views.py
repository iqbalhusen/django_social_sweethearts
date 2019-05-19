from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from allauth.socialaccount.models import SocialAccount


def home(request):
    if request.user.is_authenticated:
        try:
            social_account = SocialAccount.objects.get(user=request.user)
            context_dict = {
                'is_authenticated': True,
                'fb_id': social_account.uid,
                'full_name': request.user.get_full_name()
            }
        except SocialAccount.DoesNotExist:
            logout(request)
            context_dict = {'is_authenticated': False}
    else:
        context_dict = {'is_authenticated': False}

    return render(request, 'home.html', context_dict)


@csrf_exempt
def de_auth_callback(request):
    print(request.POST)

    fb_id = request.POST.get('uid')  # ASSUMING that the request body has this parameter
    # NOT TESTED as Facebook allows only SSL URLs as Deauthorize Callback URL. Didn't have enough time to host it on
    # some PaaS e.g. Heroku.

    social_account = SocialAccount.objects.get(provider__iexact='Facebook', uid=fb_id)
    social_account.user.is_active = False
    social_account.user.save()

    return HttpResponse(status=204)


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')
