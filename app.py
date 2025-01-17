from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
@app.route("/")

def form():
    return render_template_string '''

    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>3D Animated Buttons</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background-color: #f8f9fa;
            font-family: Arial, sans-serif;
        }

        .form-container {
            text-align: center;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 10px;
            background: #fff;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        h1 {
            margin-bottom: 20px;
            font-size: 2rem;
            color: #333;
        }

        .btn-3d {
            display: inline-block;
            position: relative;
            padding: 10px 20px;
            font-size: 1.2rem;
            font-weight: bold;
            color: #fff;
            text-decoration: none;
            background-color: #007bff;
            border: none;
            border-radius: 5px;
            transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
            box-shadow: 0 4px 0 #0056b3, 0 8px 15px rgba(0, 0, 0, 0.2);
        }

        .btn-3d:hover {
            transform: translateY(-4px);
            box-shadow: 0 8px 0 #0056b3, 0 12px 20px rgba(0, 0, 0, 0.3);
        }

        .btn-3d:active {
            transform: translateY(2px);
            box-shadow: 0 2px 0 #0056b3, 0 4px 10px rgba(0, 0, 0, 0.2);
        }

        @media (max-width: 768px) {
            h1 {
                font-size: 1.5rem;
            }

            .btn-3d {
                font-size: 1rem;
                padding: 8px 16px;
            }
        }
    </style>
</head>
<body>
    <form action="/submit" method="get" class="form-container">
        <h1>PC managment system</h1>
        <select name="on_off" id="on_off">
            <option value="on">Turn on computers</option>
            <option value="off">Turn off computers</option>
          
          </select>
        <button type="submit" class="btn-3d mb-3">Submit</button>
        <br>
        <!--<button type="submit" id="off" name="off" value="off" class="btn-3d">Turn off</button>-->
    </form>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
    '''

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
