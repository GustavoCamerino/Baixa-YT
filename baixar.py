from yt_dlp import YoutubeDL

def listar_formatos(url):
    """Lista formatos disponíveis e retorna os dados."""
    ydl_opts = {}
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        formatos = info.get('formats', [])
        print("\n=== FORMATOS DISPONÍVEIS ===")
        for f in formatos:
            tamanho = f.get('filesize', 0)
            tamanho_mb = f"{tamanho / (1024*1024):.2f} MB" if tamanho else "?"
            print(f"{f['format_id']:>5} | {f.get('ext', ''):3} | {f.get('resolution', 'audio')} | {f.get('abr', '')}kbps | {tamanho_mb}")
        return formatos

def baixar_video(url, format_id):
    opcoes = {
        'format': format_id,
        'outtmpl': '%(title)s.%(ext)s'
    }
    with YoutubeDL(opcoes) as ydl:
        ydl.download([url])

def baixar_audio(url):
    opcoes = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with YoutubeDL(opcoes) as ydl:
        ydl.download([url])

def menu():
    while True:
        print("\n=== MENU YOUTUBE ===")
        print("1 - Baixar vídeo (escolher qualidade)")
        print("2 - Baixar áudio (MP3)")
        print("0 - Sair")
        opcao = input("Escolha: ")

        if opcao == '1':
            url = input("Digite a URL do vídeo: ")
            listar_formatos(url)
            formato = input("Digite o ID do formato desejado: ")
            baixar_video(url, formato)
        elif opcao == '2':
            url = input("Digite a URL do vídeo: ")
            baixar_audio(url)
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
