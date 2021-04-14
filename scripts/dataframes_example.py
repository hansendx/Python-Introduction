# %%
import pandas
import numpy

# %%

names = ["Hans", "Ina", "Gerd", "Lena", "Nic", "Noah"]
sex = ["m", "w", "m", "w", "m", "m"]
einkommen = [750, numpy.nan, 1500, None, 1200, 1000]
schule = ["keinen", "Hauptschule", "Gymnasium", "Realschule", "Realschule", "Hauptschule"]
programmierkenntnisse = ["keine", "sehr gute", "gute", "gute", "sehr gute", "keine"]
people = pandas.DataFrame(
    {
        "names": names,
        "einkommen": einkommen,
        "schulabschluss": schule,
        "programmierkenntnisse": programmierkenntnisse,
    }
)

people["sex"] = pandas.Series(sex).astype("category")
people["schulabschluss"] = people["schulabschluss"].astype("category")
people["programmierkenntnisse"] = people["programmierkenntnisse"].astype("category")
people["programmierkenntnisse"].cat.reorder_categories(
    ["keine", "gute", "sehr gute"], ordered=True, inplace=True
)

# %%

print(people)
print("=" * 50)
print(people["sex"])
print("=" * 50)
print(people["programmierkenntnisse"])


# %%

people.dropna(subset=["schulabschluss"])

#%%
series = pandas.Series([2, 3, numpy.nan, None, 4])
print("A series with missing values:\n", series)
print("Replace missings:\n", series.fillna("missing"))
print(
    "Numerical comparisons with missings are always False:\n",
    (series > 0) | (series < 0) | (series == 0),
)


# %%

people["sex"].value_counts()
