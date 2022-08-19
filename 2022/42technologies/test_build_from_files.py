from filehandler import load
from metadata import get_metadata
from sibling_levels import SiblingLevels
from tree import build_list


def test_big_input():
    test_filepath_input = 'data-big-input.txt'
    test_filepath_output = 'data-big-output.txt'

    input_rows = load(test_filepath_input)
    output_rows = load(test_filepath_output)

    metrics, properties = get_metadata(input_rows[0])

    sibling_levels = SiblingLevels(len(metrics), len(properties), 0)
    sibling_levels.build(input_rows[1:])

    output_node_list = build_list(sibling_levels)
    # Fix different format in the input and output files.
    for node in output_node_list:
        node.metrics = [str(float(metric)) for metric in node.metrics]

    output_list = [properties + metrics] + [
        node.properties + node.metrics for node in output_node_list]

    assert output_list == output_rows
