from django.views.generic import CreateView, View, DetailView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from users.forms import RegistrationForm
from app.models import Songs, Profile


class registration_view(CreateView):
    model = Profile
    form_class = RegistrationForm
    success_url = '/'
    template_name = 'users/user_form.html'


class user_login_view(LoginView):
    template_name = 'users/login_form.html'

    def post(self, request, *args, **kwargs):
        if Profile.objects.filter(username=request.POST['username']).exists():
            return super().post(request, *args, **kwargs)
        else:
            NewProfile = Profile(username=request.POST['username'], user=User.objects.get(username=request.POST['username']))
            NewProfile.save()
            return super().post(request, *args, **kwargs)


def like_song(request, pk):
    liking_user = Profile.objects.get(username=request.user.username)
    liking_song = Songs.objects.get(id=pk)
    liking_user.favors.add(liking_song)
    return HttpResponseRedirect('/songs/')


class playlist(TemplateView):
    template_name = 'users/user_playlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = Profile.objects.get(username=self.request.user.username)
        context['user_favors'] = current_user.favors.all()
        return context


def delete_from_playlist(request, pk):
    current_user = Profile.objects.get(username=request.user.username)
    deleting_song = Songs.objects.get(id=pk)
    current_user.favors.remove(deleting_song)
    return HttpResponseRedirect('/users/playlist/')


class user_logout_view(LogoutView):
    pass


class user_profile(TemplateView):
    template_name = 'users/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.request.user
        context['user_songs'] = Songs.objects.filter(author_name=self.request.user.username)
        context['user_favors'] = User.objects.all()
        return context


class other_user(TemplateView):
    template_name = 'app/other_cabinet.html'

    def get_context_data(self, **kwargs):
        a = self.request.path
        p1, p2 = a.split('s/')
        context = super().get_context_data(**kwargs)
        context['object'] = User.objects.get(username=p2)
        context['user_songs'] = Songs.objects.filter(author_name=p2)
        return context






