from flask import Flask, request, render_template, jsonify
from flask_mail import Mail, Message
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
import os

# Загрузка переменных окружения из .env файла
load_dotenv()

app = Flask(__name__)

# Конфигурация Flask-Mail из переменных окружения
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS') == 'True'
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')
app.config['UPLOAD_FOLDER'] = os.getenv('UPLOAD_FOLDER')

mail = Mail(app)

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html', mail_username=app.config['MAIL_USERNAME'])

@app.route('/send_mail', methods=['POST'])
def send_mail():
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    msg = Message(subject, sender=app.config['MAIL_DEFAULT_SENDER'], recipients=[email])
    msg.body = message

    # Сохранение и прикрепление файлов
    for file in request.files.getlist('attachments[]'):
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            with app.open_resource(filepath) as fp:
                msg.attach(filename, file.content_type, fp.read())

    mail.send(msg)

    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(debug=True)
