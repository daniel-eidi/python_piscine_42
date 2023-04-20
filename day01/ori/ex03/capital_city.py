import sys

def capital_city():
  states = {
  "Oregon" : "OR",
  "Alabama" : "AL",
  "New Jersey": "NJ",
  "Colorado" : "CO"
  }
  capital_cities = {
  "OR": "Salem",
  "AL": "Montgomery",
  "NJ": "Trenton",
  "CO": "Denver"
  }
  if (len(sys.argv) != 2):
    sys.exit()
  for city, state in states.items():
    if (city == sys.argv[1]):
      print(capital_cities[state])
      sys.exit()
  print("Unknown state")

if __name__ == '__main__':
  capital_city()
