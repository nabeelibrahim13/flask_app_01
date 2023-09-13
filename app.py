from flask import Flask,render_template,request

app = Flask(__name__)

# @app.route("/")
# def index():
#     return "<h1>Hello Flask</h1>"



@app.route("/about<name>")
def about1(name):
    return f"<h1>Welcome Mr. {name}</h1>"

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/gallery/')
def gallery():
    return render_template('gallery.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        math = float(request.form['Maths'])
        phy = float(request.form['Physics'])
        chem = float(request.form['Chemistry'])
        eng = float(request.form['English'])
        total = math + phy + chem + eng
        avg = total / 4

        return render_template('form.html', score=avg, math=math, phy=phy, chem=chem, eng=eng)

if __name__ == "__main__":
    app.run(debug=True)