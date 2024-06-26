from firstapp.models import Album, Musica

class CadastroAlbums:

    def criar(titulo, artista, genero):
        a = Album()
        a.titulo = titulo
        a.artista = artista
        a.genero = genero
        a.save()
        return a
    
    def obter(id):
        return Album.objects.filter(id=id).first()
    
    def excluir(id):
        a = CadastroAlbums.obter(id)
        a.delete()
    
    def atualizar(id, titulo, artista, genero):
        a = CadastroAlbums.obter(id)
        if a is None:
            raise ValueError('Álbum não existe: id= ',id)
        a.titulo = titulo
        a.artista = artista
        a.genero = genero
        a.save()
    
    def obter_ultimos_albuns(quantidade):
        return Album.objects.order_by("-id")[:quantidade]

class CadastroMusicas:

    def criar(titulo, compositor, duracao, album_id):
        m = Musica()
        m.titulo = titulo
        m.compositor = compositor
        m.duracao = duracao
        m.album = CadastroAlbums.obter(album_id)
        m.save()
        return m
    
    def obter(id):
        return Musica.objects.filter(id=id).first()
    
    def excluir(id):
        m = CadastroMusicas.obter(id)
        m.delete()
    
    def atualizar(id, titulo, compositor, duracao, album_id):
        m = CadastroMusicas.obter(id)
        if m is None:
            raise ValueError('Música não existe: id= ',id)
        m.titulo = titulo
        m.compositor = compositor
        m.duracao = duracao
        m.album = CadastroAlbums.obter(album_id)
        m.save()
        return m