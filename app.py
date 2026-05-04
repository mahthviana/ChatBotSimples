from flask import Flask, request, jsonify

# Inicializa o aplicativo Flask
app = Flask(__name__)

# Rota básica (equivalente ao urls.py apontando para uma view)
@app.route('/')
def home():
    return "Servidor do Chatbot Flask está rodando!"

# Rota onde o chatbot vai receber as mensagens
@app.route('/chat', methods=['POST'])
def chat():
    # Pega os dados JSON enviados pelo usuário
    dados = request.json
    mensagem_usuario = dados.get('mensagem', '')

    # Aqui entraria a lógica do seu chatbot (IA, regras, etc)
    resposta_bot = f"Você disse: '{mensagem_usuario}'. Eu sou um bot simples em Flask!"

    # Retorna a resposta em formato JSON
    return jsonify({"resposta": resposta_bot})

# Dá o start no servidor
if __name__ == '__main__':
    # debug=True faz o servidor reiniciar sozinho quando você salva o código
    app.run(debug=True)