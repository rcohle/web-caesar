from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

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
        
        <form action="" method="post">
        
            <label for="rot">Rotate by:</label>
        
            <input type="text" id="rot" name="rot" placeholder="0" />
        
            <textarea name="text"></textarea>
        
            <input type="submit" value="Submit Query" />
        
        </form>

    </body>
</html>"""


@app.route("/")
def index():
    return form


@app.route("/", methods=['POST'])

def encrypt():
    
    rot = request.form['rot']
    rot = int(rot)
    text = request.form['text']
    encrypted_text = rotate_string(text,rot)

    #perform rotate function to get new data
    
    return '<h1>' + encrypted_text + '</h1>'

    # when form is submitted, request will contain rot and text
    # we will use request method to access these
    # use local variables to store the values of the request 
    # paramaters rot and text
    # encrypt the value of the text parameter using rotate_string
    # return encrypted string wrapped in <h1> tags



app.run()


"""The form uses the POST method.
There are two inputs: a regular input with type="text" and a textarea.
Set name="rot" on the input element and name="text" on the textarea.
Has a label on the input element that looks something like the one in the screenshot above.
The input element has the default value of 0.
Has a submit button
1) regular input. first input (name="rot") will show "Rotate by:" 
            followed by a text input for numbers where the default is 0
            2) textarea input. (name="text")will show a large text area for input
            3) submit query button will be below text area
            4) index function will return the form variable"""