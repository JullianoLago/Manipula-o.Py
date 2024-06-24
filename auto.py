import os
import shutil

# 1. Criar e escrever em um arquivo
# Primeiro, vamos criar um arquivo chamado 'arquivo_exemplo.txt'.
# Em seguida, escreveremos duas linhas de texto nele.
with open('arquivo_exemplo.txt', 'w') as arquivo:
    arquivo.write("Este é um exemplo de conteúdo para o arquivo.\n")
    arquivo.write("Python é ótimo para manipulação de arquivos!\n")
print("Arquivo criado e dados escritos com sucesso.")

# 2. Ler o conteúdo do arquivo
# Agora, vamos abrir e ler o conteúdo do 'arquivo_exemplo.txt'.
with open('arquivo_exemplo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do arquivo:")
    print(conteudo)

# 3. Renomear o arquivo
# Renomeamos 'arquivo_exemplo.txt' para 'arquivo_renomeado.txt'.
novo_nome = 'arquivo_renomeado.txt'
os.rename('arquivo_exemplo.txt', novo_nome)
print(f"Arquivo renomeado para {novo_nome}.")

# 4. Fazer uma cópia do arquivo
# Em seguida, fazemos uma cópia de 'arquivo_renomeado.txt' chamada 'arquivo_copia.txt'.
copia_nome = 'arquivo_copia.txt'
shutil.copy(novo_nome, copia_nome)
print(f"Arquivo copiado para {copia_nome}.")

# 5. Excluir o arquivo original
# Finalmente, removemos o 'arquivo_renomeado.txt'.
os.remove(novo_nome)
print(f"Arquivo original {novo_nome} excluído.")
