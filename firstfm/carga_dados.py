from firstapp.cadastros import CadastroAlbums, CadastroCantor, CadastroMusicas

import csv

# Função para carregar dados do CSV
def load_csv(filename):
    with open(filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

def executa():
    # Carregando dados dos arquivos CSV
    cantores = load_csv("artistas.csv")
    albuns = load_csv("albuns.csv")
    musicas = load_csv("musicas.csv")

    # Exibindo os dados carregados
    print("Artistas:")
    for cantor in cantores:
        CadastroCantor.criar(cantor['Nome'])

    print("\nÁlbuns:")
    for album in albuns:
        CadastroAlbums.criar(album['Nome'], album['Artista_ID'], album['Genero'], album['Ano_Lancamento'])

    print("\nMúsicas:")
    for musica in musicas:
        CadastroMusicas.criar(musica['Nome'], musica['Compositor'], musica['Duracao'], musica['Album_ID'])
