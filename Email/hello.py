from threading import Thread

from flask import Flask, render_template
from flask_mail import Mail
from flask_script import Manager
from flask_mail import Message


app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.163.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'rmslangying@163.com'
app.config['MAIL_PASSWORD'] = 'rms147258'
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <flasky@example.com>'

mail = Mail(app)
manager = Manager(app)

def send_async_email(app, msg):
    with app.app_context():
        mail.send_message(msg)

def send_mail(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                    sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)

    # mail.send(msg)
    thread = Thread(target=send_async_email, args=[app, msg])
    thread.start()
    return thread



if __name__ == '__main__':
    manager.run()