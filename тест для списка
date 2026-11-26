
import pytest

from my_list import MyList


def test_append():
    my_list = MyList()

    my_list.append(10)
    my_list.append(20)
    my_list.append(30)

    assert my_list.get(0) == 10
    assert my_list.get(1) == 20
    assert my_list.get(2) == 30


def test_get():
    my_list = MyList()

    my_list.append(10)
    my_list.append(20)

    assert my_list.get(0) == 10
    assert my_list.get(1) == 20


def test_set():
    my_list = MyList()

    my_list.append(10)
    my_list.append(20)

    my_list.set(0, 100)

    assert my_list.get(0) == 100


def test_delit():
    my_list = MyList()

    my_list.append(10)
    my_list.append(20)
    my_list.append(30)

    my_list.delit(1)

    assert my_list.get(0) == 10
    assert my_list.get(1) == 30
    assert my_list.razmer() == 2


def test_delit_first():
    my_list = MyList()

    my_list.append(10)
    my_list.append(20)

    my_list.delit(0)

    assert my_list.get(0) == 20


def test_size():
    my_list = MyList()

    assert my_list.razmer() == 0

    my_list.append(10)
    my_list.append(20)

    assert my_list.razmer() == 2


def test_clear():
    my_list = MyList()

    my_list.append(10)
    my_list.append(20)

    my_list.clear()

    assert my_list.razmer() == 0
    assert my_list.data == []


def test_get_out_of_range():
    my_list = MyList()
    my_list.append(10)

    with pytest.raises(IndexError):
        my_list.get(1)

    with pytest.raises(IndexError):
        my_list.get(-1)


def test_set_out_of_range():
    my_list = MyList()
    my_list.append(10)

    with pytest.raises(IndexError):
        my_list.set(1, 50)


def test_delit_out_of_range():
    my_list = MyList()
    my_list.append(10)

    with pytest.raises(IndexError):
        my_list.delit(1)

    with pytest.raises(IndexError):
        my_list.delit(-1)
