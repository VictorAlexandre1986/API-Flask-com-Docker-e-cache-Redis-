from flask import Flask
from src.controllers.github_controller import github_controller

app = Flask(__name__)

# Registra o blueprint do controller do fetch github
app.register_blueprint(github_controller)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
