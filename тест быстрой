
import pytest

from fast_sort import fast_sort


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
def test_fast_sort(values):
    assert fast_sort(values.copy()) == sorted(values)


def test_fast_sort_does_not_change_original():
    values = [5, 2, 3, 1]

    fast_sort(values)

    assert values == [5, 2, 3, 1]
