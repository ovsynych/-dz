
import pytest

from my_array import Array


def test_append():
    arr = Array()

    arr.append(10)
    arr.append(20)
    arr.append(30)

    assert arr.get(0) == 10
    assert arr.get(1) == 20
    assert arr.get(2) == 30


def test_get():
    arr = Array()

    arr.append(10)
    arr.append(20)

    assert arr.get(0) == 10
    assert arr.get(1) == 20


def test_set():
    arr = Array()

    arr.append(10)
    arr.append(20)

    arr.set(1, 100)

    assert arr.get(1) == 100


def test_delit():
    arr = Array()

    arr.append(10)
    arr.append(20)
    arr.append(30)

    assert arr.delit() == 30
    assert arr.razmer() == 2
    assert arr.get(1) == 20


def test_size():
    arr = Array()

    assert arr.razmer() == 0

    arr.append(10)
    arr.append(20)

    assert arr.razmer() == 2

    arr.delit()

    assert arr.razmer() == 1


def test_get_out_of_range():
    arr = Array()
    arr.append(10)

    with pytest.raises(IndexError):
        arr.get(1)

    with pytest.raises(IndexError):
        arr.get(-1)


def test_set_out_of_range():
    arr = Array()
    arr.append(10)

    with pytest.raises(IndexError):
        arr.set(1, 50)

    with pytest.raises(IndexError):
        arr.set(-1, 50)


def test_delit_empty():
    arr = Array()

    with pytest.raises(IndexError):
        arr.delit()
