
import pytest

from my_deque import Deque


def test_appendright():
    d = Deque()

    d.appendright(10)
    d.appendright(20)

    assert d.data == [10, 20]


def test_appendleft():
    d = Deque()

    d.appendleft(10)
    d.appendleft(20)

    assert d.data == [20, 10]


def test_delitleft():
    d = Deque()

    d.appendright(10)
    d.appendright(20)
    d.appendright(30)

    assert d.delitleft() == 10
    assert d.data == [20, 30]


def test_delitright():
    d = Deque()

    d.appendright(10)
    d.appendright(20)
    d.appendright(30)

    assert d.delitright() == 30
    assert d.data == [10, 20]


def test_mixed_operations():
    d = Deque()

    d.appendright(10)
    d.appendleft(20)
    d.appendright(30)

    assert d.data == [20, 10, 30]

    assert d.delitleft() == 20
    assert d.delitright() == 30

    assert d.data == [10]


def test_if_pusto():
    d = Deque()

    assert d.if_pusto() is True

    d.appendright(10)

    assert d.if_pusto() is False


def test_razmer():
    d = Deque()

    assert d.razmer() == 0

    d.appendright(10)
    d.appendleft(20)

    assert d.razmer() == 2

    d.delitleft()

    assert d.razmer() == 1


def test_perviy():
    d = Deque()

    d.appendright(10)
    d.appendright(20)

    assert d.perviy() == 10


def test_posledniy():
    d = Deque()

    d.appendright(10)
    d.appendright(20)

    assert d.posledniy() == 20


def test_delitleft_empty():
    d = Deque()

    with pytest.raises(IndexError):
        d.delitleft()


def test_delitright_empty():
    d = Deque()

    with pytest.raises(IndexError):
        d.delitright()


def test_perviy_empty():
    d = Deque()

    with pytest.raises(IndexError):
        d.perviy()


def test_posledniy_empty():
    d = Deque()

    with pytest.raises(IndexError):
        d.posledniy()
