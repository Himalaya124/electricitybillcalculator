from flask import Flask, request, render_template_string
import math

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Electricity Bill Calculator</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        :root {
            --primary: #4CAF50;
            --primary-dark: #388E3C;
            --bg: #f9f9f9;
            --text: #333;
            --card-bg: #fff;
        }

        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', sans-serif;
            background-color: var(--bg);
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            animation: fadeIn 0.6s ease-in;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .container {
            background: var(--card-bg);
            padding: 30px 25px;
            border-radius: 18px;
            box-shadow: 0 6px 30px rgba(0, 0, 0, 0.08);
            max-width: 420px;
            width: 95%;
            text-align: center;
        }

        h2 {
            color: var(--text);
            margin: 10px 0 5px;
        }

        .version {
            font-size: 0.85rem;
            color: #777;
            margin-bottom: 25px;
        }

        input[type="number"] {
            padding: 12px;
            width: 100%;
            border-radius: 8px;
            border: 1px solid #ccc;
            margin-bottom: 20px;
            font-size: 16px;
            outline-color: var(--primary);
        }

        input[type="submit"] {
            padding: 12px 24px;
            background-color: var(--primary);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        input[type="submit"]:hover {
            background-color: var(--primary-dark);
        }

        .result {
            margin-top: 25px;
            font-weight: bold;
            font-size: 1.1rem;
            color: var(--text);
        }

        footer {
            margin-top: 30px;
            font-size: 0.8rem;
            color: #aaa;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Electricity Bill Calculator</h2>
        <div class="version">Version 2.0</div>

        <form method="post" style="display: flex; flex-direction: column; align-items: center; gap: 10px;">
    <input type="number" name="unit" min="0" placeholder="Enter consumed unit" required
        style="padding: 10px; width: 100%; border-radius: 8px; border: 1px solid #ccc; font-size: 16px;">
    
    <div style="display: flex; gap: 10px; flex-wrap: wrap; justify-content: center;">
        <input type="submit" value="Calculate"
            style="padding: 8px 16px; background-color: #4CAF50; color: white; border: none; border-radius: 6px; font-size: 14px; cursor: pointer;">
        
        <a href="https://bpdb.portal.gov.bd/sites/default/files/files/bpdb.portal.gov.bd/page/4a0f045a_1415_45f1_9e7c_02a8ed4f103c/2024-03-01-13-45-740f1fb3c50588f18077bdce93250b9a.pdf" target="_blank"
           style="padding: 8px 16px; background-color: #2196F3; color: white; text-decoration: none; border-radius: 6px; font-size: 14px; display: inline-block;">
            📄 View Tariff Rate
        </a>
    </div>
</form>

        {% if bill is not none %}
        <div class="result">
            Your electricity bill is {{ bill }} Taka only.<br>
        </div>
        {% endif %}
        <footer>
            &copy; {{ year }} Nafis. All rights reserved.
        </footer>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    bill = None
    if request.method == "POST":
        try:
            unit = int(request.form["unit"])
            bill = 0

            while unit != 0:
                if unit > 0 and unit <= 75:
                    bill += unit * 5.26
                    unit = 0
                elif unit >= 76 and unit <= 200:
                    temp = unit - 75
                    unit -= temp
                    bill += temp * 7.20
                elif unit >= 201 and unit <= 300:
                    temp = unit - 200
                    unit -= temp
                    bill += temp * 7.59
                elif unit >= 301 and unit <= 400:
                    temp = unit - 300
                    unit -= temp
                    bill += temp * 8.02
                elif unit >= 401 and unit <= 600:
                    temp = unit - 400
                    unit -= temp
                    bill += temp * 12.67
                elif unit > 600:
                    temp = unit - 600
                    unit -= temp
                    bill += temp * 14.61
                else:
                    return render_template_string(TEMPLATE, bill="Invalid unit")

            bill += 42
            vat = bill * 0.05
            bill += vat
            bill = math.ceil(bill) if bill - int(bill) >= 0.5 else int(bill)

        except:
            bill = "Error in input"

    return render_template_string(TEMPLATE, bill=bill)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=20020)