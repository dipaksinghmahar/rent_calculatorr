# Import required modules from Flask
from flask import Flask, render_template, request

# Create Flask application instance
app = Flask(__name__)

# Define route for home page (supports both GET and POST requests)
@app.route("/", methods=["GET", "POST"])
def home():
    # Initialize result variable (will store final output)
    result = None

    # Check if form is submitted (POST request)
    if request.method == "POST":
        # Get user inputs from HTML form and convert to appropriate types
        rent = float(request.form["rent"])                 # Total rent
        food = float(request.form["food"])                 # Food expenses
        electricity_units = float(request.form["electricity"])  # Units consumed
        charge_per_unit = float(request.form["charge"])    # Cost per unit
        persons = int(request.form["persons"])             # Number of people

        # Calculate electricity bill
        total_bill = electricity_units * charge_per_unit

        # Calculate total expense
        total_expense = rent + food + total_bill

        # Avoid division by zero
        if persons > 0:
            # Calculate per person share and round to 2 decimal places
            result = round(total_expense / persons, 2)
        else:
            # Handle invalid input
            result = "Invalid number of persons"

    # Render HTML page and pass result variable to template
    return render_template("index.html", result=result)


# Run the Flask application
if __name__ == "__main__":
    # debug=True enables auto-reload and error messages
    # port=5001 avoids conflict with default port 5000
    app.run(debug=True, port=5001)