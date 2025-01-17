from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
@app.route("/")

def form():
    return render_template("test1.html") 

@app.route('/submit', methods=['GET'])

def submit():
    action = request.args.get('on_off', "No action selected")
    print(action)
    return f"Action selected :{action}"

@app.route("/data", methods= ["GET"])

def send_data():
    action = request.args.get('action', "No action selected")
    data = {"Input": action}
    return jsonify(data)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
