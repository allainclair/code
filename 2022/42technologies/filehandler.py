import csv

DELIMITER = '|'


def load(filepath):
    with open(filepath) as csvfile:
        return [row for row in csv.reader(csvfile, delimiter=DELIMITER)]


def save(filepath, header, node_output_list):
    with open(filepath, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=DELIMITER)
        writer.writerow(header)
        for node in node_output_list:
            writer.writerow(node.properties + node.metrics)

    # with open(filepath) as csvfile:
    #     return [row for row in csv.reader(csvfile, delimiter='|')]


def parse(row, n_properties, n_metrics):
    """Separate the properties and metrics of a row."""
    return row[:n_properties], row[n_properties:n_properties+n_metrics]
