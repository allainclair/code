## Summary

It requests
[https://www.beautylish.com/rest/interview-product/list](https://www.beautylish.com/rest/interview-product/list)
and displays a list of products according to some constraints, 
see `Beautylish - Software Engineering Code Interview.pdf` for more context.

## Running Environment

### Python version used

* Python 3.10.4

### Running main application and Python dependencies

* You can run: `python3 .` to run the main code without any dependency installed.
  The list of (unique) products will be shown in the standard output sorted by
  price and name with a summary at the end.

```
List of unique products:

Brand name:     Wonderful Widgets
Product name:   Another Widget
Product price:  $10.00

Brand name:     Acme
Product name:   Anvil
Product price:  $10.00

Brand name:     Wonderful Widgets
Product name:   Widget 3000
Product price:  $10.00

Brand name:     Acme
Product name:   Giant Anvil
Product price:  $99.99

Brand name:     Acme
Product name:   Mini Anvil
Product price:  $99.99

Brand name:     Wonderful Widgets
Product name:   Most Wonderful Widget
Product price:  $99.99

Brand name:     Hooli
Product name:   Nucleus
Product price:  $99.99

Summary:
Total number of unique products: 7
Total number of unique brands: 3
Average price: 61.42
```

* To run the test suit you need [Pytest](https://docs.pytest.org/) installed
  and run `pytest .`

* Use [Poetry](https://python-poetry.org/) to manage the packages and check 
  `pyproject.toml` to see the dependencies if you prefer.

* The `test/test_get_all_products.py` uses the main function `get_all_products` to
test end-to-end the constraints of the application.
