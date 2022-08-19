from pytest import fixture

from node import Node
from sibling_levels import SiblingLevels


COMPARISON_METRIC_INDEX = 1


@fixture
def node_woman_footwear_total():
    properties = ['womens footwear', '$total', '$total']
    metrics = ['330267.42', '1406.0']
    return Node(properties, metrics)


@fixture
def node_mens_footwear_total():
    properties = ['mens footwear', '$total', '$total']
    metrics = ['178959.8', '742.0']
    return Node(properties, metrics)


@fixture
def node_accessories_total():
    properties = ['accessories', '$total', '$total']
    metrics = ['84786.29', '310.0']
    return Node(properties, metrics)


@fixture
def node_product_care_total():
    properties = ['product care', '$total', '$total']
    metrics = ['2280.9', '240.0']
    return Node(properties, metrics)


@fixture
def node_kids_footwear_total():
    properties = ['kids footwear', '$total', '$total']
    metrics = ['2757.2', '30.0']
    return Node(properties, metrics)


@fixture
def node_new_total_to_end():
    properties = ['new total node to the end', '$total', '$total']
    metrics = ['200.9', '20.0']
    return Node(properties, metrics)


@fixture
def node_new_total_to_beginning():
    properties = ['new total node to the beginning', '$total', '$total']
    metrics = ['999999.5', '999999999.0']
    return Node(properties, metrics)


@fixture
def node_new_total_to_mid():
    properties = ['new total node to the mid', '$total', '$total']
    metrics = ['1000.5', '270.0']
    return Node(properties, metrics)


@fixture
def node_to_new_group():
    properties = ['new total node', 'other pattern', '$total']
    metrics = ['10.5', '1']
    return Node(properties, metrics)


@fixture
def sibling_levels():
    n_properties = 3
    n_metrics = 2
    return SiblingLevels(n_metrics, n_properties, COMPARISON_METRIC_INDEX)


@fixture
def sibling_nodes(
        node_woman_footwear_total,
        node_mens_footwear_total,
        node_accessories_total,
        node_product_care_total,
        node_kids_footwear_total):
    return [
        node_woman_footwear_total,
        node_mens_footwear_total,
        node_accessories_total,
        node_product_care_total,
        node_kids_footwear_total,
    ]


class TestSiblingLevels:
    def test_build(self, sibling_levels):
        properties_1,  = ['prop_1_1', 'prop_1_2', 'prop_1_3'],
        metrics_1 = ['100.1', '10.0']

        properties_2 = ['$total', '$total', '$total']
        metrics_2 = ['10000.1', '1000.0']

        properties_3 = ['prop_3_1', 'prop_3_2', '$total']
        metrics_3 = ['1000.1', '100.0']

        properties_4 = ['prop_4_1', '$total', '$total']
        metrics_4 = ['5000.1', '500.0']

        rows = [
            properties_1 + metrics_1,
            properties_2 + metrics_2,
            properties_3 + metrics_3,
            properties_4 + metrics_4,
        ]

        assert sibling_levels.levels == []
        sibling_levels.build(rows)

        node_1 = Node(properties_1, metrics_1)
        node_2 = Node(properties_2, metrics_2)
        node_3 = Node(properties_3, metrics_3)
        node_4 = Node(properties_4, metrics_4)
        assert_levels = [[[node_4]], [[node_3]], [[node_1]], node_2]

        assert sibling_levels.levels == assert_levels

    def test_insert(self, sibling_levels, sibling_nodes, node_new_total_to_end):
        row = ['new total node to the end', '$total', '$total', '200.9', '20.0']
        sibling_levels.levels = [[sibling_nodes]]
        assertion_levels = [[sibling_nodes[:] + [node_new_total_to_end]]]
        sibling_levels.insert(row)
        assert sibling_levels.levels == assertion_levels

    def test__get_group_insertion_index_returning_first_index(
            self, sibling_nodes, sibling_levels):
        node_to_insert = sibling_nodes[0]
        del sibling_nodes[0]  # Removing first node to be inserted.

        insertion_level = sibling_levels._get_group_insertion_index(
            sibling_nodes, node_to_insert)
        assert insertion_level == 0

    def test__get_group_insertion_index_returning_mid_index(
            self, sibling_nodes, sibling_levels):
        mid_index = len(sibling_nodes)//2
        node_to_insert = sibling_nodes[mid_index]
        del sibling_nodes[mid_index]  # Removing mid-node to be inserted.

        insertion_level = sibling_levels._get_group_insertion_index(
            sibling_nodes, node_to_insert)
        assert insertion_level == mid_index

    def test__get_group_insertion_index_returning_last_index(
            self, sibling_nodes, sibling_levels):
        last_index = len(sibling_nodes)-1
        node_to_insert = sibling_nodes[last_index]
        del sibling_nodes[last_index]  # Removing last node to be inserted.

        insertion_level = sibling_levels._get_group_insertion_index(
            sibling_nodes, node_to_insert)
        assert insertion_level == last_index

    def test__get_group_metric(self, sibling_nodes, sibling_levels):
        sibling_levels.levels = [sibling_nodes]
        assertion_metric = sum(
            node.get_metric(COMPARISON_METRIC_INDEX) for node in sibling_nodes)
        assert sibling_levels._get_group_metric(sibling_nodes) == assertion_metric

    def test__insert_into_level_to_the_end(
            self, sibling_levels, sibling_nodes, node_new_total_to_end):
        # Hierarchy: levels -> groups -> list of sibling_nodes (a group)
        sibling_levels.levels = [[sibling_nodes]]
        assertion_levels = [[sibling_nodes[:] + [node_new_total_to_end]]]

        sibling_levels._insert_into_level(node_new_total_to_end, 0)
        assert sibling_levels.levels == assertion_levels

    def test__insert_into_level_to_the_beginning(
            self, sibling_levels, sibling_nodes, node_new_total_to_beginning):
        sibling_levels.levels = [[sibling_nodes]]
        assertion_levels = [[[node_new_total_to_beginning] + sibling_nodes[:]]]

        sibling_levels._insert_into_level(node_new_total_to_beginning, 0)
        assert sibling_levels.levels == assertion_levels

    def test__insert_into_level_to_the_mid(
            self, sibling_levels, sibling_nodes, node_new_total_to_mid):
        sibling_levels.levels = [[sibling_nodes]]
        mid = (len(sibling_nodes) + 1)//2

        assertion_levels = [
            [
                sibling_nodes[:mid]
                + [node_new_total_to_mid]
                + sibling_nodes[mid:]
            ]
        ]

        sibling_levels._insert_into_level(node_new_total_to_mid, 0)
        assert sibling_levels.levels == assertion_levels

    def test__insert_into_level_to_new_group(
            self, sibling_levels, sibling_nodes, node_to_new_group):
        sibling_levels.levels = [[sibling_nodes]]
        assertion_levels = [[sibling_nodes[:], [node_to_new_group]]]

        sibling_levels._insert_into_level(node_to_new_group, 0)
        assert sibling_levels.levels == assertion_levels
