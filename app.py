from flask import Flask, send_from_directory, request, jsonify

app = Flask(__name__, static_url_path='')

lista_pacientes = [
    {
        'id': 1,
        'nome': 'Manuela da Silva',
        'rg': '9845098487',
        'telefone': '(81) 3333-3333',
        'setor': 'Enfermaria',
        'sus': '111-2222-3333-4444-5555'
    },
    {
        'id': 2,
        'nome': 'Arlindo da Silva',
        'rg': '9845098487',
        'telefone': '(81) 3333-3333',
        'setor': 'Ambulatório',
        'sus': '111-2222-3333-4444-5555'
    },
    {
        'id': 3,
        'nome': 'Pedro Vieira',
        'rg': '9845098487',
        'telefone': '(81) 3333-3333',
        'setor': 'COVID-19',
        'sus': '111-2222-3333-4444-5555'
    },
    {
        'id': 4,
        'nome': 'Clara Santana',
        'rg': '9845098487',
        'telefone': '(81) 3333-3333',
        'setor': 'COVID-19',
        'sus': '111-2222-3333-4444-5555'
    },
    {
        'id': 5,
        'nome': 'Elder Lamarck',
        'rg': '9845098487',
        'telefone': '(81) 3333-3333',
        'setor': 'COVID-19',
        'sus': '111-2222-3333-4444-5555'
    },
    {
        'id': 6,
        'nome': 'Diego Moura',
        'rg': '9845098487',
        'telefone': '(81) 3333-3333',
        'setor': 'COVID-19',
        'sus': '111-2222-3333-4444-5555'
    },
    {
        'id': 7,
        'nome': 'Micaela Krolls',
        'rg': '9845098487',
        'telefone': '(81) 3333-3333',
        'setor': 'COVID-19',
        'sus': '111-2222-3333-4444-5555'
    },
    {
        'id': 8,
        'nome': 'Maria Júlia Wayne',
        'rg': '9845098487',
        'telefone': '(81) 3333-3333',
        'setor': 'COVID-19',
        'sus': '111-2222-3333-4444-5555'
    },
    {
        'id': 9,
        'nome': 'Jorge Camara',
        'rg': '9845098487',
        'telefone': '(81) 3333-3333',
        'setor': 'COVID-19',
        'sus': '111-2222-3333-4444-5555'
    },
    {
        'id': 10,
        'nome': 'Felipe Leão',
        'rg': '9845098487',
        'telefone': '(81) 3333-3333',
        'setor': 'COVID-19',
        'sus': '111-2222-3333-4444-5555'
    },
    {
        'id': 11,
        'nome': 'Ricardo FP',
        'rg': '6666666666',
        'telefone': '(81) 6666-6666',
        'setor': 'COVID-19',
        'sus': '111-2222-3333-4444-5555'
    },
]

@app.route('/app/')
def send_index():
    return send_from_directory('.', 'index.html')

@app.route('/app/<path:path>')
def send_static(path):
    return send_from_directory('.', path)

@app.route('/autenticar', methods = ['POST'])
def autenticar():
    obj = request.get_json()
    email = obj['email']
    senha = obj['senha']
    emails_validos = [
        'dovm@cesar.school',
        'elgr@cesar.school',
        'ffcl@cesar.school',
        'jhcc2@cesar.school',
        'pevs@cesar.school',
        'csgg@cesar.school',
        'mk2@cesar.school',
        'mjwps@cesar.school'
    ]
    email_invalido = email not in emails_validos
    senha_invalida = senha != '12345'
    if email_invalido or senha_invalida:
        return jsonify(False)
    return jsonify(True)

@app.route('/pacientes')
def pacientes():
    if 'id' in request.args:
        id = request.args['id']
        for paciente in lista_pacientes:
            if paciente['id'] == int(id):
                return jsonify(paciente)
        return jsonify(None)        
    else:
        return jsonify(lista_pacientes)
