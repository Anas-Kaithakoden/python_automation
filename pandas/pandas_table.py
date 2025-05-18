import pandas as pd

table_data = pd.read_html('https://en.wikipedia.org/wiki/Family_Guy')



table_data.to_html("data.html", index=False)
