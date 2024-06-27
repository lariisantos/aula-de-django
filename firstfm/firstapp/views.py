from django.shortcuts import render
from django.views import View
from .cadastros import CadastroAlbums
from .cadastros import CadastroCantor
from .cadastros import CadastroMusicas

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
    
class HomeView(View):
    def get(self, request):
        ultimos_cantores = CadastroCantor.obter_ultimos_cantores(10)
        ultimos_albuns = CadastroAlbums.obter_ultimos_albuns(10)
        ultimas_musicas= CadastroMusicas.obter_ultimas_musicas(10)
        context = {'albuns' : ultimos_albuns, 'cantores': ultimos_cantores, 'musicas': ultimas_musicas}
        return(request, 'index.html', context)
    

class AvaliacaoMusicaView(View):
    def get(self, request, musica_id, nota):
        if request.user.is_autenticated:
            username = request.username
        CadastroAvaliacoesMusica.criar