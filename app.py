from flask import Flask, render_template, request, redirect
import csv

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("main_page.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

#photos
@app.route("/photos")
def photos():
    return render_template("photos.html")

#quotes
quotes = csv.reader(open("static/svc-s/quotes.csv", 'r'))
quote_list = {}
for quote, author in quotes:
    quote_list[quote] = author 


@app.route("/quotes")
def quotes():
    return render_template("quotes.html", quotes=quote_list)

@app.route("/ml")
def ml():
    return render_template("ml.html")


#writing
writing_list = csv.reader(open("static/svc-s/writings.csv", 'r'))
writings = {}
for title, writing in writing_list:
    writings[title] = writing

@app.route("/cmd", methods=['GET', 'POST'])
def cmd():
    return render_template("cmd.html", writings = writings, writing_to_retrieve=None)

@app.route("/retrieve", methods=["POST"])
def retrieve():
    retrieve_name = request.form.get("writing_draft_form")

    # to not show error if erred
    if retrieve_name not in writings:
         return (" ", 204) 
    else:
        writing_to_retrieve = writings[retrieve_name]
        return render_template("cmd.html", writings=writings, writing_to_retrieve = writing_to_retrieve)

@app.route("/save", methods=['GET', 'POST'])
def save():
    if request.method=='POST':
        print(request.form['cmd'])
        writing_content = request.form['cmd']
        writing_name = 'namell'
        #writing_list[writing_name] = writing_content    #saving in dict. need it?
        with open("static/svc-s/writings.csv", "a") as file:
            writer=csv.writer(file)
            writer.writerow((writing_name, writing_content))
    return(" ", 204 )


    csv sucks, try saving in txt
    https://stackoverflow.com/questions/27913261/python-storing-data