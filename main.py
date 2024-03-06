from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello():
    return """
           <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User</title>
</head>
<body>
    <form action="" method="get">
        <input type="text" name="" id="user">
        <button onclick="user()">Send</button>
    </form>
    <script>
        function user() {
            const Http = new XMLHttpRequest();
            let text = document.getElementById("user").text;
            const url='eldablo81.pythonanywhere.com/user<' + text + '>';
            Http.open("GET", url);
            Http.send();

            Http.onreadystatechange = (e) => {
            console.log(Http.responseText)
            }
        }
    </script>
</body>
</html>
            """

@app.route("/user<user>", methods=["POST", "GET"])
def user(user):
    text = escape(user)
    return(text)

if __name__ == "__main__":
    app.run()