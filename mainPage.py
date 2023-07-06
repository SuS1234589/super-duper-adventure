from flask import Flask, render_template, redirect


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home_base.html")

@app.route("/experience/")
def about_us():
    return render_template("experience.html")

@app.route("/career/")
def career():
    return render_template("career.html")


@app.route("/send_email/")
def send_email():
    email = "recipient@example.com"  
    subject = "Please enter your Subject"  
    body = "Please tell us how can we help you!"  
    gmail_url = f"mailto:{email}?subject={subject}&body={body}"

    return redirect(gmail_url)


if __name__ == "__main__":
    app.run(debug= True)

