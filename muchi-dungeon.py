import connexion
import os


app = connexion.FlaskApp(__name__)


if __name__ == '__main__':
    app.add_api('muchi-dungeon.yaml')
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
