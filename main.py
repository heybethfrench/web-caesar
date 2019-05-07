from flask import Flask, request, render_template
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods = ['GET'])
def index():
    return render_template('index.html')

@app.route("/encryptedtext", methods = ['POST'])
def encrypt():
    rot = int(request.form.get('rot'))
    text = request.form.get('text')
    encrypted_string = rotate_string(text, rot)

    print(rot)
    print(text)

    return render_template('index.html', encrypted_string=encrypted_string)

app.run()