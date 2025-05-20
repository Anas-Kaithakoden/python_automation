import camelot

table = camelot.read_pdf('fifa.pdf', pages='1')

# table.export('fifa.csv', f='csv', compress=True)

table[0].to_csv('fifa.csv')
