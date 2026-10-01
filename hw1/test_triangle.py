import pytest

from triangle import classify_triangle


# 每個 return 敘述各需一個測試案例：4 個 return → 最少 4 個案例
@pytest.mark.parametrize(
    ("a", "b", "c", "expected"),
    [
        (1, 1, 3, "invalid"),      # line 4
        (2, 2, 2, "equilateral"),  # line 6
        (2, 2, 3, "isosceles"),    # line 8
        (3, 4, 5, "scalene"),      # line 9
    ],
)
def test_classify_triangle(a, b, c, expected):
    assert classify_triangle(a, b, c) == expected
