from node import (
    Node,
    _all_are_total_flag,
)


class TestNode:
    def test_get_metric(self):
        metrics = ['330267.42', '1406.0']
        node = Node(None, metrics)
        assert node.get_metric(0) == float(metrics[0])
        assert node.get_metric(1) == float(metrics[1])

    def test_parent(self):
        properties_parent = ['womens footwear', '$total', '$total']
        node_parent = Node(properties_parent, None)

        properties_child = ['womens footwear', 'shoes', '$total']
        node_child = Node(properties_child, None)

        assert node_parent.parent(node_child)

    def test_not_parent(self):
        properties_1 = ['womens footwear', '$total', '$total']
        node_1 = Node(properties_1, None)

        properties_2 = ['men footwear', 'shoes', '$total']
        node_2 = Node(properties_2, None)

        assert not node_1.parent(node_2)

    def test_nodes_are_siblings(self):
        properties_1 = ['womens footwear', '$total', '$total']
        node_1 = Node(properties_1, None)

        properties_2 = ['mens footwear', '$total', '$total']
        node_2 = Node(properties_2, None)

        assert node_1.siblings(node_2)
        assert node_2.siblings(node_1)

    def test_nodes_are_siblings_2(self):
        properties_1 = ['womens footwear', 'boots']
        node_1 = Node(properties_1, None)

        properties_2 = ['womens footwear', 'sandals']
        node_2 = Node(properties_2, None)

        assert node_1.siblings(node_2)
        assert node_2.siblings(node_1)

    def test_nodes_are_not_siblings(self):
        properties_1 = ['womens footwear', 'boots', '$total']
        node_1 = Node(properties_1, None)

        properties_2 = ['mens footwear', '$total', '$total']
        node_2 = Node(properties_2, None)

        assert not node_1.siblings(node_2)
        assert not node_2.siblings(node_1)

    def test_nodes_are_not_siblings_2(self):
        properties_1 = ['womens footwear', 'boots', '$total']
        node_1 = Node(properties_1, None)

        properties_2 = ['mens footwear', 'boots', '$total']
        node_2 = Node(properties_2, None)

        assert not node_1.siblings(node_2)
        assert not node_2.siblings(node_1)

    def test__remaining_properties_to_be_siblings_with_both_are_total_flag(self):
        properties_1 = ['$total', '$total']
        properties_2 = ['$total', '$total']

        node = Node(None, None)
        assert node._remaining_properties_to_be_siblings(
            properties_1, properties_2)

    def test__remaining_properties_to_be_siblings_with_both_are_empty(self):
        properties_1 = []
        properties_2 = []

        node = Node(None, None)
        assert node._remaining_properties_to_be_siblings(
            properties_1, properties_2)

    def test__remaining_properties_to_be_siblings_with_different_total(self):
        properties_1 = ['non_total', '$total']
        properties_2 = ['$total', '$total']

        node = Node(None, None)
        assert not node._remaining_properties_to_be_siblings(
            properties_1, properties_2)


def test__all_are_total_flag():
    all_total_flags = ['$total', '$total']
    assert _all_are_total_flag(all_total_flags)


def test__all_are_not_total_flag():
    all_total_flags = ['non_total', '$total']
    assert not _all_are_total_flag(all_total_flags)
