from datetime import date
today = date.today()
# get full month name
thisMonth = today.strftime('%B').lower()

name = input('what is your name? ')
month = '' # empty to trigger while loop
months = [
  'january', 
  'febuary', 
  'march', 
  'april',
  'may',
  'june',
  'july',
  'august',
  'september',
  'october',
  'november',
  'december'
]

while month not in months:
  if ((month != '') & (month not in months)):
    print(' '.join(months))
  month = input('What month were you born? ').lower()

print('You entered ' + str(name) + ' and it is ' + str(len(name)) + ' characters long.') 
if (month == thisMonth):
  print('Happy birthday month!')