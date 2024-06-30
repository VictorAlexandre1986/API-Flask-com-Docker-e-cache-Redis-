from flask import Blueprint, request


github_blueprint = Blueprint('Consultando_repo', __name__)


@github_blueprint.route('/get', methods=['GET'])
def fetch_repo():
    try:
        url = 'https://api.github.com/users/VictorAlexandre1986/repos'

        response = request.get(url)

        if response.status_code == 200:
            repos = response.json()
            repositorios=[]
            for repo in repos:
                repositorio={
                    "name" : repo.get('name'),
                    "html_url" : repo.get('html_url'),
                    "language" : repo.get('language')
                }
                repositorios.append(repositorio)
            return repositorios
        else:
            print(f'Failed to fetch data. Status code: {response.status_code}')
    except Exception as e:
        print(f'Failed to fetch data. Error: {e}')
