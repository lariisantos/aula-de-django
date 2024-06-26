from django.shortcuts import render
from django.views import View
from .cadastros import CadastroAlbuns

# Create your views here.

class AlbumsView(View):
    def get(self, request):
        ultimos_albuns = CadastroAlbuns.obter_ultimos_albuns(10)
        context = {'albuns' : ultimos_albuns}
        return render(request, 'firstfm/index.html', context)