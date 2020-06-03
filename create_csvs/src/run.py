from partition import run
import sys

if __name__ == "__main__":
    path = '.'
    print("Try to start main\n")

    if len(sys.argv) == 2:
        run(sys.argv[1], sys.argv[1].split('.')[0] + "Output.csv")
    elif len(sys.argv) == 3:
        run(sys.argv[1], sys.argv[2])
    else:
        print("bad input must be two or three!!")
        sys.exit(1)
    print("Finish!!\n")
