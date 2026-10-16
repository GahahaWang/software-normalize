# 作業二：Line Coverage

組別／組員：（請填寫）

- 測試目標：Line coverage（使用最少的測試案例達到測試目標涵蓋率 100%）
- 待測程式：沿用作業一的 [hw1/triangle.py](../hw1/triangle.py)
- 測試程式：[test_line_coverage.py](test_line_coverage.py)
- 測試工具：pytest + pytest-cov（coverage.py）

## 待測程式

```python
1  def classify_triangle(a: int, b: int, c: int) -> str:
2      """依三邊長回傳三角形種類：invalid / equilateral / isosceles / scalene。"""
3      if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
4          return "invalid"
5      if a == b == c:
6          return "equilateral"
7      if a == b or b == c or a == c:
8          return "isosceles"
9      return "scalene"
```

總共 Lines：1 3 4 5 6 7 8 9（共 8 行；第 2 行是 docstring，不是可執行敘述，coverage.py 也不列入統計）

## 測試案例

### test case 1（測試案例 1）

1. Input values（測試時候需要控制資料的值）：a = 1, b = 1, c = 3
2. expected result（正確的結果）：`invalid`
3. test program's result（程式執行後的結果）：`invalid`
4. criteria analysis（測試目標的分析）
   Line coverage：測試案例涵蓋的 Lines：1, 3, 4

### test case 2（測試案例 2）

1. Input values（測試時候需要控制資料的值）：a = 2, b = 2, c = 2
2. expected result（正確的結果）：`equilateral`
3. test program's result（程式執行後的結果）：`equilateral`
4. criteria analysis（測試目標的分析）
   Line coverage：測試案例涵蓋的 Lines：1, 3, 5, 6

### test case 3（測試案例 3）

1. Input values（測試時候需要控制資料的值）：a = 2, b = 2, c = 3
2. expected result（正確的結果）：`isosceles`
3. test program's result（程式執行後的結果）：`isosceles`
4. criteria analysis（測試目標的分析）
   Line coverage：測試案例涵蓋的 Lines：1, 3, 5, 7, 8

### test case 4（測試案例 4）

1. Input values（測試時候需要控制資料的值）：a = 3, b = 4, c = 5
2. expected result（正確的結果）：`scalene`
3. test program's result（程式執行後的結果）：`scalene`
4. criteria analysis（測試目標的分析）
   Line coverage：測試案例涵蓋的 Lines：1, 3, 5, 7, 9

## 結果

最少個案例為 **4** 個案例，總共涵蓋 Lines：1 3 4 5 6 7 8 9

**Line coverage：100%**（8 / 8）

| Line | T1 | T2 | T3 | T4 |
| --- | :-: | :-: | :-: | :-: |
| 1 | ✔ | ✔ | ✔ | ✔ |
| 3 | ✔ | ✔ | ✔ | ✔ |
| 4 | ✔ | | | |
| 5 | | ✔ | ✔ | ✔ |
| 6 | | ✔ | | |
| 7 | | | ✔ | ✔ |
| 8 | | | ✔ | |
| 9 | | | | ✔ |

### 為什麼 4 個是最少

第 4、6、8、9 行是 4 個 `return`，每次呼叫只會執行其中一個就離開函式，所以一個測試案例最多只能涵蓋其中一行，**至少需要 4 個測試案例**。上面 4 個案例剛好各涵蓋一個不同的 `return`，其餘的第 1、3、5、7 行也都會順帶執行到，所以 4 個案例就能達到 100%。

從上表也看得出每個案例都缺一不可：第 4 行只有 T1 涵蓋、第 6 行只有 T2、第 8 行只有 T3、第 9 行只有 T4。

## 工具驗證

### 4 個案例一起執行：Line coverage 100%

```text
> .venv\Scripts\python -m pytest hw2 -v
hw2/test_line_coverage.py::test_line_coverage[T1] PASSED                 [ 25%]
hw2/test_line_coverage.py::test_line_coverage[T2] PASSED                 [ 50%]
hw2/test_line_coverage.py::test_line_coverage[T3] PASSED                 [ 75%]
hw2/test_line_coverage.py::test_line_coverage[T4] PASSED                 [100%]

Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
hw1\triangle.py       8      0   100%
-----------------------------------------------
TOTAL                 8      0   100%
Required test coverage of 100.0% reached. Total coverage: 100.00%
4 passed
```

### 每個案例單獨執行：驗證各案例涵蓋的 Lines

用 `-k T1` 等只執行單一案例，`Missing` 欄位列出沒被執行的行；8 行扣掉 `Missing` 就是該案例涵蓋的 Lines，和上面的分析一致。

```text
> .venv\Scripts\python -m pytest hw2 -q -k T1
```

| 案例 | Stmts | Miss | Cover | Missing | 涵蓋的 Lines |
| --- | --: | --: | --: | --- | --- |
| T1 | 8 | 5 | 38% | 5-9 | 1, 3, 4 |
| T2 | 8 | 4 | 50% | 4, 7-9 | 1, 3, 5, 6 |
| T3 | 8 | 3 | 62% | 4, 6, 9 | 1, 3, 5, 7, 8 |
| T4 | 8 | 3 | 62% | 4, 6, 8 | 1, 3, 5, 7, 9 |
