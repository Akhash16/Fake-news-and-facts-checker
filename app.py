from flask import Flask,render_template,request

app = Flask(__name__,template_folder='templates')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search.html")
def search():
    return render_template("search_v2.html")

@app.route("/search_query",methods=['POST','GET'])
def store():
    query = request.form.get('user_query')
    return query


if __name__ == '__main__':
    app.run(port=5000,debug=True)