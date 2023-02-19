import datetime as dt

d = dt.datetime.now()
print('%04d-%02d-%02d' % (d.year, d.month, d.day))