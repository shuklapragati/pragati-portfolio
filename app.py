from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key_here' 

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'psshukla2029@gmail.com'  
app.config['MAIL_PASSWORD'] = 'scvwltczaqxhovak'  

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html') 

@app.route('/skill')
def skill():
    return render_template('skill.html')

@app.route('/services') 
def services():
    return render_template('services.html')   

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        msg = Message(subject=f"New Message Form {name}", sender=app.config['MAIL_USERNAME'], recipients=[app.config['MAIL_USERNAME']], body=f"From: {name} <{email}>\n\n{message}")
        mail.send(msg)

        return render_template('contact.html', success=True)

    return render_template('contact.html', success=False)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    # Triggering redeploy
#rebuild render manually
