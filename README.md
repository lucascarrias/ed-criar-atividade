# ED Criar Atividade

Script básico para quem tem preguiça de criar as pastas e nomear os arquivos de acordo com o solicitado pelo professor Fabio

### Instalar

  1. Clonar repositorio\
    `$ git clone https://github.com/LucasCarrias/ed-criar-atividade ~/.ed-criar-atividade`

  2. Abrir as configs do terminal\
    `$ sudo nano ~/.bashrc` or `$ sudo nano ~/.zshrc`

  3. Adicionar codigo nas configs do terminal\
    ```
    function ed-ca() {
      python3 -B ~/.ed-criar-atividade/ED_criar_pasta_linux.py
    }
    ```
  4. Atualizar terminal\
    `$ source ~/.bashrc` or `$ source ~/.zshrc`

### Usar

`$ cd <pasta-alvo>`\
`$ ed-ca`

### Contribuir

`$ git clone https://github.com/LucasCarrias/ed-criar-atividade`\
`$ cd ed-criar-atividade`\
`$ pip install -r requirements.txt`
