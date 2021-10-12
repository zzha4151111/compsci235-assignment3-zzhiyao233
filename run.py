from app import app

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
