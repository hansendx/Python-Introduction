#%%

import time

import pandas
import numpy
import math

from typing import List, Sized

from IPython.display import Markdown
from pandas.api.types import CategoricalDtype

from .weighted_average import weighted_statistics

#%%

mtcars = pandas.read_stata("./mtcars.dta")

array = numpy.empty(101, dtype=numpy.int64)
start = time.time()
print("NumPy value:", array.mean())
end = time.time()
print("NumPy time:", end - start)

start = time.time()
python_list = [int(item) for item in array]
print("Vanilla Python value:", sum(python_list) / len(array))
end = time.time()
print("Vanilla Python time:", end - start)

#%%
numpy_mtcars = mtcars.to_numpy()
#%%
numpy_mtcars.ndim
#%%
numpy_mtcars.size
#%%
numpy_mtcars.shape
#%%
numpy.rot90(numpy_mtcars, k=-1)


#%%
ids = ["{:04d}".format(id) for id in range(1, 2001)]
years = range(1984, 2021)
income_table = pandas.DataFrame({"pid": [], "syear": []})

for year in years:
    income_table = income_table.append(
        pandas.DataFrame({"pid": ids, "syear": [year] * len(ids)})
    )

random_generator = numpy.random.default_rng(42)
income_table["income"] = random_generator.integers(
    low=1000,
    high=10000,
    size=(len(income_table["pid"]),),
)
income_table["weight"] = random_generator.uniform(
    low=1,
    high=2,
    size=(len(income_table["pid"]),),
)

#%%

income_grouped_by = income_table[["syear", "income", "weight"]].groupby(["syear"])
# Calculate weighted average
aggregated = income_grouped_by.apply(
    lambda data_frame: pandas.Series(
        weighted_statistics(
            data_frame[["income"]].to_numpy(), weights=data_frame["weight"]
        ),
        ["mean_income", "sd", "N", "error"],
    )
).reset_index()
# Calculate confidence interval boundaries
aggregated["lower"] = aggregated["mean_income"] - aggregated["error"]
aggregated["upper"] = aggregated["mean_income"] + aggregated["error"]
