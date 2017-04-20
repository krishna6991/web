from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Album

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name= 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('musci:index')



#
# from django.shortcuts import render, get_object_or_404
# from django.http import Http404
# from django.http import HttpResponse
# from django.template import loader
# from .models import Album
# # Create your views here.
#
# def index(request):
#     all_albums=Album.objects.all()
#     # html = ''
#     template = loader.get_template('music/index.html')
#     context = {
#         'all_albums':all_albums,
#     }
#     return render(request, 'music/index.html', context)
#     # return HttpResponse(template.render(context, request))
#
#     # for album in all_album:
#     #     url = '/music/' + str(album.id) + '/'
#     #     html += '<a href = "' + url + '">' + album.album_title + '</a><br>'
#
#     # return HttpResponse(html)
#     # return HttpResponse("<h1>This is the music app homepage</h1>")
#
# def detail(request, album_id):
#     #return HttpResponse("<h2>Detail of album id: " + str(album_id) + "</h2>")
#     # try:
#     #     album = Album.objects.get(pk=album_id)
#     # except Album.DoesNotExist:
#     #     raise Http404("ALbum does not exist")
#     album = get_object_or_404(Album, pk=album_id)
#     return render(request, 'music/detail.html', {'album':album})
#
#
# def favorite(request, album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     try:
#         selected_song = album.song_set.get(pk=request.POST['song'])
#     except (KeyError, Song.DoesNotExist):
#         return render(request, 'music/detail.html', {
#         'album':album,
#         'error_message':"you have not selected any valid song",
#         })
#     else:
#         selected_song.is_favorite = True
#         selected_song.save()
#         return render(request, 'music/detail.html', {'album':album})
