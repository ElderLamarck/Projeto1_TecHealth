from flask import Flask, send_from_directory, request

app = Flask(__name__, static_url_path='')

@app.route('/app/<path:path>')
def send_static(path):
    email = request.args.get('email')
    passord = request.args.get('password')
    if not email is None and email != 'diegoovmoura@gmail.com':
        return send_from_directory('.', 'firstpage.html')    
    return send_from_directory('.', path)
