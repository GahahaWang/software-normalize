import pytest

from hw1.triangle import classify_triangle


# Line coverage：4 個 return 各需一個測試案例 → 最少 4 個案例
@pytest.mark.parametrize(
    ("a", "b", "c", "expected"),
    [
        pytest.param(1, 1, 3, "invalid", id="T1"),      # lines 1, 3, 4
        pytest.param(2, 2, 2, "equilateral", id="T2"),  # lines 1, 3, 5, 6
        pytest.param(2, 2, 3, "isosceles", id="T3"),    # lines 1, 3, 5, 7, 8
        pytest.param(3, 4, 5, "scalene", id="T4"),      # lines 1, 3, 5, 7, 9
    ],
)
def test_line_coverage(a, b, c, expected):
    assert classify_triangle(a, b, c) == expected
