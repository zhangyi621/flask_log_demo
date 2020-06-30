from apps import created_app

app = created_app()

if __name__ == '__main__':
    print(app.url_map)
    app.run(host="0.0.0.0", port=9800)
