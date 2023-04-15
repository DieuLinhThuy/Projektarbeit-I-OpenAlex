from neo4j import GraphDatabase
from flask import Flask, render_template, request
from bokeh.plotting import figure
from bokeh.embed import components

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


# Bokeh-Plot definieren
def make_bokeh_plot(data):
    plot = figure(title="Related Works", x_axis_label='Author', y_axis_label='Number of related works')
    x_values = [row['author_name'] for row in data]
    y_values = [len(row['related_works']) for row in data]
    plot.vbar(x=x_values, top=y_values, width=0.5)
    return plot


# Flask-Route definieren
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Suchanfrage hier durchführen
        work_title = request.form['work_title']
        data = get_data(work_title)
        bokeh_plot = make_bokeh_plot(data)

        # Daten für das Bokeh-Plot hier vorbereiten
        script, div = components(bokeh_plot)

        # HTML-Seite mit Suchergebnissen und Bokeh-Plot anzeigen
        return render_template('search_results.html', results=data, script=script, div=div)
    else:
        # Standardseite anzeigen
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=8080)
