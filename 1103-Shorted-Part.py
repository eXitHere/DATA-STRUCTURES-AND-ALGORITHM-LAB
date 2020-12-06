def shortest(graph, start, stop, path, dis, min_):
    if start == stop and (min_ == None or
                          (dis <= min_[1] and len(path) <= len(min_[0]))):
        min_ = [path, dis]
        return min_

    for a in graph.get(start, []):
        if a[0] not in path:
            tmp = shortest(graph, a[0], stop, path + [a[0]], dis + a[1], min_)
            if tmp is not None:
                min_ = tmp

    return min_


if __name__ == '__main__':

    inp, case = input('Enter : ').split('/')

    graph = {}
    for a in inp.split(','):
        a = a.split()
        graph[a[0]] = graph.get(a[0], []) + [[a[2], int(a[1])]]

    for b in case.split(','):
        b = b.split()
        path = shortest(graph, b[0], b[1], [b[0]], 0, None)
        if path is None:
            print('Not have path :', b[0], "to", b[1])
            continue
        print(b[0], 'to', b[1], ': ' + '->'.join(path[0]))