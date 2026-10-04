from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Automated Docker Deployment</title>
        <style>
            body {
                font-family: Arial;
                text-align: center;
                margin-top: 100px;
                background: #f4f4f4;
            }

            .container {
                background: white;
                padding: 40px;
                margin: auto;
                width: 500px;
                border-radius: 10px;
                box-shadow: 0 0 10px #ccc;
            }

            h1 {
                color: #333;
            }

            .status {
                color: green;
                font-weight: bold;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <h1>Automated Docker Deployment</h1>
            <p class="status">Application is running successfully!</p>
            <p>Deployed using Docker and DevOps CI/CD.</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)