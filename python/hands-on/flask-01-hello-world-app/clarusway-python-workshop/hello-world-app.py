from flask import Flask

app = Flask(__name__)
@app.route('/')
def head():
    return "Hello World"

@app.route('/ahmet')
def second():
    return "This is the ahmet 's page"

@app.route('/third/subthird')
def third():
    return "this is subpage of third page "

@app.route('/forth/<string:id>')
def forth(id):
    return f'Id of this page {id}'

if __name__ == '__main__':
    app.run(debug=True)



