from flask import Flask, request, render_template_string
import math

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Electricity Bill Calculator</title>
    <style>
        body { font-family: Arial; text-align: center; padding: 40px; }
        .header { border-top: 2px solid #000; border-bottom: 2px solid #000; padding: 10px; margin-bottom: 30px; }
    </style>
</head>
<body>
    <div class="header">
        <h2>Welcome to the Electricity Bill Calculator</h2>
        <p>Created by Nafis</p>
        <p>Version 1.1</p>
    </div>

    <form method="post">
        <label>Enter consumed unit:</label>
        <input type="number" name="unit" min="0" required>
        <input type="submit" value="Calculate">
    </form>

    {% if bill is not none %}
        <p><strong>Your electricity bill is {{ bill }} taka only. Please pay it on time.</strong></p>
    {% endif %}
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
    app.run(host='0.0.0.0', port=10000)
