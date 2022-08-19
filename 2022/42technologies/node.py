from const import TOTAL_FLAG


class Node:
    """Each node represents a row from the original problem."""
    def __init__(self, properties, metrics):
        self.properties = properties
        self.metrics = metrics

    def __repr__(self):
        return repr(f'Node(properties={self.properties}, metrics={self.metrics})')

    def __hash__(self):
        return hash(self.__repr__())

    def __eq__(self, other):
        return (
            self.properties == other.properties
            and self.metrics == other.metrics)

    def get_metric(self, index):
        return float(self.metrics[index])

    def parent(self, node):
        """It works only for next level nodes."""
        try:
            index = self.properties.index(TOTAL_FLAG)
        except ValueError:  # Leaf node
            return False

        return self.properties[:index] == node.properties[:index]

    def siblings(self, node):
        """Check if nodes are siblings.

        When a property of the sequence differs from nodes,
        we need to check the remaining_properties.

        To be siblings:
        node_1 = [
            same_property_1,
            same_property_2,
            ...,
            different_property_1,  <-- different property from node_2 below
            # The remaining properties below must be $total
            # or there is no list anymore.
            $total,  # Or the remaining list does not exist.
            $total,
            ...
        ]
        node_2 = [
            same_property_1,
            same_property_2,
            ...
            different_property_2,  <-- different property from node_1 above
            # The remaining properties below must be $total
            # or there is no list anymore.
            $total,  # Or the remaining list does not exist.
            $total,
            ...
        ]
        """
        for index, properties in enumerate(zip(self.properties, node.properties)):
            property_1, property_2 = properties
            if property_1 != property_2:
                return self._remaining_properties_to_be_siblings(
                    self.properties[index+1:], node.properties[index+1:])

        # We need at least one property difference.
        # Nodes with the same property mean that they are the same,
        # it is not allowed.
        raise ValueError(
            f'Invalid node properties for self.node ({self.properties}) '
            f'or node ({node.properties})')

    def _remaining_properties_to_be_siblings(self, properties_1, properties_2):
        both_are_total_flag = (
            _all_are_total_flag(properties_1)
            and _all_are_total_flag(properties_2))
        if not both_are_total_flag:
            both_are_empty = not properties_1 and not properties_2
            return both_are_empty
        return True


def _all_are_total_flag(properties):
    return set(properties) == {TOTAL_FLAG}
