from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# do template se dává všechno html a do static zbytek obrázky a css 
#form patří do template
@app.route("/")
def vitej():
    return render_template("start.html")        


 #name = request.args.get("name") 
 #input_class = request.args.get("class")
 #message = request.args.get("message")
 #return redirect(url_for("result", name=name, form_class=input_class, message=message))
    
@app.route("/form")
def form():
 name = request.form.get("name") #z formuláře vezme jméno
 input_class = request.form.get("class")# z formuláře vezme clasu
 message = request.form.get("message") #z formuláře vezme message
 return redirect(url_for("result", name=name, form_class=input_class, message=message))
            #a vypíše je v html result





if __name__ == "__main__":
    app.run(debug=True) #spouštění flaskové aplikace