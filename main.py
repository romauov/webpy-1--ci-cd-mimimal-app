from app.app import app


if __name__ == '__main__':
    from os import environ
    port = environ.get("PORT", 8888)
    app.run(host='0.0.0.0', port=port, debug=True)