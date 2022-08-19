def get_metadata(header):
    metrics, properties = [], []
    for column in header:
        if column.startswith('property'):
            properties.append(column)
        else:
            metrics.append(column)
    return metrics, properties
