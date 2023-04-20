import sys

def state(var1, states, capital_cities):
  for st, city in capital_cities.items():
    if (city == var1.title()):
      print(city, "is the capital of", get_state(st, states))
      return
  print(var1, " is neither a capital city nor a state")
  
def get_state(state, states):
  for city , st in states.items():
    if(st == state):
      return city

def capital_city(var1):
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
 
  for city, st in states.items():
    if (city == var1.title()):
      print(capital_cities[st], " is the capital of ", var1)
      return
  state(var1, states, capital_cities)
  

def check_run():
  if (len(sys.argv) != 2):
    sys.exit()
  x = sys.argv[1].split(",")
  for str in x:
    if(str.strip()):
      new_str = " ".join(str.strip().split())
      capital_city(new_str)


if __name__ == '__main__':
  check_run()
