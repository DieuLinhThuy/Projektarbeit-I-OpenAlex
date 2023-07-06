import networkx as nx
from bokeh.embed import components
from bokeh.models.graphs import from_networkx, NodesAndLinkedEdges, EdgesAndLinkedNodes
from bokeh.models import Plot, Range1d, MultiLine, Circle, HoverTool
from bokeh.palettes import Spectral4
from bokeh.plotting import figure, output_file, show

# create NetworkX-graph
def create_networkx_graph(data):
    G = nx.Graph()
    for row in data:
        G.add_node(row['author_name'], node_type='author')
        G.add_node(row['related_work_title'], node_type='related_work')
        G.add_nodes_from(row['related_works'], node_type='related_work')
        G.add_edge(row['author_name'], row['related_work_title'])
        for related_work in row['related_works']:
            G.add_edge(row['related_work_title'], related_work)
    return G

# create bokeh-plot
def create_bokeh_plot(G):
    plot = Plot(plot_width=800, plot_height=600, title='Knowledge Graph',
                x_range=Range1d(-1.1, 1.1), y_range=Range1d(-1.1, 1.1))

    graph_renderer = from_networkx(G, nx.spring_layout, scale=1, center=(0, 0))

    # configure node glyphs
    graph_renderer.node_renderer.glyph = Circle(size=15, fill_color=Spectral4[0])
    graph_renderer.node_renderer.selection_glyph = Circle(size=15, fill_color=Spectral4[2])
    graph_renderer.node_renderer.hover_glyph = Circle(size=15, fill_color=Spectral4[1])

    graph_renderer.edge_renderer.glyph = MultiLine(line_color="#CCCCCC", line_alpha=0.8, line_width=5)
    graph_renderer.edge_renderer.selection_glyph = MultiLine(line_color=Spectral4[2], line_width=5)
    graph_renderer.edge_renderer.hover_glyph = MultiLine(line_color=Spectral4[1], line_width=5)

    graph_renderer.selection_policy = NodesAndLinkedEdges()
    graph_renderer.inspection_policy = NodesAndLinkedEdges()

    plot.renderers.append(graph_renderer)

    # nodes interactivity
    hover = HoverTool(tooltips=[
        ("Author", "@index"),
        ("Related Work Title", "@related_work_title")
    ])
    plot.add_tools(hover)
    # embed plot into script
    script, div = components(plot)

    return script, div
