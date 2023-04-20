import sys

def state():
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
  for state, city in capital_cities.items():
    if (city == sys.argv[1]):
      print(get_state(state, states))
      sys.exit()
  print("Unknown capital city")
  
def get_state(state, states):
  for city , st in states.items():
    if(st == state):
      return city

if __name__ == '__main__':
  state()
