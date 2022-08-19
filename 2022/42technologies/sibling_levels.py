from const import TOTAL_FLAG
from filehandler import parse
from node import Node


class SiblingLevels:
    """A tree abstraction with its levels.

    level_0 are for $total...$total,
    level_1 are for prop1$total...$total-1,
    ...
    level_n are for only properties without $total.
    """
    def __init__(self, n_metrics, n_properties, comparison_metric_index):
        self.n_metrics = n_metrics
        self.n_properties = n_properties
        self.comparison_metric_index = comparison_metric_index
        self.levels = []
        self.output_list = []

    def build(self, rows):
        self.levels = [[] for _ in range(self.n_properties)]
        for row in rows:
            self.insert(row)

    def insert(self, row):
        properties, metrics = parse(row, self.n_properties, self.n_metrics)
        node = Node(properties, metrics)
        if set(properties) == {TOTAL_FLAG}:
            self.levels.append(node)  # Let's keep the total node in the end.
            return
        row_level = _get_row_level(properties)
        self._insert_into_level(node, row_level)

    def _get_group_insertion_index(self, sibling_group, new_node):
        new_index = len(sibling_group)
        for i, node in enumerate(sibling_group):
            new_node_metric = float(new_node.metrics[self.comparison_metric_index])
            node_metric = float(node.metrics[self.comparison_metric_index])
            if new_node_metric > node_metric:
                new_index = i
                break
        return new_index

    def _get_group_metric(self, group):
        return sum(node.get_metric(self.comparison_metric_index) for node in group)

    def _insert_into_level(self, new_node, row_level):
        level = self.levels[row_level]
        insert_group = insert_group_index = None

        for i, sibling_group in enumerate(level):
            # All sibling_group need to be siblings of the new_node.
            if _all_but_not_any(sibling_group, new_node.siblings):
                insert_group = sibling_group
                insert_group_index = self._get_group_insertion_index(
                    sibling_group, new_node)
                break

        if insert_group_index is not None:
            insert_group.insert(insert_group_index, new_node)
        else:  # New group
            insert_group = [new_node]
            level.append(insert_group)


def _all_but_not_any(elements, filter_function):
    filtered = False
    for element in elements:
        if filter_function(element):
            filtered = True
        elif filtered:
            raise ValueError(
                'At least one element was filtered in and one element was not. '
                'It needs all elements filtered in, or none of them.')
    return filtered


def _get_row_level(properties):
    for index, prop in enumerate(properties):
        if prop == TOTAL_FLAG:
            return index - 1
    return index
