'''
Lab 10 QN.2 
Done By: 1802965
'''
import sys

def main():
    sum = 0
    for i in range(2):  # Runs the loop twice, to take in two inputs
        while True:
            try:
                number = int(input(""))
                if isinstance(number, int):
                    sum += number
                break
            except KeyboardInterrupt:
                print("KeyboardInterrupt Detected!!")
                sys.exit()
            except:     # If an invalid number is detected, an exception will be thrown, and the user will need to input again
                print("Invalid Number!")     
    print(sum/2)


if __name__ == "__main__":
    main()