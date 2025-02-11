import html

from src.discord import DiscordLink
from dash import html
from src.nGraph import nGraph


def selection(graph: nGraph, selections):
    """
    Callback for the selection of nodes.

    If the selection is a node we show its image and the job buttons will work with this nodes job id.
    """
    if len(selections["nodes"]) == 0:
        return html.Div([html.H4("No node selected")])

    node = graph.nodes[selections["nodes"][0]]
    if node is None:
        return html.Div([html.H4("No node selected")])

    discord_link = node["node"].getDiscordLink()

    n = node
    depth = 0
    # Get the depth of the node (Nodes between it and its prompt.)
    while n["reference_job_id"]:
        n = graph.nodes[n["reference_job_id"]]
        depth += 1

    # Its not actually that intersting to see the depth; originally done for hierarchical graphs; but they seem to know what to do just fine without it.
    # html.H4('Predecessors:'+str(depth))

    x = []  # clunky way to build x...
    if node["image"]:
        x.append(
            html.Img(
                src="https://storage.googleapis.com/dream-machines-output/"
                + node["id"]
                + "/grid_0.webp",
                style={"max-width": "40vw"},
            )
        )
    x.append(
        html.A(
            html.H4("Goto discord"),
            href=discord_link,
        )
    )
    div = html.Div(
        x,
        style={"right": 0, "position": "absolute"},
    )

    return div
