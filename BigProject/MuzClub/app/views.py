from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, View, TemplateView
from django.http import HttpResponseRedirect, StreamingHttpResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from app.models import Category, Songs, Profile
from django.contrib.auth.models import User
from django.template import RequestContext
from app.forms import SongCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render
from django.db.models import Q


def main_page(request):
    if request.method == "GET":
        return render(request, 'hello.html')

    if request.method == "POST":
        return HttpResponseRedirect('/')


class genre_create_view(LoginRequiredMixin, CreateView):
    fields = ('title',)
    model = Category
    success_url = reverse_lazy('genres')


class genres_list_view(ListView):
    model = Category


def genre_delete(request, pk):
    deleting_genre = Category.objects.get(id=pk)
    deleting_genre.delete()
    return HttpResponseRedirect('/songs/categories')


def genre_detail(request, pk):
    success_url = reverse_lazy('genres')
    category_songs = Songs.objects.filter(category = Category.objects.get(id=pk))
    category_name = Category.objects.get(id=pk).title
    return render(request, 'app/current_genre_list.html', {'category_name': category_name, 'object_list': category_songs, 'some_url': request.path})


class song_detail_view(DetailView):
    model = Songs


def song_list(request):
    if request.method == "GET":
        object_list = None
        if (request.GET.get('sort', None) == None) and (request.GET.get('sort', None) == None):
            object_list = Songs.objects.all()
        if request.GET.get('sort', None) == "date-sort":
            object_list = Songs.objects.all().order_by('date')
        elif request.GET.get('sort', None) == "name-sort":
            object_list = Songs.objects.order_by("name")
        return render(request, 'app/songs_list.html', {'object_list': object_list})


def song_delete(request, pk):
    if request.method == "GET":
        song = Songs.objects.get(id=pk)
        song.delete()
        return HttpResponseRedirect('/songs/')


@login_required
def song_create(request):
    if request.method == "GET":
        form = SongCreationForm()
        form_user = User.objects.get(username=request.user.username)
        return render(request, 'app/songs_form.html', {'form': form, 'form_user': form_user})
    if request.method == "POST":
        New_object = Songs(name=request.POST['name'], category=Category.objects.get(id=request.POST['category']),
                           image=request.FILES.get('image'), file=request.FILES.get('file'), author_name=request.user.username)
        new_file_name = New_object.name + '_' + New_object.author_name
        new_file_name = new_file_name.replace(' ', '_')
        New_object.file.name = new_file_name
        # Валидация
        # -----------
        New_object.save()
        return HttpResponseRedirect('/songs/')


def search_something(request):
    if request.method == "POST":
        query = request.POST.get('text')
        if query == '':
            songs_list = None
            users_list = None
        else:
            songs_list = Songs.objects.all().filter(Q(name=None) | Q(name__icontains=query))
            users_list = User.objects.all().filter(Q(username=None) | Q(username__icontains=query))
        return render(request, 'app/search_result.html', {'object_list': songs_list, 'users_list': users_list})
    return render(request, 'hello.html')


def page_not_found(request, exception):
    return render(request, 'errors/error404.html')


def handler500(request, *args, **argv):
    response = render(request, 'errors/error500.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response



