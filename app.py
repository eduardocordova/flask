from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'


@app.route('/')
def home():
    return render_template('index.html')


def chatbot_response(user_text):
    return "Vuelva pronto!"


@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    return chatbot_response(user_text)


if __name__ == '__main__':
    app.run()
