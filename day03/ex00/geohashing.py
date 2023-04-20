import antigravity
import sys

def main():
    if len(sys.argv) == 4 :
        try:
            antigravity.geohash(float(sys.argv[1]), float(sys.argv[2]), sys.argv[3].encode('UTF-8'))
        except Exception as error:
            print(error)      

    else:
        print("Invalid number of args, try again")

if __name__ == '__main__':
    main()

