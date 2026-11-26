
import pytest

from buble_sort import buble_sort


@pytest.mark.parametrize("values", [
    [],
    [1],
    [3, 1, 2],
    [1, 2, 3],
    [3, 2, 1],
    [2, 1, 2],
    [-3, 0, -1],
    [4, 4, 4, 4],
    [5, 2, 3, 4, 5, 4],
    [-10, 5, 0, -5, 10],
])
def test_buble_sort(values):
    assert buble_sort(values.copy()) == sorted(values)


def test_buble_sort_changes_original():
    values = [5, 2, 3, 1]

    result = buble_sort(values)

    assert result == [1, 2, 3, 5]
    assert values == [1, 2, 3, 5]
