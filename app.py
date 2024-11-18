from flask import Flask,render_template,jsonify

PROJECTS=[
    {
        "id": 1,
        "title": "Portfolio",
        "lang": "HTML5, CSS3, Bootstrap, Python, Flask",
        "link": "https://github.com/Undriling/Portfolio"
    },
    {
        "id": 2,
        "title": "IBC-A Latest News Update Web Application",
        "lang": "HTML5, CSS3, Bootstrap, JavaScript",
        "link": "https://github.com/Undriling/IBC-Latest-News-Updates-Website"
    },
    {
        "id": 3,
        "title": "Latest Weather Forecast Web Application",
        "lang": "HTML5, CSS3, JavaScript",
        "link": "https://github.com/Undriling/Weather-App"
    },
    {
        "id": 4,
        "title": "Calculator",
        "lang": "JavaScript",
        "link": "https://github.com/Undriling/Calculator"
    },
    {
        "id": 5,
        "title": "Salesfoece UI Clone",
        "lang": "HTML5, CSS3",
        "link": "https://github.com/Undriling/Salesforce-Clone-UI"
    },
    {
        "id": 6,
        "title": "Password Manager",
        "lang": "Python",
        "link": "https://github.com/Undriling/Password-Manager"
    },
    {
        "id": 7,
        "title": "Multi App friendly QR Code Generator",
        "lang": "Python",
        "link": "https://github.com/Undriling/Multi-app-friendly-UPI-QR-Code-Generator-With-Setting-an-Amount"
    },
    {
        "id": 8,
        "title": "Quiz Management System like KBC",
        "lang": "Python",
        "link": "https://github.com/Undriling/Quize-Management-System-Like-KBC"
    }
]

# Social Item 
SOCIALS=[
    {
        "id": 1,
        "title": "Linkdin",
        "link": "https://www.linkedin.com/in/manash-baruah-mb",
        "bt_icon": ".in"
    },
    {
        "id": 2,
        "title": "Github",
        "link": "https://github.com/Undriling",
        "bt_icon": "git",
    },
    {
        "id": 3,
        "title": "Twitter",
        "link": "https://x.com/ManashBaruah22",
        "bt_icon": "  𝕏  "
    }
]

app = Flask(__name__)
@app.route('/')
def hello_manash():
    return render_template('home.html', projects=PROJECTS, socials=SOCIALS)

# API 
@app.route('/api/projects')
def list_projects():
    return jsonify(PROJECTS)



if __name__=="__main__":
    app.run(debug=True)