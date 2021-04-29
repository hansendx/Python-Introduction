# %%
import pandas
import numpy

# %%
# Building a DataFrame "by hand"

names = ["Robert", "Ina", "Gerd", "Lena", "Nic", "Noah"]
sex = ["m", "w", "m", "w", "m", "m"]
einkommen = [750, numpy.nan, 1500, None, 1200, 1000]
schule = ["keinen", "Hauptschule", "Gymnasium", "Realschule", "Realschule", "Hauptschule"]
programmierkenntnisse = ["keine", "sehr gute", "gute", "gute", "sehr gute", "keine"]
people = pandas.DataFrame(
    {
        "name": names,
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
# Output some aspects of the DataFrame

print(people)
print("=" * 50)
print(people["sex"])
print("=" * 50)
print(people["programmierkenntnisse"])


# %%
# Drop all rows that contain missings in the columns identified by the keys in the list.
# Pandas treats Pythons standard None and NumPys nan as missing.
people.dropna(subset=["schulabschluss"])

# Drop all rows that contain missings in at least one column.
people.dropna()


#%%
# Replace missings with a value.
series = pandas.Series([2, 3, numpy.nan, None, 4])
print("A series with missing values:\n", series)
print("Replace missings:\n", series.fillna("missing"))
print(
    "Numerical comparisons with missings are always False:\n",
    (series > 0) | (series < 0) | (series == 0),
)


# %%
# Count occurences of category values.

people["sex"].value_counts()

# %% An incomplete table

people_without_einkommen = people.drop("einkommen", axis=1)
people_without_einkommen

# %% Another differently incomplete table
people_without_schulabschluss = people.drop("schulabschluss", axis=1)
people_without_schulabschluss

# %%

pandas.merge(
    people_without_einkommen,
    people_without_schulabschluss,
    on=["name"],
    how="inner",
)

# %%
