import cv2
from flask import Flask, render_template, Response, request, redirect, url_for, session,send_file
import Main
import shutil
import os
from werkzeug.utils import secure_filename



app = Flask(__name__, template_folder="./templates")


@app.route("/", methods=["GET", "POST"])
@app.route("/homepage", methods=["GET", "POST"])
def homepage():
    return render_template("home.html")


# <---------- OBJECT DETECTION ---------->#


@app.route("/object-detection")
def object_detection():
    return render_template("object_detect.html")


@app.route("/object_Machine")
def object_Machine():
    Main.Obj_command()
    return render_template("object_detect.html")


# <---------- OBJECT DETECTION END ---------->#


# <---------- VQA ---------->#

@app.route("/vqa")
def vqa():
    return render_template("vqa.html")

@app.route("/vqa_Machine")
def vqa_Machine():
    Main.vqa_command()
    return render_template("vqa.html")





# <---------- VQA END ---------->#


# <---------- ID ---------->#

# @app.route("/id_creater")
# def id_creater():
#     return render_template("id_create.html")
#
# @app.route("/id_create_Machine")
# def id_create_Machine():
#     Main.id_creater()
#     return render_template("demo.html")
#




# <---------- ID END ---------->#



# <---------- CONTACT US---------->#

@app.route("/contact")
def contact():
    return render_template("contact.html")


# <---------- CONTACT US END ---------->#


@app.route("/download")
def download_file():
  shutil.make_archive("Weights", 'zip', "./static/images/img")
  path="Weights.zip"
  return send_file(path,as_attachment=True)

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
