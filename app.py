from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Prabu's Training | Netsys Infotech</title>
        <style>
          body {
            align-items: center;
            background: #f3f6fb;
            color: #172554;
            display: flex;
            font-family: Arial, sans-serif;
            justify-content: center;
            margin: 0;
            min-height: 100vh;
            text-align: center;
          }
          main {
            background: #fff;
            border-radius: 12px;
            box-shadow: 0 8px 24px #1725541a;
            margin: 24px;
            max-width: 640px;
            padding: 48px 32px;
          }
          h1 { color: #1d4ed8; }
        </style>
      </head>
      <body>
        <main>
          <header><h1>Netsys Infotech</h1></header>
          <h2>Welcome to Prabu's Training</h2>
          <p>Welcome to the home page. We're glad you're here!</p>
        </main>
      </body>
    </html>
    """


if __name__ == "__main__":
    app.run()
