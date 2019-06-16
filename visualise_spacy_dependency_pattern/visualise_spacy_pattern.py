from visualise_spacy_dependency_pattern import util
import pydot


DEFAULT_NODE_ATTRS = {
    'color': 'purple',
    'shape': 'box',
    'style': 'rounded',
    'fontname': 'palatino',
    'fontsize': 10,
    'penwidth': 2
}


def get_node_text(pattern_element):
    feature_dict = util.get_feature_dict(pattern_element)
    feature_text = ['{0} - {1}'.format(k, v) for k, v in feature_dict.items()]
    feature_text = '\n'.join(feature_text)
    node_text = feature_text
    return node_text


def to_pydot(pattern):
    graph = pydot.Dot(graph_type='graph')

    # Create and add nodes
    node_objects = {}
    for pattern_element in pattern:
        node_name = util.get_node_name(pattern_element)
        node_text = get_node_text(pattern_element)
        plot_attrs = {
            **DEFAULT_NODE_ATTRS,
            'name': node_text,
        }
        node = pydot.Node(**plot_attrs)
        node_objects[node_name] = node
        graph.add_node(node)

    # Add edges
    for pattern_element in pattern:
        nbor_name = util.get_nbor_name(pattern_element)
        if not nbor_name:
            continue
        node_name = util.get_node_name(pattern_element)
        node = node_objects[node_name]
        nbor = node_objects[nbor_name]
        rel = util.get_rel(pattern_element)
        if not rel:
            continue
        if rel == '>':
            edge = pydot.Edge(nbor, node)
        elif rel == '<':
            edge = pydot.Edge(node, nbor)
        else:
            print('Warning: rel type {} unhandled. Results maybe be incorrect.'.format(rel))
            edge = pydot.Edge(node, nbor)
        graph.add_edge(edge)

    return graph