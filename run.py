from api import app
from api.user_list_api import user_list_api

app.register_blueprint(user_list_api)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
