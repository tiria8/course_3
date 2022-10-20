from flask import Flask
from functions import get_all, get_by_pk, get_by_skill

DATA_SOURCE = 'candidates.json'

app = Flask(__name__)

@app.route("/")
def page_index():
    data = get_all(DATA_SOURCE)
    result = '<pre>'
    for i in data:
        result += f"""
            Имя кандидата - {i["name"]}
            Позиция кандидата - {i["position"]}
            Навыки - {i["skills"]}
        """
    result += '</pre>'
    return result

@app.route("/candidates/<int:x>")
def page_candidates(x):
    data = get_by_pk(x, DATA_SOURCE)
    url = data[0]["picture"]
    return f"""
           <img src='({url})'>"
           <pre>
           Имя кандидата - {data[0]["name"]}
           Позиция кандидата - {data[0]["position"]}
           Навыки через запятую - {data[0]["skills"]}
           </pre>
    """

@app.route("/skills/<x>")
def page_skills(x):
    data = get_by_skill(x, DATA_SOURCE)
    result = '<pre>'
    for i in data:
        result += f"""
                    Имя кандидата - {i["name"]}
                    Позиция кандидата - {i["position"]}
                    Навыки - {i["skills"]}
                """
    result += '</pre>'
    return result

app.run(debug=True)

