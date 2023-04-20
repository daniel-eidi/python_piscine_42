def display_number():
  with open("./numbers.txt", 'r') as txt:
    x = txt.read().strip()
    y = x.split(",")
    for num in y:
      print(num)

if __name__ == '__main__':
  display_number()


