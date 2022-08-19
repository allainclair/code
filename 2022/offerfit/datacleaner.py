"""Instructions:

Fill in the methods of the DataCleaner class to produce the
same printed results as in the comments below. Good luck, and have fun!
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from typing import Dict, Any, List


class DataCleaner:
    """Transform a pandas df while keeping track of the history
    of transformations to allow reverting back to earlier state.
    """
    transactions = {}

    def __init__(self, df: pd.DataFrame):
        self.history = [('Initial df', df)]
        self.current = df

    def adjust_dtype(self, types: Dict[str, Any]) -> None:
        self.current = self.current.astype(types)
        self.history.append(
            (f'Adjusted dtypes using {types}', self.current.copy(deep=True)))

    def impute_missing(self, columns: List[str]) -> None:
        mean = self.current[columns].mean()
        self.current[columns] = self.current[columns].fillna(mean)
        self.history.append(
            (f'Imputed missing in {columns}', self.current.copy(deep=True)))

    def revert(self, steps_back: int = 1) -> None:
        try:
            self.history.pop()
            for _ in range(steps_back):
                _, self.current = self.history.pop()
        except IndexError:
            raise IndexError(
                f'Can not revert {steps_back} steps back. Handle this '
                'exception to get the oldest data frame in self.current')

    def save(self, path: str) -> None:
        # Saving only the self.current
        self.transactions[path] = self.current.copy(deep=True)

    @classmethod  # Changed to classmethod
    def load(cls, path: str) -> DataCleaner:
        # TODO: how to return a DataCleaner that does not have a path?
        current = cls.transactions[path]
        return cls(current)


transactions = pd.DataFrame(
    {
        "customer_id": [10, 10, 13, 10, 11, 11, 10],
        "amount": [1.00, 1.31, 20.5, 0.5, 0.2, 0.2, np.nan],
        "timestamp": [
            "2020-10-08 11:32:01",
            "2020-10-08 13:45:00",
            "2020-10-07 05:10:30",
            "2020-10-08 12:30:00",
            "2020-10-07 01:29:33",
            "2020-10-08 13:45:00",
            "2020-10-09 02:05:21",
        ]
    }
)

transactions_dc = DataCleaner(transactions)

print(f"Current dataframe:\n{transactions_dc.current}")

# Current dataframe:
#    customer_id  amount            timestamp
# 0           10    1.00  2020-10-08 11:32:01
# 1           10    1.31  2020-10-08 13:45:00
# 2           13   20.50  2020-10-07 05:10:30
# 3           10    0.50  2020-10-08 12:30:00
# 4           11    0.20  2020-10-07 01:29:33
# 5           11    0.20  2020-10-08 13:45:00
# 6           10     NaN  2020-10-09 02:05:21

print(f"Current dtypes:\n{transactions_dc.current.dtypes}")

# Initial dtypes:
# customer_id      int64
# amount         float64
# timestamp       object
# dtype: object

transactions_dc.adjust_dtype({"timestamp": np.datetime64})

print(f"Changed dtypes to:\n{transactions_dc.current.dtypes}")

# Changed dtypes to:
# customer_id             int64
# amount                float64
# timestamp      datetime64[ns]

transactions_dc.impute_missing(columns=["amount"])

print(f"Imputed missing as overall mean:\n{transactions_dc.current}")

# Imputed missing as mean:
#    customer_id     amount           timestamp
# 0           10   1.000000 2020-10-08 11:32:01
# 1           10   1.310000 2020-10-08 13:45:00
# 2           13  20.500000 2020-10-07 05:10:30
# 3           10   0.500000 2020-10-08 12:30:00
# 4           11   0.200000 2020-10-07 01:29:33
# 5           11   0.200000 2020-10-08 13:45:00
# 6           10   3.951667 2020-10-09 02:05:21

print(f"History of changes:\n{transactions_dc.history}")

# ** Any coherent structure with history of changes **
# E.g., here's one possibility

# History of changes:
# [('Initial df',    customer_id  amount            timestamp
# 0           10    1.00  2020-10-08 11:32:01
# 1           10    1.31  2020-10-08 13:45:00
# 2           13   20.50  2020-10-07 05:10:30
# 3           10    0.50  2020-10-08 12:30:00
# 4           11    0.20  2020-10-07 01:29:33
# 5           11    0.20  2020-10-08 13:45:00
# 6           10     NaN  2020-10-09 02:05:21), ("Adjusted dtypes using {'timestamp': <class 'numpy.datetime64'>}",    customer_id  amount           timestamp
# 0           10    1.00 2020-10-08 11:32:01
# 1           10    1.31 2020-10-08 13:45:00
# 2           13   20.50 2020-10-07 05:10:30
# 3           10    0.50 2020-10-08 12:30:00
# 4           11    0.20 2020-10-07 01:29:33
# 5           11    0.20 2020-10-08 13:45:00
# 6           10     NaN 2020-10-09 02:05:21), ("Imputed missing in ['amount']",    customer_id     amount           timestamp
# 0           10   1.000000 2020-10-08 11:32:01
# 1           10   1.310000 2020-10-08 13:45:00
# 2           13  20.500000 2020-10-07 05:10:30
# 3           10   0.500000 2020-10-08 12:30:00
# 4           11   0.200000 2020-10-07 01:29:33
# 5           11   0.200000 2020-10-08 13:45:00
# 6           10   3.951667 2020-10-09 02:05:21)]

transactions_dc.save("transactions")
loaded_dc = DataCleaner.load("transactions")
print(f"Loaded DataCleaner current df:\n{loaded_dc.current}")

# Loaded DataCleaner current df:
#    customer_id     amount           timestamp
# 0           10   1.000000 2020-10-08 11:32:01
# 1           10   1.310000 2020-10-08 13:45:00
# 2           13  20.500000 2020-10-07 05:10:30
# 3           10   0.500000 2020-10-08 12:30:00
# 4           11   0.200000 2020-10-07 01:29:33
# 5           11   0.200000 2020-10-08 13:45:00
# 6           10   3.951667 2020-10-09 02:05:21

transactions_dc.revert()
print(f"Reverting missing value imputation:\n{transactions_dc.current}")

# Reverting missing value imputation:
#    customer_id  amount           timestamp
# 0           10    1.00 2020-10-08 11:32:01
# 1           10    1.31 2020-10-08 13:45:00
# 2           13   20.50 2020-10-07 05:10:30
# 3           10    0.50 2020-10-08 12:30:00
# 4           11    0.20 2020-10-07 01:29:33
# 5           11    0.20 2020-10-08 13:45:00
# 6           10     NaN 2020-10-09 02:05:21


def test_current():
    dc = DataCleaner(transactions)
    pd.testing.assert_frame_equal(dc.current, transactions)


def test_input_missing():
    dc = DataCleaner(transactions)
    assert_df = transactions.copy(deep=True)

    dc.impute_missing(columns=['amount'])
    mean = assert_df['amount'].mean()
    assert_df['amount'] = assert_df['amount'].fillna(mean)
    pd.testing.assert_frame_equal(dc.current, assert_df)


def test_revert():
    dc = DataCleaner(transactions)
    assert_df = transactions.copy(deep=True)

    dc.adjust_dtype({'timestamp': np.datetime64})
    dc.impute_missing(columns=['amount'])
    dc.revert(2)

    pd.testing.assert_frame_equal(dc.current, assert_df)


def test_save_load():
    dc = DataCleaner(transactions)
    assert_df = transactions.copy(deep=True)

    dc.save('transactions')
    pd.testing.assert_frame_equal(
        DataCleaner.transactions['transactions'], assert_df)

    pd.testing.assert_frame_equal(
        DataCleaner.load('transactions').current, assert_df)
