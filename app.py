from flask import Flask,render_template,jsonify

PROJECTS=[
    {
        "id": 1,
        "title": "Portfolio",
        "lang": "HTML5, CSS3, Bootstrap, Python, Flask"
    },
    {
        "id": 2 ,
        "title": "Salesfoece UI Clone",
        "lang": "HTML5, CSS3"
    },
    {
        "id": 3,
        "title": "Password Manager",
        "lang": "Python"
    },
    {
        "id": 4,
        "title": "Multi App friendly QR Code Generator",
        "lang": "Python"
    },
    {
        "id": 5,
        "title": "Quiz Management System like KBC",
        "lang": "Python"
    },
    {
        "id": 6,
        "title": "Rent Calculator",
        "lang": "Python"
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
        "bt_icon": "  X  "
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