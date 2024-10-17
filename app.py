from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

# Configuração da chave da API OpenAI
openai.api_key = '' #Coloque a API dentro das asplas simples

# Função para testar a API OpenAI
def test_api(query_text):
    try:
        # Enviando a solicitação à API OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Modifique o modelo de sua API , no caso utilizado será a gpt-3.5-turbo.
            messages=[
                {
                    "role": "user",
                    "content": f"Me dê uma ideia inovadora para uma startup sobre {query_text}. Responda em português e formate a resposta utilizando negrito para títulos e seções e use '##' para subtítulos. Limite a resposta a no máximo 150 palavras."
                }
            ],
            max_tokens=150,  # Limite de tokens na resposta
            temperature=0.9   # Grau de criatividade
        )

        # Retorna o conteúdo da resposta
        return response

    except Exception as err:
        return {'error': f'Erro inesperado: {err}'}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate-startup', methods=['POST'])
def generate_startup():
    # Recebe o input do usuário do corpo da solicitação
    user_input = request.json.get('input')

    # Chama a função test_api para gerar uma resposta da OpenAI com formatação
    api_response = test_api(user_input)

    # Extrai a mensagem da resposta da API
    if 'choices' in api_response and len(api_response['choices']) > 0:
        response_message = api_response['choices'][0]['message']['content'].strip()

        # Formata a resposta com ## e **
        formatted_message = f"## Ideia:\n**{response_message}**"

        return jsonify({"msg": formatted_message})
    else:
        return jsonify(api_response)


if __name__ == '__main__':
    app.run(debug=True)
