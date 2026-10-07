import tabula #import pandas as pd
import pandas #as pd

#use tabula to read pdf file tables
table = tabula.read_pdf("TableText.pdf", pages=0)
print(table[0]) #print pandas dataframe
table[0].to_excel("outputs.xlsx", index=False) #export to excel
print(table[0])

