import os
import networkx as nx
from bokeh.embed import components
from bokeh.models.graphs import from_networkx, NodesAndLinkedEdges, EdgesAndLinkedNodes
from bokeh.models import Plot, Range1d, MultiLine, Circle, HoverTool
from bokeh.palettes import Spectral4
from bokeh.plotting import figure, output_file, show
from neo4j import GraphDatabase
from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv

from graph import create_networkx_graph, create_bokeh_plot
from database import get_data

load_dotenv()

# get access to database
password = os.environ.get("DATABASE_PASSWORD")
username = os.environ.get("DATABASE_USERNAME")
url = os.getenv("DATABASE_URL")
app = Flask(__name__)

# create connection to Neo4j database
driver = GraphDatabase.driver(url, auth=(username, password))

# Flask-Route for homepage
@app.route('/')
def index():
    return render_template('index.html')

# flask-route for searching works
@app.route('/works', methods=['POST'])
def search_work():
    work_title = request.form['work_title']
    return redirect(f'/works/{work_title}')

@app.route('/works/<string:work_title>')
def show_related_works(work_title):
    try:
        # get data from neo4j
        data = get_data(work_title)

        # create graph from graph.py
        G = create_networkx_graph(data)

        # create bokeh-plot from graph.py
        script, div = create_bokeh_plot(G)

        return render_template('table.html', data=data, script=script, div=div, target_id='knowledge-graph')
    # error message wip
    except Exception as e:
        return render_template('error.html', error=str(e))


if __name__ == "__main__":
    app.run(port=8080, debug=True)
