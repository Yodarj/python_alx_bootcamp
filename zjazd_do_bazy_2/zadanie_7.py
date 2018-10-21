def test_przytnij_1():
    assert przytnij(
        data=[1, 2, 3, 4, 5, 6, 7],
        start=lambda x: x > 3,
        stop=lambda x: x < 6,
    ) == [4, 5, 6]


def test_przytnij_2():
    assert przytnij(
        data=[1, 2, 3, 4, 5, 6, 7],
        start=lambda x: x > 3,
        stop=lambda x: x == 7,
    ) == [4, 5, 6, 7]


def przytnij(data, start, stop):
    out = []
    for i in data:
        if stop(i):
            if start(i):
                out.append(i)
                break
            continue
        elif start(i):
            out.append(i)
    return out

# ----------------------------------------- zrobić w domku, fajne to to