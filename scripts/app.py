from neo4j import GraphDatabase
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Verbindung zur Neo4j-Datenbank herstellen
uri = "bolt://localhost:7687"
user = "neo4j"
password = "Flora2049%"
driver = GraphDatabase.driver(uri, auth=(user, password))

# Abfrage der Daten aus der Datenbank
def get_data(work_title):
    with driver.session() as session:
        result = session.run("""
            MATCH (w:Work {title: $work_title})<-[:AUTHORED]-(a:Author)-[:AUTHORED]->(relatedWork:Work)
            OPTIONAL MATCH (relatedWork)<-[:RELATED_TO]-(r:RelatedWork)
            RETURN w.title AS work_title, a.name AS author_name, relatedWork.title AS related_work_title, collect(r.id) AS related_works
        """, {"work_title": work_title})

        return [dict(row) for row in result]


# Flask-Route definieren
@app.route('/')
def index():
    return render_template('index.html')


# Flask-Route definieren
@app.route('/works', methods=['POST'])
def search_work():
    work_title = request.form['work_title']
    return redirect(f'/works/{work_title}')


@app.route('/works/<string:work_title>')

def show_related_works(work_title):
    data = get_data(work_title)
    print(data)
    return render_template('table.html', data=data)

if __name__ == '__main__':
    app.run(port=8080)
