def odd(n = 0):
    for i in range(1, n, 2):
        print(i)

print("In odd.... reading args")
args = input()
args = args.split("=")
odd(int(args[1]))
