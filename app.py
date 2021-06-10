from flask import Flask, send_from_directory, request, jsonify

app = Flask(__name__, static_url_path='')

@app.route('/app/')
def send_index():
    return send_from_directory('.', 'index.html')

@app.route('/app/<path:path>')
def send_static(path):
    email = request.args.get('email')
    senha = request.args.get('senha')
    emails_validos = [
        'dovm@cesar.school'
        'elgr@cesar.school'
        'ffcl@cesar.school'
        'jhcc2@cesar.school'
        'pevs@cesar.school'
        'csgg@cesar.school'
        'mk2@cesar.school'
        'mjwps@cesar.school'
    ]
    if not email is None:
        email_invalido = email not in emails_validos
        senha_invalida = senha != '12345'
        if email_invalido or senha_invalida:
            return send_from_directory('.', 'firstpage.html')    
    return send_from_directory('.', path)

@app.route('/pacientes')
def pacientes():
    pacientes = [
        {
            'nome': 'Manuela da Silva',
            'rg': '9845098487',
            'telefone': '(81) 3333-3333',
            'setor': 'Enfermaria',
            'sus': '111-2222-3333-4444-5555'
        },
        {
            'nome': 'Arlindo da Silva',
            'rg': '9845098487',
            'telefone': '(81) 3333-3333',
            'setor': 'Ambulatório',
            'sus': '111-2222-3333-4444-5555'
        },
        {
            'nome': 'Pedro Vieira',
            'rg': '9845098487',
            'telefone': '(81) 3333-3333',
            'setor': 'COVID-19',
            'sus': '111-2222-3333-4444-5555'
        },
        {
            'nome': 'Clara Santana',
            'rg': '9845098487',
            'telefone': '(81) 3333-3333',
            'setor': 'COVID-19',
            'sus': '111-2222-3333-4444-5555'
        },
        {
            'nome': 'Elder Lamarck',
            'rg': '9845098487',
            'telefone': '(81) 3333-3333',
            'setor': 'COVID-19',
            'sus': '111-2222-3333-4444-5555'
        },
        {
            'nome': 'Diego Moura',
            'rg': '9845098487',
            'telefone': '(81) 3333-3333',
            'setor': 'COVID-19',
            'sus': '111-2222-3333-4444-5555'
        },
        {
            'nome': 'Micaela Krolls',
            'rg': '9845098487',
            'telefone': '(81) 3333-3333',
            'setor': 'COVID-19',
            'sus': '111-2222-3333-4444-5555'
        },
        {
            'nome': 'Maria Júlia Wayne',
            'rg': '9845098487',
            'telefone': '(81) 3333-3333',
            'setor': 'COVID-19',
            'sus': '111-2222-3333-4444-5555'
        },
        {
            'nome': 'Jorge Camara',
            'rg': '9845098487',
            'telefone': '(81) 3333-3333',
            'setor': 'COVID-19',
            'sus': '111-2222-3333-4444-5555'
        },
        {
            'nome': 'Felipe Leão',
            'rg': '9845098487',
            'telefone': '(81) 3333-3333',
            'setor': 'COVID-19',
            'sus': '111-2222-3333-4444-5555'
        },
    ]
    return jsonify(pacientes)
