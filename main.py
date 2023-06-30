from flask import Flask
import googlecloudprofiler

# Initialize the profiler
try:
    googlecloudprofiler.start(verbose=3)
except (ValueError, NotImplementedError) as exc:
    print(exc)  # Handle errors here

app = Flask(__name__)

@app.route("/")
def hello():
    """Return a friendly HTTP greeting."""
    return "Hello World!"

# This code will only be executed when running the application in a production environment
if __name__ == "__main__":
    app.run()
