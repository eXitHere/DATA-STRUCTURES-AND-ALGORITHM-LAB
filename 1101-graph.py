if __name__ == "__main__":
    #inp = "A B,C D,E F,A C,A D,H G".split(",")
    inp = input("Enter : ").split(",")
    graph = {}
    all_ = set()
    for x in inp:
        y = x.split()
        all_.add(y[0])
        all_.add(y[1])
        if not graph.get(y[0]):
            graph[str(y[0])] = [y[1]]
        else:
            graph[str(y[0])] = graph[str(y[0])] + [y[1]]
    all_ = sorted(all_)
    print("   ", '  '.join(all_))
    for x in all_:
        print(x, ": ", end='')
        if graph.get(x) is None:
            print('0, ' * (len(all_) - 1) + '0', end='')
        else:
            for idx in range(len(all_)):
                if all_[idx] in graph.get(x):
                    print(1, end='')
                else:
                    print(0, end='')
                if idx != len(all_) - 1:
                    print(", ", end='')
        print()
