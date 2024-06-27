from firstapp.models import Album, Musica, Cantor, avaliacao_musica

class CadastroAlbums:

    def criar(titulo, artista_id, genero, ano_lancamento):
        a = Album()
        a.titulo = titulo
        a.artista = CadastroCantor.obter(artista_id)
        a.genero = genero
        a.ano_lancamento = ano_lancamento
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
    
    def obter_ultimas_musicas(quantidade):
        return Musica.objects.order_by("-id")[:quantidade]

class CadastroCantor:
    def criar (nome):
        c = Cantor()
        c.nome = nome
        c.save()
    
    def obter(id):
        return Cantor.objects.filter(id=id).first()
    
    def excluir(id):
        c = CadastroCantor.obter(id)
        c.delete()

    def atualizar(id, nome):
        c = CadastroCantor.obter(id)
        if c is None:
            raise ValueError('Cantor não existe: id= ',id)
        c.nome = nome
        c.save()
        return c

    def obter_ultimos_cantores(quantidade):
        return Cantor.objects.order_by("-id")[:quantidade]
    
class CadastroAvaliacaoMusica:
    def criar (username, musica_id, nota):
        ava = avaliacao_musica()
        ava.username = username
        ava.musica = CadastroMusicas.obter(musica_id)
        ava.nota = nota
        ava.save()
        return ava
    
    def obter(id):
        return avaliacao_musica.objects.filter(id=id).first()
    
    def obter_avaliacoes_usuario(username):
        return avaliacao_musica.objects.filter(username=username).all()
    