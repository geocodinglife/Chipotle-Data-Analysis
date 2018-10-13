# Step 1 - Import the necessary libraries
import pandas as pd

# Step 2 - Import the dataset from the URL
# Step 3 - Assign the data to variable chipo
chipo = pd.read_csv('chipo.tsv', sep = '\t')
chipo.head(10)

# Step 4 - How many products cost more than $10?
prices_float = pd.Series([float(value[1:-1]) for value in chipo.item_price])
chipo.item_price = prices_float
chipo_filtered = chipo.drop_duplicates(['item_name', 'quantity'])
chipo_one_prod = chipo_filtered[chipo_filtered.quantity == 1]
results = chipo_one_prod[chipo_one_prod.item_price > 10]
print(len(results))

# Step 5 - What is the price of each item?
chipo_filtered = chipo.drop_duplicates(['item_name', 'quantity'])
chipo_one_prod = chipo_filtered[chipo_filtered.quantity == 1]
price_per_item = chipo_one_prod[['item_name', 'item_price']]
price_per_item.sort_values(by = 'item_price', ascending = False).head(20)

# Step 6 - Sort by the name of the item
chipo.item_name.sort_values()

# Step 7 - What was the quantity of the most expensive item ordered?
chipo.sort_values(by = 'item_price', ascending = False).head(1)

# Step 8 - How many times were a Veggie Salad Bowl ordered?
vsb = chipo[chipo.item_name == 'Veggie Salad Bowl']

qty = 0
for i in range(0, len(vsb)):
    qty += vsb.iloc[i, 1]
print(qty)

# Step 9 - How many times people ordered more than one Canned Soda?
soda = chipo[chipo.item_name == 'Canned Soda']
soda = soda[soda.quantity > 1]
print(len(soda))