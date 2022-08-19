## Running main.py

Python version: 3.10.4

`$ python3 main.py <input-filepath> <output-filepath> <sorting_metric_index>`

`<sorting_metric_index>` must be only the position of the metric index. For example:
`net_sales|net_sales_units`, `net_sales` is `1`, `net_sales_units` is `1`

Example:
`python3 main.py data-big-input.txt data-big-out.txt 0`

## Running tests

[Pytest](https://docs.pytest.org/) is necessary to run the tests

Run all the tests: `pytest .`

## Solution design

1. Read the input file rows and put them into a list.
2. Add each row in the `SiblingLevels` class according to a sibling rule.
3. Traverse the `SiblingLevels` recursively to create the output list and save it
   in an output file.

## SiblingLevels

This is the most important and complex class to build the solution. The goal of
this class is to separate the input rows into similar groups, and each level can
have `M` number of groups. The first level must have only one group due to the nature
of the problem.

* This class holds the `N` levels according to the `N` columns that are the
  **properties**.
  * The first level holds all `property1|$total|$total|...` rows.
  * The second level holds all `property1|property2|$total|$total|...` rows.
  * and so on.
  * The last level holds only the special row `$total|$total|...`.
  * This way, each level removes one `$total` property and adds a specific property.
  * The first level is a single group of `property1|$total|$total|...`. This is why
  we only need one group for this level.

Ex of SiblingLevels:
```
[
  
  [  # Level 0
    [  # Group 0 of the level 0 (Only one group)
      # Siblins rows
      ['womens footwear', '$total', '$total', '330267.42', '1406'],
      ['mens footwear', '$total', '$total', '178959.8', '742'],
      ['accessories', '$total', '$total', '84786.29', '310'],
      ['kids footwear', '$total', '$total', '2757.2', '30'],
      ['product care', '$total', '$total', '2280.9', '240'],
    ],
  ],

  [  # Level 1
    [  # Group 0 of the level 1
      # Siblins rows
      ['womens footwear', 'shoes', '$total', '166186.02', '864'],
      ['womens footwear', 'boots', '$total', '164081.39', '542'],
    ],
    [  # Group 1 of the level 1
      # Siblins rows
      ['mens footwear', 'boots', '$total', '99739.9', '341'],
      ['mens footwear', 'shoes', '$total', '79219.9', '401'],
    ],
    ...
  ],
  
  [  # Level 2
    [  # Group 0 of the level 2
      # Siblins rows
      ['womens footwear', 'shoes', 'sandals', '48355', '209'],
      ['womens footwear', 'shoes', 'sneakers', '40678.91', '272'],
      ...
    ],
    [  # Group 1 of the level 2
      # Siblins rows
      ['womens footwear', 'boots', 'tailored', '42454.92', '121'],
      ['womens footwear', 'boots', 'western', '39314.15', '144'],
      ...
    ],
    ...
  ],
]
```

## Build Tree

After creating a `sibling_level` object we can traverse it and create our output
list by recursively accessing the levels and creating an output list,
the `build_list` code is in `tree.py`.
