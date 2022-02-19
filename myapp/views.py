from distutils.log import error
from urllib.request import Request
from django.shortcuts import render, redirect
from django.views import View
from myapp.forms import UserProfileForm
from myapp.models import UserProfile
# Create your views here.


class HomwView(View):
    def get(self, request):
        fm = UserProfileForm()
        return render(request, 'home.html', {'form': fm})

    def post(self, request):
        fm = UserProfileForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            return render(request, 'home.html', {'form': fm})
        else:
            print("error")
            return render(request, 'home.html', {'form': fm})


class ShowDetails(View):
    def get(self, request):
        userpro = UserProfile.objects.all()
        return render(request, 'showdetails.html', {'myuser': userpro})


class Editview(View):
    def get(self, request, id):
        myuser = UserProfile.objects.get(id=id)
        userprofile = UserProfileForm(instance=myuser)
        return render(request, 'editview.html', {'form': userprofile})

    def post(self, request, id):
        myuser = UserProfile.objects.get(id=id)
        userprofile = UserProfileForm(
            request.POST, request.FILES, instance=myuser)
        if userprofile.is_valid():
            userprofile.save()
            return redirect("showdetail")
        else:
            return render(request, 'editview.html', {'form': userprofile})


class Deleteview(View):
    def get(self, request, id):
        myuser = UserProfile.objects.get(id=id)
        myuser.delete()
        return redirect("showdetail")


class SearchView(View):
    def get(self, request):
        userpro = UserProfile.objects.all()
        return render(request, 'showdetails.html', {'myuser': userpro})

    def post(self, request):
        se = request.POST.get("se")
        userpro = UserProfile.objects.filter(name=se)
        print(userpro)
        return render(request, 'showdetails.html', {'myuser': userpro})
