from flask import Flask,render_template,request

app=Flask(__name__,template_folder='templates')
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('test2.html')

@app.route('/?search=hello',methods=['GET','POST'])
def search():
    msg = request.form.get('user_query')
    return msg

if __name__ == '__main__':
    app.run(port=5000,debug=True)