from django.shortcuts import render
from django.views import View
from .cadastros import CadastroAlbums

# Create your views here.

class AlbumsView(View):
    def get(self, request):
        ultimos_albuns = CadastroAlbums.obter_ultimos_albuns(10)
        context = {'albuns' : ultimos_albuns}
        return render(request, 'index.html', context)
    

class AlbumView(View):
    def get(self, request, id):
        album = CadastroAlbums.obter(id)
        context = {'album' : album}
        return render(request, 'album.html', context)