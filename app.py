from flask import Flask, render_template,url_for

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')
@app.route("/about", methods=['GET'])
def about():
    return render_template('about.html')
@app.route("/contact-us", methods=['GET', 'POST'])
def contact_us():
    return render_template('contact.html')
@app.route("/products", methods=['GET'])
def products():
    return render_template('products.html')
@app.route("/services", methods=['GET'])
def services():
    return render_template('services.html')

if __name__ == '__main__':
    app.run(debug=True)