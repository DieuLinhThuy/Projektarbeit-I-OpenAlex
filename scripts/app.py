import os
import networkx as nx
from bokeh.embed import components
from bokeh.models.graphs import from_networkx, NodesAndLinkedEdges, EdgesAndLinkedNodes
from bokeh.models import Plot, Range1d, MultiLine, Circle, HoverTool
from bokeh.models.graphs import from_networkx
from bokeh.palettes import Spectral4
from bokeh.plotting import figure, output_file, show
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
# Abfrage der Daten aus der Datenbank
def get_data(work_title):
    with driver.session() as session:
        result = session.run("""
            MATCH (w:Work)
            WHERE toLower(w.title) CONTAINS toLower($work_title)
            MATCH (w)<-[:AUTHORED]-(a:Author)-[:AUTHORED]->(relatedWork:Work)
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

    # Erstellen eines Graphen mit Hilfe von NetworkX
    G = nx.Graph()
    for row in data:
        G.add_node(row['author_name'])
        G.add_node(row['related_work_title'])
        G.add_edge(row['author_name'], row['related_work_title'])

    # Erstellen des Bokeh-Plots
    plot = Plot(plot_width=800, plot_height=600, title='Knowledge Graph',
            x_range=Range1d(-1.1, 1.1), y_range=Range1d(-1.1, 1.1))

    graph_renderer = from_networkx(G, nx.spring_layout, scale=1, center=(0, 0))

    graph_renderer.node_renderer.glyph = Circle(size=15, fill_color=Spectral4[0])
    graph_renderer.node_renderer.selection_glyph = Circle(size=15, fill_color=Spectral4[2])
    graph_renderer.node_renderer.hover_glyph = Circle(size=15, fill_color=Spectral4[1])

    graph_renderer.edge_renderer.glyph = MultiLine(line_color="#CCCCCC", line_alpha=0.8, line_width=5)
    graph_renderer.edge_renderer.selection_glyph = MultiLine(line_color=Spectral4[2], line_width=5)
    graph_renderer.edge_renderer.hover_glyph = MultiLine(line_color=Spectral4[1], line_width=5)

    graph_renderer.selection_policy = NodesAndLinkedEdges()
    graph_renderer.inspection_policy = NodesAndLinkedEdges()

    plot.renderers.append(graph_renderer)

    script, div = components(plot)

    return render_template('table.html', data=data, script=script, div=div, target_id='knowledge-graph')


if __name__ == "__main__":
    app.run(port=8080)