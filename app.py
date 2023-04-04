import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        input_text = request.form["input_text"]
        print("input is ", input_text)
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=input_text,
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)

####
#def generate_prompt(input_text):
#    return """Suggest three names for an animal that is a superhero.

#Animal: Cat
#Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
#Animal: Dog
#Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
#Animal: {}
#Names:""".format(
#        animal.capitalize()
#   )
#####

if __name__ =='__main__':
    app.run(host='172.31.31.40',port=5000)
#if __name__ =='__main__':
#    app.run(debug=True)