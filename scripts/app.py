import os
from neo4j import GraphDatabase
from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv

load_dotenv()

password = os.environ.get("DATABASE_PASSWORD")
username = os.environ.get("DATABASE_USERNAME")
url = os.getenv("DATABASE_URL")
app = Flask(__name__)

# Verbindung zur Neo4j-Datenbank herstellen
driver = GraphDatabase.driver(url, auth=(username, password))

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
    graph = get_knowledge_graph(data)
    plot = Plot(plot_width=800, plot_height=800, x_range=Range1d(-2, 2), y_range=Range1d(-2, 2))

    node_hover_tool = HoverTool(tooltips=[("Name", "@name")])
    plot.add_tools(node_hover_tool, TapTool(), BoxSelectTool(), BoxZoomTool(), ResetTool(), WheelZoomTool())

    graph_renderer = from_networkx(graph, nx.spring_layout, scale=1, center=(0, 0))
    graph_renderer.node_renderer.glyph = Circle(size=15, fill_color="skyblue")
    graph_renderer.node_renderer.hover_glyph = Circle(size=15, fill_color="red")
    graph_renderer.edge_renderer.glyph = MultiLine(line_color="gray", line_alpha=0.8, line_width=1)
    graph_renderer.edge_renderer.hover_glyph = MultiLine(line_color="red", line_alpha=1, line_width=2)

    plot.renderers.append(graph_renderer)

    output_file("knowledge_graph.html")
    show(plot)

    return render_template('table.html', data=data)


if __name__ == "__main__":
    app.run(port=8080)
