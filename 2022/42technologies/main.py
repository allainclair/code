import sys

from filehandler import (
    load,
    save,
)
from metadata import get_metadata
from sibling_levels import SiblingLevels
from tree import build_list


def main():
    input_filepath, output_filepath, sorting_metric_index = get_parameters(
        sys.argv)

    sales = load(input_filepath)
    metrics, properties = get_metadata(sales[0])  # Sales header

    if sorting_metric_index >= len(metrics):
        raise SystemExit(
            '<sorting_metric_index> must be less the size of the metrics. '
            f'len(metrics)={len(metrics)}, '
            f'sorting_metric_index={sorting_metric_index}. Exiting...')

    sibling_levels = SiblingLevels(
        len(metrics), len(properties), sorting_metric_index)
    sibling_levels.build(sales[1:])
    output_node_list = build_list(sibling_levels)

    save(output_filepath, sales[0], output_node_list)


def get_parameters(args):
    try:  # Input file, output file, chosen metric.
        return args[1], args[2], int(args[3])
    except IndexError:
        raise SystemExit(
            'Please use: $ python3 main.py <input-filepath> <output-filepath> '
            '<sorting_metric_index> Exiting...')
    except ValueError:
        raise SystemExit(
            'Please use: $ python3 main.py <input-filepath> <output-filepath> '
            '<sorting_metric_index> and <sorting_metric_index> must be an integer. '
            f'Your <sorting_metric_index>="{args[3]}". Exiting...')


if __name__ == '__main__':
    main()
