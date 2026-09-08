from http.server import BaseHTTPRequestHandler
import random


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Number Guessing Game</title>
        </head>

        <body>
            <h1>🎯 Number Guessing Game</h1>

            <p>Guess a number between 1 and 100</p>

            <input type="number" id="guess" placeholder="Enter your guess">

            <button onclick="checkGuess()">Guess</button>

            <p id="result"></p>

            <script>
                let answer = Math.floor(Math.random() * 100) + 1;
                let attempts = 0;

                function checkGuess() {
                    let guess = Number(document.getElementById("guess").value);
                    attempts++;

                    if (guess > answer) {
                        document.getElementById("result").innerText =
                            "Too high! Try again.";
                    }
                    else if (guess < answer) {
                        document.getElementById("result").innerText =
                            "Too low! Try again.";
                    }
                    else {
                        document.getElementById("result").innerText =
                            "🎉 You got it! The answer was " + answer +
                            ". Attempts: " + attempts;
                    }
                }
            </script>

        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())