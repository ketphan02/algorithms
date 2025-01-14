import matplotlib.pyplot as plt

from benchmarking.evaluations.graphing.line_graph_metadata import LineGraphMetadata


def make_space_above(axes, top_margin=1):
    """
    Adding space on top of the graph
    """
    fig = axes.flatten()[0].figure
    s = fig.subplotpars
    w, h = fig.get_size_inches()

    figh = h - (1 - s.top) * h + top_margin
    fig.subplots_adjust(bottom=s.bottom * h / figh, top=1 - top_margin / figh)
    fig.set_figheight(figh)


def line_graph(graph_data: LineGraphMetadata):
    # Select graph theme
    plt.style.use("bmh")

    # Data security
    if graph_data.data is None:
        raise ValueError("There is no data to graph")

    # Graphing
    fig, ax = plt.subplots(figsize=(9, 5), squeeze=False)
    legends = []
    for curr_data in graph_data.data:
        plt.plot(curr_data.x_data, curr_data.y_data)
        legends.append(curr_data.name)

    # Graph format
    legend = plt.legend(
        legends, bbox_to_anchor=(1.05, 1), loc="upper left", edgecolor="none"
    )
    legend.get_frame().set_alpha(None)
    legend.get_frame().set_facecolor("white")

    if graph_data.title is not None:
        plt.suptitle(graph_data.title, size=20, fontweight="bold", y=0.98)

    if graph_data.description is not None:
        plt.title(graph_data.description, size=13, y=1.05, fontweight="ultralight")

    if graph_data.x_lim is not None:
        plt.xlim([graph_data.x_lim.start, graph_data.x_lim.end])

    if graph_data.y_lim is not None:
        plt.ylim([graph_data.y_lim.start, graph_data.y_lim.end])

    if graph_data.x_label is not None:
        plt.xlabel(graph_data.x_label)

    if graph_data.y_label is not None:
        plt.ylabel(graph_data.y_label)

    make_space_above(ax)

    plt.tight_layout()
    plt.show()
