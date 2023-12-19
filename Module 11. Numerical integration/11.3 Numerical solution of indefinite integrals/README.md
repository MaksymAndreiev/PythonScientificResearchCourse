# Task 11.3 (Variant 15)

### Numerical solution of indefinite integrals.

Using the ```scipy.integrate.cumtrapz``` function,
calculate the indefinite integral and plot its graph. Build as well
the graph of the integrand function. At the point ```x0```, construct a tangent to the graph
original

Recall that the equation of the tangent to the graph of the function $\(y = y(x)\)$ at the point $\(x_0\)$ has the form $\(y = y(x_0) + k \cdot (x -
x_0)\)$, where $\(k = y'(x_0)\)$ is the value of the derivative at the point of contact. The coefficient $\(k\)$ can be calculated in two ways:
using the definition of the primitive (the derivative of the primitive is equal to the integrand), and approximated by the formula
$\(y'(x_0) \approx \frac{y(x_0 + \Delta x) - y(x_0)}{\Delta x}\)$. Construct tangent graphs for both values of $\(k\)$.
The value of $\(x_0\)$, intervals of the independent variable on the graphs, as well as an arbitrary constant for the initial one can be chosen independently.
As a result of solving the problem, you should get a drawing similar to
for example, on the next one.

**Hint.** To select a point on the graph of the original, it is desirable to use the abscissa $\(x\)$ among the values of the array, which were calculated
the value of the ordinate $\(y_{\text{int}}\)$, determine the index $\(i_0\)$ of the element that is equal to $\(x_0\)$ (the value of $\(x_0\)$
must be
among the elements of $\(x\))$. This can be done, for example, by the instruction $\(i_0 = \text{np.where}(x==x_0)[0][0]\)$. Then
ordinate
point of contact will be $\(y_{\text{int}}[i_0]\)$, and the approximate formula $\(y' (x_0) \approx \frac{y_{\text{int}}[i_0+1] - y_
{\text{int}}[i_0]}{x[i_0+1] - x[i_0]}\)$ can be implemented by the instruction ```k1=(yint[i0+1]-yint[i0])/( x[i0+1]-x[i0])```.
Obviously, the array of tangent ordinates ```yd1'' will be calculated by the instruction ``yd1=yint[i0]+k1*(xd1-x[i0])'',
where ``xd1'' is the abscissa array along which the tangent will be drawn. Exactly the coefficient (tangent of the angle) of the slope of the tangent to the graph
of the original is calculated as the value of the integrand
of the expression at the point ```x0'''. Use it to construct another straight line that will more accurately model the tangent line. At
increasing the number of points by which the array of ordinates ```yint''' of the original is calculated, the discrepancy between the tangent graphs
should decrease (check it).

$$\int (4 - 16x) \sin(4x) \, dx$$

# Завдання 11.3 (Варіант 15)

### Чисельне знаходження невизначених інтегралів.

Використовуючи функцію ```scipy.integrate.cumtrapz```,
обчислити невизначений інтеграл і побудувати його графік. Побудувати також
графік підінтегральної функції. В точці ```x0``` побудувати дотичну до графіка
первісної.

Нагадаємо, що рівняння дотичної до графіка функції $\(y = y(x)\)$ в точці $\(x_0\)$ має вид $\(y = y(x_0) + k \cdot (x -
x_0)\)$, де $\(k = y'(x_0)\)$ – значення похідної в точці дотику. Коефіцієнт $\(k\)$ обчислити двома способами:
використовуючи визначення первісної (похідна до первісної дорівнює підінтегральному виразу), та наближено за формулою
$\(y'(x_0) \approx \frac{y(x_0 + \Delta x) - y(x_0)}{\Delta x}\)$. Для обох значень $\(k\)$ побудувати графіки дотичних.
Значення $\(x_0\)$, інтервали незалежної змінної на графіках, а також довільну сталу для первісної обрати самостійно.
В результаті розв'язання задачі ви повинні отримати рисунок схожий,
наприклад, на наступний.

**Вказівка.** Для вибору точки на графіку первісної бажано серед значень масиву абсцис $\(x\)$, по яким обчислювалися
значення ординат $\(y_{\text{int}}\)$, визначити індекс $\(i_0\)$ елемента, який дорівнює $\(x_0\)$ (значення $\(x_0\)$
має бути
серед елементів $\(x\))$. Це можна зробити, наприклад, інструкцією $\(i_0 = \text{np.where}(x==x_0)[0][0]\)$. Тоді
ординатою
точки дотику буде $\(y_{\text{int}}[i_0]\)$, а наближену формулу $\(y' (x_0) \approx \frac{y_{\text{int}}[i_0+1] - y_
{\text{int}}[i_0]}{x[i_0+1] - x[i_0]}\)$ можна реалізувати інструкцією ```k1=(yint[i0+1]-yint[i0])/(x[i0+1]-x[i0])```.
Вочевидь, масив ординат ```yd1``` дотичної обчислюватиметься інструкцією ```yd1=yint[i0]+k1*(xd1-x[i0])```,
де ```xd1``` – масив абсцис, по яким малюватиметься дотична. Точно коефіцієнт (тангенс кута) нахилу дотичної до графіка
первісної обчислюється як значення підінтегрального
виразу в точці ```x0```. Використайте його для побудови іншої прямої, яка точніше буде моделювати дотичну. При
збільшенні кількості точок, по яким обчислюється масив ординат ```yint``` первісної, розбіжність між графіками дотичних
повинна зменшуватися (перевірте це).

$$\int (4 - 16x) \sin(4x) \, dx$$