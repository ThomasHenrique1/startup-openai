## Startup OpenAI
Este projeto é uma aplicação web que utiliza a API do OpenAI para gerar ideias inovadoras de startups com base em temas fornecidos pelo usuário. O backend é implementado em Flask, permitindo uma interface simples e intuitiva.

## Funcionalidades

- Gera ideias de startups com base em temas fornecidos.
- Exibe o resultado formatado com negrito e subtítulos.
- Backend em Flask.
- Frontend simples com HTML, CSS e JavaScript.

## Estrutura do Projeto
```bash
startup-openai/
│
├── app.py                   # Arquivo principal usando API do OpenAI
├── static/                  # Pasta para arquivos estáticos (CSS e JS)
│   ├── style/               # Pasta para arquivos CSS
│   │   └── style.css        # Arquivo CSS personalizado
│   └── js/                  # Pasta para arquivos JavaScript
│       └── index.js         # Código JavaScript para requisições AJAX
│
├── templates/               # Pasta para templates HTML
│   └── index.html           # Frontend HTML principal
│
├── requirements.txt         # Lista de dependências do projeto
└── README.md                # Documentação do projeto

```
## Vídeo Explicativo

[![Assista ao vídeo explicativo](https://img.youtube.com/vi/Dfsghuq31vI/maxresdefault.jpg)](https://youtu.be/Dfsghuq31vI)


## Requisitos

- Python 3.x
- Flask
- Requests
- Conta na OpenAI (para usar a API do GPT)

## Instalação

> Clone o repositório:

```bash 
git clone https://github.com/seu-usuario/startup-idea-generator.git
cd startup-idea-generator
```

> Crie um ambiente virtual e ative-o:

```bash
python -m venv venv
source venv/bin/activate  
```
> Instale as dependências:

```bash
pip install -r requirements.txt
```
> Crie um arquivo .env (opcional para manter sua chave da API segura) ou defina diretamente no código sua chave da API.

- No caso da OpenAI, insira sua chave no código onde estiver escrito `YOUR_OPENAI_API_KEY`.

- No caso da RapidAPI, insira a chave no código onde estiver `YOUR_RAPIDAPI_KEY`.

## Estrutura dos Arquivos

- `app.py`: Contém a lógica para gerar ideias de startup usando a API do OpenAI.

- `index.html`: Interface onde o usuário insere um tema e recebe a ideia gerada.

- `index.js`: Lida com requisições AJAX, enviando o tema para o backend e recebendo a resposta.

## Considerações

- O uso da API do OpenAI está sujeito a limites de requisição e custos, dependendo do seu plano.
- Para teste, você pode verificar as documentações e as opções de uso gratuito.


## Contato

Se você tiver dúvidas ou sugestões, entre em contato com [Thomas Henrique](mailto:thomasnhenrique@gmail.com).
