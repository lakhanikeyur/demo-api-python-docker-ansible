from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():

    # For handling different types of error cases like
    # e.g. errors in key or value 
    try:

      caption = "area"
      if request.method == 'POST':
        output = float(request.form["width"]) * float(request.form["length"])
      else:
        output = float(request.args["width"]) * float(request.args["length"])

    except:
      caption = "Error"
      output ="Requires integer or float input with width and length as key in lower case characters."

    result={
      caption:output
    }
    return jsonify(result)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)