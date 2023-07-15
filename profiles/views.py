from django.shortcuts import render, redirect
from . models import Userprofiles
from . forms import UpdateprofileForm
from django.contrib import messages

# Create your views here.

def profile(request, pk):
    user_profile = Userprofiles.objects.get(pk=pk)
    context = {'user_profile': user_profile}

    return render(request, 'profiles/profile.html', context)


def account(request):
    user_account = request.user.userprofile
    context = {'account': user_account}
    return render(request, 'profiles/account.html', context)


def updateprofile(request):
    # profile = request.user.userprofile
    form = UpdateprofileForm()
    if request.method == 'POST':
        form = UpdateprofileForm(request.POST, request.FILES, instance = profile)
        if form.is_valid():
            form.save()
            messages.info(request, "You updated your profile")
            return redirect('account')

    context = { 'form': form}
    return render(request, 'profile/update.html', context)

def delete(request):
    profile = request.user.userprofile
    form = UpdateprofileForm(instance=profile)
    if request.method == 'POST':
        userprofile = Userprofiles.objects.get(user=profile)
        userprofile.delete()
        messages.error(request, 'Your profile has been deleted')
        return redirect('index')

    context = {'userprofile': userprofile}
    return render(request, 'profiles/delete.html', context)


