from bokeh.io import show, output_file
from bokeh.models import Plot, Range1d, MultiLine, Circle, HoverTool, BoxZoomTool, ResetTool
from bokeh.models.graphs import from_networkx, NodesAndLinkedEdges, EdgesAndLinkedNodes
from bokeh.palettes import Spectral4
import networkx as nx

def get_knowledge_graph(data):
    G = nx.Graph()
    edges = []

    for row in data:
        G.add_edge(row['author_name'], row['related_work_title'])
        for related_work in row['related_works']:
            edges.append((row['related_work_title'], related_work))

    G.add_edges_from(edges)

    plot = Plot(plot_width=800, plot_height=600, x_range=Range1d(-1.1, 1.1), y_range=Range1d(-1.1, 1.1))

    node_hover_tool = HoverTool(tooltips=[("Name", "@index")])
    plot.add_tools(BoxZoomTool(), ResetTool(), node_hover_tool)

    node_size = 30
    node_color = Spectral4[0]
    node_hover_color = Spectral4[1]

    node_renderer = from_networkx(G, nx.spring_layout, scale=1, center=(0, 0))

    node_renderer.node_size = node_size
    node_renderer.node_color = node_color
    node_renderer.hover_glyph = Circle(size=node_size, fill_color=node_hover_color)
    node_renderer.selection_glyph = Circle(size=node_size, fill_color=node_hover_color)

    node_renderer.nonselection_glyph = Circle(size=node_size, fill_alpha=0.2, fill_color=node_color)
    node_renderer.glyph.properties_with_values()

    plot.renderers.append(node_renderer)

    edge_renderer = from_networkx(G, nx.spring_layout, scale=1, center=(0, 0))
    edge_renderer.edge_color = "#cccccc"
    edge_renderer.selection_glyph = MultiLine(line_color=Spectral4[1], line_width=3)
    edge_renderer.hover_glyph = MultiLine(line_color=Spectral4[2], line_width=2)
    edge_renderer.nonselection_glyph = MultiLine(line_alpha=0.2, line_color="#cccccc")
    edge_renderer.glyph.properties_with_values()

    plot.renderers.append(edge_renderer)

    node_and_edge_hover_tool = HoverTool(tooltips=[("Name", "@index")])
    plot.add_tools(BoxZoomTool(), ResetTool(), node_and_edge_hover_tool)

    plot.renderers.append(node_renderer)
    plot.renderers.append(edge_renderer)

    output_file("knowledge_graph.html")
    show(plot)
