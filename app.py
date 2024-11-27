from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")



# name = request.args.get("name") 
# input_class = request.args.get("class")
# message = request.args.get("message")

#     return redirect(url_for("result", name=name, form_class=input_class, message=message))
    


# name = request.form.get("name")
# input_class = request.form.get("class")
# message = request.form.get("message")

#     return redirect(url_for("result", name=name, form_class=input_class, message=message))
    





if __name__ == "__main__":
    app.run(debug=True) #spouštění flaskové aplikace