from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!doctype html>
    <html>
    <head>
        <title>PK's Python Webpage</title>
        <style>
            body { font-family: Arial, sans-serif; background:#f5f5f5; text-align:center; padding:50px; }
            h1 { color:#4f46e5; }
            p { color:#333; }
            a.btn { display:inline-block; margin-top:20px; padding:10px 15px;
                    background:#4f46e5; color:white; text-decoration:none; border-radius:8px; }
        </style>
    </head>
    <body>
        <h1>Welcome to PK's Web Page 🚀</h1>
        <p>This page is served using <b>Python + Flask</b>.</p>
        <a href="/about" class="btn">Go to About Page</a>
    </body>
    </html>
    """

@app.route("/about")
def about():
    return "<h2>About Page</h2><p>This is a simple page made by PK with Python!</p>"

if __name__ == "__main__":
    app.run(debug=True)
