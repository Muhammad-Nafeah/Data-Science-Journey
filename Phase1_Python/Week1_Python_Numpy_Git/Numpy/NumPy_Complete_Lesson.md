# NumPy — Complete Lesson (0 to Advanced)

---

## What is NumPy?

Python lists are slow when working with large data. NumPy gives you **arrays** that are:
- Much faster than Python lists
- Take less memory
- Built for math operations

Everything in data science — Pandas, Matplotlib, Machine Learning — uses NumPy under the hood.

---

## Installation

```bash
pip install numpy
```

---

## Import NumPy

```python
import numpy as np
```

`np` is just a shortcut — everyone uses it.

---

## Topic 1 — Creating Arrays

### 1D Array
```python
marks = np.array([88, 76, 45, 90, 60])
print(marks)
print(type(marks))
```

Output:
```
[88 76 45 90 60]
<class 'numpy.ndarray'>
```

Notice — no commas in the output. That's how you know it's a NumPy array.

---

### List vs Array — The Key Difference

```python
# Python list
marks_list = [88, 76, 45, 90, 60]
print(marks_list + 10)  # ERROR

# NumPy array
marks_array = np.array([88, 76, 45, 90, 60])
print(marks_array + 10)  # Works! Adds 10 to every element
```

---

### 2D Array (rows and columns — like a table)

```python
classroom = np.array([
    [88, 76, 45],
    [90, 60, 70],
    [55, 80, 95]
])
```

---

### 3D Array (multiple tables)

```python
school = np.array([
    [[88, 76], [90, 60]],   # Class A
    [[55, 80], [95, 70]]    # Class B
])
```

---

### Real World Uses

| Array | Real World |
|-------|-----------|
| 1D | A single student's marks |
| 2D | Whole class marks (table) |
| 3D | Multiple classes or RGB image |
| 4D+ | Video frames, deep learning data |

---

### Other Ways to Create Arrays

```python
np.zeros((3, 3))        # 3x3 array of zeros
np.ones((2, 4))         # 2x4 array of ones
np.arange(0, 10, 2)     # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)    # 5 evenly spaced numbers between 0 and 1
np.random.randint(0, 100, (3, 3))  # 3x3 random integers between 0 and 100
```

---

## Topic 2 — Indexing & Slicing

### 1D Indexing

```python
marks = np.array([88, 76, 45, 90, 60])

print(marks[0])     # First element → 88
print(marks[-1])    # Last element → 60
print(marks[1:4])   # Index 1 to 3 → [76 45 90]
print(marks[:3])    # First 3 → [88 76 45]
print(marks[2:])    # From index 2 onwards → [45 90 60]
```

---

### 2D Indexing

```python
classroom = np.array([
    [88, 76, 45],
    [90, 60, 70],
    [55, 80, 95]
])

print(classroom[0])       # First row → [88 76 45]
print(classroom[1, 2])    # Row 1, Column 2 → 70
print(classroom[:, 1])    # All rows, Column 1 → [76 60 80]
print(classroom[0:2, 1:]) # Rows 0-1, Columns 1+ → [[76 45] [60 70]]
```

---

## Topic 3 — Array Operations & Math

### Basic Operations

```python
marks = np.array([88, 76, 45, 90, 60])

print(marks + 10)   # Add 10 to every element
print(marks - 5)    # Subtract 5
print(marks * 2)    # Multiply by 2
print(marks / 10)   # Divide by 10
print(marks ** 2)   # Square every element
```

---

### Operations Between Two Arrays

```python
math    = np.array([88, 76, 45])
english = np.array([70, 80, 90])

print(math + english)   # Adds element by element
print(math - english)   # Subtracts element by element
print(math * english)   # Multiplies element by element
```

---

### Comparison Operations (Boolean Masking)

```python
marks = np.array([88, 76, 45, 90, 60])

print(marks > 50)           # [True True False True True]
print(marks == 90)          # [False False False True False]

# Filter — get only passing marks
print(marks[marks >= 50])   # [88 76 90 60]
```

This is called **Boolean Masking** — one of the most used patterns in data science.

---

## Topic 4 — Aggregations

### Basic Aggregations

```python
marks = np.array([88, 76, 45, 90, 60])

print(np.sum(marks))    # Total → 359
print(np.mean(marks))   # Average → 71.8
print(np.min(marks))    # Lowest → 45
print(np.max(marks))    # Highest → 90
print(np.std(marks))    # Standard deviation
print(np.median(marks)) # Median
```

---

### Aggregations on 2D Arrays

```python
classroom = np.array([
    [88, 76, 45],
    [90, 60, 70],
    [55, 80, 95]
])

print(np.mean(classroom))           # Average of everything
print(np.mean(classroom, axis=0))   # Average per column (per subject)
print(np.mean(classroom, axis=1))   # Average per row (per student)
```

**Rule:**
- `axis=0` → go down the rows (column wise)
- `axis=1` → go across the columns (row wise)

---

## Topic 5 — Reshaping

### Check Shape

```python
marks = np.array([1, 2, 3, 4, 5, 6])
print(marks.shape)  # (6,) → 6 elements, 1D
```

---

### Reshape 1D to 2D

```python
marks = np.array([1, 2, 3, 4, 5, 6])

reshaped = marks.reshape(2, 3)  # 2 rows, 3 columns
print(reshaped)
print(reshaped.shape)  # (2, 3)
```

Output:
```
[[1 2 3]
 [4 5 6]]
```

---

### Important Rule

Total elements must stay the same:

```python
marks.reshape(2, 3)  # 2x3 = 6 ✅
marks.reshape(3, 2)  # 3x2 = 6 ✅
marks.reshape(2, 4)  # 2x4 = 8 ❌ ERROR
```

---

### Flatten — 2D to 1D

```python
classroom = np.array([
    [88, 76, 45],
    [90, 60, 70]
])

flat = classroom.flatten()
print(flat)  # [88 76 45 90 60 70]
```

---

### Real World Use

In machine learning, image data comes as 3D but models expect 2D — you reshape it before feeding into the model.

---

## Topic 6 — Broadcasting

### What is Broadcasting?

When you do math between arrays of different shapes, NumPy automatically expands the smaller one to match the bigger one.

---

### Simple Example

```python
marks = np.array([88, 76, 45, 90, 60])
print(marks + 10)  # 10 is broadcast across all 5 elements
```

You already used this without knowing it was called broadcasting.

---

### 2D Broadcasting

```python
classroom = np.array([
    [88, 76, 45],
    [90, 60, 70],
    [55, 80, 95]
])

bonus = np.array([5, 10, 15])  # One row

print(classroom + bonus)
```

Output:
```
[[ 93  86  60]
 [ 95  70  85]
 [ 60  90 110]]
```

NumPy added 5 to every first column, 10 to every second column, 15 to every third column — automatically.

---

### Real World Use

In data science you constantly add, subtract, or normalize values across rows or columns — broadcasting makes this fast without writing loops.

---

## Topic 7 — Useful Functions

```python
marks = np.array([88, 76, 45, 90, 60])

np.sort(marks)              # Sort ascending → [45 60 76 88 90]
np.argsort(marks)           # Indices that would sort the array
np.unique(marks)            # Unique values
np.where(marks > 70, 'Pass', 'Fail')  # Conditional — like if/else for arrays
np.clip(marks, 50, 100)     # Clip values between 50 and 100
np.argmax(marks)            # Index of highest value
np.argmin(marks)            # Index of lowest value
```

---

### np.where — Very Important

```python
marks = np.array([88, 76, 45, 90, 60])
result = np.where(marks >= 50, 'Pass', 'Fail')
print(result)  # ['Pass' 'Pass' 'Fail' 'Pass' 'Pass']
```

You'll use `np.where` constantly in data science.

---

## Topic 8 — Copying Arrays

```python
marks = np.array([88, 76, 45, 90, 60])

# Wrong way — both point to same data
copy1 = marks
copy1[0] = 999
print(marks)  # marks is also changed!

# Right way — independent copy
copy2 = marks.copy()
copy2[0] = 999
print(marks)  # marks is NOT changed
```

Always use `.copy()` when you don't want to affect the original array.

---

## Quick Reference Cheatsheet

| Task | Code |
|------|------|
| Create array | `np.array([1, 2, 3])` |
| Create zeros | `np.zeros((3, 3))` |
| Create ones | `np.ones((2, 4))` |
| Array shape | `arr.shape` |
| Reshape | `arr.reshape(2, 3)` |
| Flatten | `arr.flatten()` |
| Sum | `np.sum(arr)` |
| Mean | `np.mean(arr)` |
| Max | `np.max(arr)` |
| Min | `np.min(arr)` |
| Sort | `np.sort(arr)` |
| Filter | `arr[arr > 50]` |
| Conditional | `np.where(arr > 50, 'Pass', 'Fail')` |
| Column slice | `arr[:, 1]` |
| Row slice | `arr[1, :]` |
| Copy | `arr.copy()` |

---

*Made while learning Data Science — Phase 1, Week 1*
