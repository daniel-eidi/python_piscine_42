import sys

def my_sort():
  d = {
  'Hendrix' : '1942',
  'Allman' : '1946',
  'King' : '1925',
  'Clapton' : '1945',
  'Johnson' : '1911',
  'Berry' : '1926',
  'Vaughan' : '1954',
  'Cooder' : '1947',
  'Page' : '1944',
  'Richards' : '1943',
  'Hammett' : '1962',
  'Cobain' : '1967',
  'Garcia' : '1942',
  'Beck' : '1944',
  'Santana' : '1947',
  'Ramone' : '1948',
  'White' : '1975',
  'Frusciante': '1970',
  'Thompson' : '1949',
  'Burton' : '1939',
  }
  d = dict(sorted(d.items()))
  dict_sort = sorted(d.items(), key=lambda x:x[1])
  for x in dict_sort:
   print(x[0])
  # # print(dict(dict_sort));

  # new_list = sorted([v, k] for (k, v) in d.items())
  # for x in new_list:
  #   print(x[1])
    
if __name__ == '__main__':
  my_sort()
