from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/encryptedtext" method="post">
            <label for="rot">Rotate by:</label>
            <input type="text" name="rot" />
            <textarea name="text">Enter text here... </textarea>
            <input type="submit"/>
            </form>
        </ul>
    </body>
</html>
"""

@app.route("/", methods = ['GET'])
def index():
    return form

@app.route("/encryptedtext", methods = ['POST'])
def encrypt():
    rot = int(request.form.get('rot'))
    text = request.form.get('text')
    encrypted_string = rotate_string(text, rot)

    print(rot)
    print(text)

    return encrypted_string

app.run()