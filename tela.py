import requests
import tkinter as tk

import os
# Obtenha a sua chave de acesso da API do GitHub e insira-a aqui
API_KEY = os.environ("TOKEN_GITHUB")

# O URL da API para editar o arquivo README
API_URL = "https://api.github.com/repos/SEU_USUARIO/SEU_REPOSITORIO/contents/README.md"

# Função para enviar uma solicitação PATCH para a API do GitHub com as novas alterações
def edit_readme(text):
  headers = {"Authorization": f"Bearer {API_KEY}"}
  data = {"message": "Editando o README", "content": text}
  response = requests.patch(API_URL, headers=headers, json=data)
  if response.status_code == 200:
    print("README editado com sucesso!")
  else:
    print(f"Erro ao editar o README: {response.status_code}")

# Criação da janela da GUI
window = tk.Tk()
window.title("Editor de README")

# Criação do campo de texto para inserir o novo conteúdo do README
text_field = tk.Text(window)
text_field.pack()

# Criação do botão de envio
submit_button = tk.Button(window, text="Enviar", command=lambda: edit_readme(text_field.get("1.0", "end")))
submit_button.pack()

# Execução da janela da GUI
window.mainloop()
