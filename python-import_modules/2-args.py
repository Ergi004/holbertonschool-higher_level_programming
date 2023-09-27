#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    numArgv = len(sys.argv) - 1
    if numArgv == 0:
        print("0 arguments.")
    elif numArgv == 1:
        print("1 argument:")
    else:
        print(f"{numArgv} arguments:")
    for i in range(numArgv):
        print(f"{i + 1}: {sys.argv[i + 1]}")
