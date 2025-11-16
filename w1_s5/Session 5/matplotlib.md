
---

# Matplotlib Cheatsheet

## 1. Setup
```
python
import numpy as np
import matplotlib.pyplot as plt

plt.show()  # display plots
```

## 2. Line Plots (`plt.plot`)

**Basic:**
```
python
plt.plot(x, y)
```
**Format string: `marker line_style color`**
```
python
plt.plot(x, y, 'o-r')   # circle markers, solid red line
plt.plot(x, y, 's--g')  # square markers, dashed green line
plt.plot(x, y, 'd:m')   # diamond markers, dotted magenta line
plt.plot(x, y, 'o-.y')  # circle markers, dash-dot yellow line
```
**Common markers:**

- `'o'` → circle  
- `'s'` → square  
- `'d'` → diamond  
- `'^'` → triangle up  
- `'p'` → pentagon  
- `'h'` → hexagon  

**Line styles:**

- `'-'` or `'solid'`  
- `'--'` or `'dashed'`  
- `':'` or `'dotted'`  
- `'-. '` dash-dot  

**Colors:**

- Short codes: `'r','g','b','k','m','y','c'`
- Named: `color='red'`
- Hex: `c='#00fcdd'`

**Extra styling:**
```
python
plt.plot(
    x, y,
    c='grey',      # line color
    marker='h',    # marker shape
    ms=13,         # marker size
    mec='r',       # marker edge color
    mfc='g',       # marker face color
    linewidth=7,   # or lw
    alpha=0.3      # transparency
)
```
---

## 3. Titles, Labels, Grid
```
python
plt.title("My Plot", loc='left')  # 'left' | 'center' | 'right'
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.grid(color='r', linestyle=':', linewidth=0.7)
```
---

## 4. Subplots (`plt.subplot`, `plt.suptitle`)
```
python
plt.subplot(2, 2, 1)   # (rows, cols, index)
plt.plot(x1, y1)
plt.title("First")

plt.subplot(2, 2, 2)
plt.plot(x2, y2)
plt.title("Second")

plt.suptitle("Overall Figure Title")
plt.show()
```
Common layouts:

- `plt.subplot(2, 1, 1)` → 2 rows, 1 column, top
- `plt.subplot(2, 1, 2)` → bottom
- `plt.subplot(1, 2, 1)` → left
- `plt.subplot(1, 2, 2)` → right

---

## 5. Scatter Plots (`plt.scatter`)

**Basic:**
```
python
plt.scatter(x, y)
```
**Two series:**
```
python
plt.scatter(x1, y1)
plt.scatter(x2, y2)
```
**Color options:**
```
python
plt.scatter(x, y, color='red')          # single color
plt.scatter(x, y, color=['r','g','b'])  # one color per point
```
**Colormap by values:**
```
python
plt.scatter(x, y, c=values, cmap='winter')
plt.colorbar()
```
**Sizes & transparency:**
```
python
plt.scatter(x, y, c='r', s=sizes, alpha=0.4)
```
**Labels + grid:**
```
python
plt.title("Scatter")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.grid(color='g', linestyle='--', linewidth=0.3)
```
---

## 6. Bar Charts (`plt.bar`, `plt.barh`)

**Vertical:**
```
python
plt.bar(categories, values)
```
**Horizontal:**
```
python
plt.barh(categories, values)
```
**Styling:**
```
python
plt.bar(categories, values, color='gold', width=0.3)
plt.barh(categories, values, color='gold', height=0.3)
```
---

## 7. Histogram (`plt.hist`)
```
python
data = np.random.normal(loc=100, scale=25, size=100)  # mean, std, count
plt.hist(data)
plt.show()
```
---

## 8. Pie Charts (`plt.pie`)

**Basic:**
```
python
plt.pie(values, labels=labels)
```
**Full options example:**
```
python
plt.pie(
    values,
    labels=labels,
    startangle=90,                # rotate start
    explode=[0.1, 0, 0, 0],       # pull slices out
    shadow=True,
    colors=['r', 'g', 'b', 'y'],
    autopct='%1.1f%%',            # percentages on wedges
    radius=1.2,
    wedgeprops={'edgecolor': 'black'},
    textprops={'fontsize': 12}
)
plt.show()
```
---

## 9. Quick Templates

**Line plot:**
```
python
plt.title("Line Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(x, y, 'o--r')
plt.grid(True)
plt.show()
```
**Scatter with colormap:**
```
python
plt.scatter(x, y, c=values, cmap='jet', s=sizes, alpha=0.4)
plt.colorbar()
plt.show()
```
**2×2 subplots:**
```
python
plt.subplot(2, 2, 1); plt.plot(x1, y1); plt.title("1")
plt.subplot(2, 2, 2); plt.plot(x2, y2); plt.title("2")
plt.subplot(2, 2, 3); plt.plot(x3, y3); plt.title("3")
plt.subplot(2, 2, 4); plt.plot(x4, y4); plt.title("4")
plt.suptitle("4 Plots")
plt.show()
```
