from flask import Flask, render_template, request, redirect, url_for # type: ignore
import database

app = Flask(__name__)

# List accommodations
@app.route("/")
@app.route("/accommodation/list")
def list_accommodations():
    accommodations = database.retrieve_accommodations()
    for accommodation in accommodations:
        accommodation["reviews"] = database.retrieve_reviews_by_accommodation(accommodation["id"])
    return render_template("accommodation_list.html", accommodations=accommodations)


# Create accommodation
@app.route("/accommodation/create", methods=['GET', 'POST'])
def create_accommodation():
    if request.method == 'POST':
        data = dict(request.form)
        data["price"] = float(data["price"])
        data["amenities"] = data["amenities"].split(",")
        database.create_accommodation(data)
        return redirect(url_for('list_accommodations'))
    return render_template("accommodation_create.html")

# Update accommodation
@app.route("/accommodation/update/<accommodation_id>", methods=['GET', 'POST'])
def update_accommodation(accommodation_id):
    if request.method == 'POST':
        data = dict(request.form)
        data["price"] = float(data["price"])
        data["amenities"] = data["amenities"].split(",")
        database.update_accommodation(accommodation_id, data)
        return redirect(url_for('list_accommodations'))

    accommodation = database.retrieve_accommodation(accommodation_id)
    return render_template("accommodation_update.html", accommodation=accommodation)

# Delete accommodation
@app.route("/accommodation/delete/<accommodation_id>")
def delete_accommodation(accommodation_id):
    database.delete_accommodation(accommodation_id)
    return redirect(url_for('list_accommodations'))

# List reviews
@app.route("/review/list")
def list_reviews():
    reviews = database.retrieve_reviews()
    return render_template("review_list.html", reviews=reviews)

# Create review
@app.route("/review/create", methods=['GET', 'POST'])
def create_review():
    if request.method == 'POST':
        data = dict(request.form)
        data["rating"] = int(data["rating"])
        database.create_review(data)
        return redirect(url_for('list_accommodations'))
    accommodations = database.retrieve_accommodations()
    return render_template("review_create.html", accommodations=accommodations)

if __name__ == "__main__":
    app.run(debug=True)
