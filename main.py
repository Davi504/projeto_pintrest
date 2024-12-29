from flask import Flask

app = Flask(__name__) 

@app.route('/')
def homepage():
    return 'meu primeiro site com Flask!'

if __name__ == '__main__':
    app.run(debug=True)