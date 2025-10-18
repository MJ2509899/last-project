from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__, template_folder='src', static_folder='stlyes')

# Routes for each page
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about-us.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/portfolio")
def portfolio():
    return render_template("my-portfolio.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# Example: API endpoint to serve dynamic data
@app.route("/api/projects")
def projects():
    data = [
        {"title": "Project 1", "desc": "Awesome project"},
        {"title": "Project 2", "desc": "Another project"}
    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
