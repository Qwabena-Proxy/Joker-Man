import pyjokes as pj
print('''Jokes are availble in the following languages;
*English
*German
*Spanish
*Italian
*Galician
*Basque
''')
lang = input('Enter language: ').lower()
language_dict = {
  'english':'en',
  'german':'de',
  'spanish':'es',
  'italian':'it',
  'galician':'gl',
  'basque':'eu'
} 
try:
  lang = language_dict[f'{lang}']
  joke = pj.get_joke(language = lang , category = 'all')
  print(joke)
except:
  print('Language entered is not in the list above..😏😏')
