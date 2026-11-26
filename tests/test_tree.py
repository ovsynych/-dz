
import pytest

from derevo import Derevo


def test_create_tree():
    tree = Derevo([10, 5, 15])

    assert len(tree) == 3
    assert tree.inorder() == [5, 10, 15]


def test_dobavit():
    tree = Derevo()

    tree.dobavit(10)
    tree.dobavit(5)
    tree.dobavit(15)

    assert len(tree) == 3
    assert tree.inorder() == [5, 10, 15]


def test_poisk():
    tree = Derevo([10, 5, 15, 3, 7])

    assert tree.poisk(10) is True
    assert tree.poisk(3) is True
    assert tree.poisk(100) is False


def test_contains():
    tree = Derevo([10, 5, 15])

    assert 10 in tree
    assert 5 in tree
    assert 100 not in tree


def test_inorder():
    tree = Derevo([8, 3, 10, 1, 6, 14, 4, 7, 13])

    assert tree.inorder() == [
        1, 3, 4, 6, 7, 8, 10, 13, 14
    ]


def test_preorder():
    tree = Derevo([8, 3, 10, 1, 6, 14, 4, 7, 13])

    assert tree.preorder() == [
        8, 3, 1, 6, 4, 7, 10, 14, 13
    ]


def test_postorder():
    tree = Derevo([8, 3, 10, 1, 6, 14, 4, 7, 13])

    assert tree.postorder() == [
        1, 4, 7, 6, 3, 13, 14, 10, 8
    ]


def test_minimum():
    tree = Derevo([10, 5, 15, 3, 7])

    assert tree.minimum() == 3


def test_maximum():
    tree = Derevo([10, 5, 15, 20, 7])

    assert tree.maximum() == 20


def test_delete_leaf():
    tree = Derevo([10, 5, 15])

    assert tree.udalit(5) is True

    assert tree.inorder() == [10, 15]
    assert len(tree) == 2


def test_delete_one_child():
    tree = Derevo([10, 5, 15, 3])

    assert tree.udalit(5) is True

    assert tree.inorder() == [3, 10, 15]
    assert len(tree) == 3


def test_delete_two_children():
    tree = Derevo([10, 5, 15, 3, 7])

    assert tree.udalit(5) is True

    assert tree.inorder() == [3, 7, 10, 15]
    assert len(tree) == 4


def test_delete_root():
    tree = Derevo([10, 5, 15])

    assert tree.udalit(10) is True

    assert tree.inorder() == [5, 15]
    assert len(tree) == 2


def test_delete_missing_element():
    tree = Derevo([10, 5, 15])

    assert tree.udalit(100) is False

    assert tree.inorder() == [5, 10, 15]
    assert len(tree) == 3


def test_delete_last_element():
    tree = Derevo([10])

    assert tree.udalit(10) is True

    assert len(tree) == 0
    assert tree.inorder() == []
    assert tree.root is None


def test_empty_tree():
    tree = Derevo()

    assert len(tree) == 0
    assert tree.inorder() == []
    assert tree.preorder() == []
    assert tree.postorder() == []

    assert tree.poisk(10) is False


def test_minimum_empty():
    tree = Derevo()

    with pytest.raises(ValueError):
        tree.minimum()


def test_maximum_empty():
    tree = Derevo()

    with pytest.raises(ValueError):
        tree.maximum()


def test_duplicate_values():
    tree = Derevo([10, 5, 15, 10])

    assert len(tree) == 4
    assert tree.inorder() == [5, 10, 10, 15]

    assert tree.poisk(10) is True

    tree.udalit(10)

    assert len(tree) == 3
    assert tree.inorder() == [5, 10, 15]
