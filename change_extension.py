import os
import sys

def trocar_extensao(caminho):
    # Verifica se a pasta existe
    if not os.path.isdir(caminho):
        print("A pasta especificada não existe.")
        return

    # Lista todos os arquivos na pasta
    arquivos = os.listdir(caminho)

    # Itera sobre todos os arquivos
    for arquivo in arquivos:
        if arquivo.endswith('.webp'):
            # Renomeia o arquivo trocando a extensão para .png
            novo_nome = os.path.join(caminho, os.path.splitext(arquivo)[0] + '.png')
            os.rename(os.path.join(caminho, arquivo), novo_nome)
            print(f"{arquivo} foi renomeado para {os.path.basename(novo_nome)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <caminho_para_pasta>")
        sys.exit(1)

    caminho_pasta = sys.argv[1]
    trocar_extensao(caminho_pasta)
