import PyPDF2
import os
import re

# Caminho Documento
caminho_arquivo_termo = r"C:\Users\killy\Downloads\Termos Onboarding Automate\Termo de Equipamento -2025  (5).pdf"

# Abrir e Ler PDF
with open(caminho_arquivo_termo,"rb") as arquivo:
    leitor_pdf = PyPDF2.PdfReader(arquivo)
    texto = ""
    for pagina in leitor_pdf.pages:
        texto += pagina.extract_text()

    print(texto)

# # Expressão regular para encontrar o nome após o e-mail
# padrao_nome = r"gustavo\.tavares@c6bank\.com\s*([A-Z][a-z]+(?:\s[A-Z][a-z]+)+)"

# # Buscar o nome no texto extraído
# match = re.search(padrao_nome, texto, re.IGNORECASE)

# if match:
#     nome_extraido = match.group(1).strip()

#     # Adicionar " Termo Onboarding 2025.pdf" ao final do nome
#     novo_nome = f'{nome_extraido} Termo Onboarding 2025.pdf'

#     # Definir novo caminho
#     novo_caminho_arquivo = os.path.join(os.path.dirname(caminho_arquivo_termo), novo_nome)

#     # Renomear arquivo
#     os.rename(caminho_arquivo_termo, novo_caminho_arquivo)

#     print(nome_extraido)