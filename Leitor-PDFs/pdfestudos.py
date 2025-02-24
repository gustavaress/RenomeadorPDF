import PyPDF2
import os
import re

caminho_pasta = r"C:\Users\killy\Downloads\Termos Onboarding Automate"

inicioArquivo = "Termo de Equipamento -2025"

arquivos = os.listdir(caminho_pasta)
for arquivo in arquivos:
      if arquivo.startswith(inicioArquivo):
        caminho_arquivo = os.path.join(caminho_pasta, arquivo)


# Ele meio que cria um objeto que abre o caminho do arquivo e atribui a variavel "arquivo". O rb determina que ele sera aberto em modo binario
with open(caminho_arquivo, "rb") as arquivo:
        # Estou atribuindo o nome de leitor_pdf para essa função que le o arquivo pdf
        leitor_pdf = PyPDF2.PdfReader(arquivo)
        # Defino o texto para vazio, para em seguida adicionar nele o texto do pdf. Faço isso apenas para criar o texto
        texto = ""

        # Aqui estou validando a questão das paginas. Ele vai pegar listar todas as paginas do PDF com o .pages, e depois e repetir para cada pagina por causa do loop "for"
        for paginas in leitor_pdf.pages:
            texto += paginas.extract_text()

# O que eu entendi: Essas letras supostamente "aleatorias" são as letras que podem variar no texto, mas no final, ele expecifica que o padrao do user SEMPRE ira ter o @c6bank.com em seu fim. Ou seja, o padrao do user = "([Qualquer letra, pontuação ou numero]+)@c6bank.com"
padrao_user = r"([a-zA-Z0-9_.+-]+)@c6bank.com"
# Match sera nosso objeto. re.search é uma função da biblioteca re (expressão regular). Basicamente, ele utiliza a expressão regular para fazer a busca nos seguintes parametros. re.search(pattern, string, flags=0) se continuar confuso: re.search(padrão buscado, texto que vc quer buscar o padrão, marcação que no nosso caso faz com que a função ignore se as letras estão em caixa alta ou baixa). Se o padrao for encontrado, match conterá um objeto novo Match. Caso contrário, match será None
match = re.search(padrao_user, texto, re.IGNORECASE)
# Diz que o nome sera igual ao primeiro (e unico) grupo que conseguimos no match, que sera o das letras "aleatorias". Para conseguirmos o email completo, digitamos o grupo 0. O strip ignora espaços em branco, ele faz sentido nesse contexto ja que evita que o email tenha espaços acidentais antes ou depois
nome = match.group(1).strip()

print(nome)