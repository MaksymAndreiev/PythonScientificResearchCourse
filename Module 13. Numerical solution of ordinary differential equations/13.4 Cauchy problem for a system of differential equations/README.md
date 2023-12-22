# Task 13.4

### Cauchy problem for a system of differential equations.

Find a numerical solution of the Cauchy problem for a system of second-order differential equations that is not reduced to the normal form. Plot the graphs of the obtained solutions and add a legend to the figure.
In terms $\(\dot{x}\)$ denotes $\(\frac{dx}{dt}\)$, $\(\ddot{x}\)$ denotes $\(\frac{d^2x }{dt^2}\)$, $\(\dot{y}\)$ denotes $\(\frac{dy}{dt}\)$, etc. When constructing graphs, the range of change of the argument t in each case to choose independently.\
Remark. The given curves are drawn both to the left and to the right of the initial one
points 𝑡 = 𝑡<sub>0</sub> = 0. The ```odeint``` function creates solutions only for time points
𝑡 ≥ 𝑡<sub>0</sub>. And your graphs should only be plotted in the right half-plane 𝑡 ≥ 0.

$$
\begin{array}{|r|r|}
\hline
\text № & Task
\\
\hline
 15 & 
\begin{cases}
\frac{d^2x}{dt^2} &= x - 4y, \quad x(0) = 2, \quad y(0) = 0, \\
\frac{d^2y}{dt^2} &= -x + y, \quad x\'(0) = -\sqrt{3}, \quad y\'(0) = \frac{\sqrt{3}}{2}.
\end{cases}
\\
\hline
16 & 
\begin{cases}
\frac{d^2x}{dt^2} + \frac{dy}{dt} &= e^t - x, \quad x(0) = 1, \quad y(0) = 0, \\
\frac{d^2y}{dt^2} + \frac{dx}{dt} &= 1, \quad x\'(0) = 2, \quad y\'(0) = -1.
\end{cases}
\\
\hline
\end{array}
$$

| №  | Image  |
|---|---|
|  15 |  ![image](https://github.com/MaksymAndreiev/PythonScientificResearchCourse/assets/29687267/456e5ca5-5e5b-414e-bd4e-1e8bd69f680b) |
|  16 | ![image](https://github.com/MaksymAndreiev/PythonScientificResearchCourse/assets/29687267/0ada08a3-a6fa-4916-ae3c-a1b0efa3282a) |

# Завдання 13.4

### Задача Коші для системи диференціальних рівнянь.

Знайти чисельний розв’язок задачі Коші для системи
диференціальних рівнянь другого порядку, яка не приведена до нормального
вигляду. Побудувати графіки отриманих розв’язків і додати на рисунок легенду.
В умовах $\(\dot{x}\)$ позначає $\(\frac{dx}{dt}\)$, $\(\ddot{x}\)$ позначає $\(\frac{d^2x}{dt^2}\)$, $\(\dot{y}\)$
позначає $\(\frac{dy}{dt}\)$ і т. д. При побудові графіків діапазон
зміни аргументу t в кожному випадку підбирати самостійно.\
Зауваження. Наведені криві намальовано як вліво так вправо від початкової
точки 𝑡 = 𝑡<sub>0</sub> = 0. Функція ```odeint``` створює розв’язки лише для моментів часу
𝑡 ≥ 𝑡<sub>0</sub>. І ваші графіки мають бути побудовані лише у правій півплощині 𝑡 ≥ 0.

$$
\begin{array}{|r|r|}
\hline
\text № & Завдання
\\
\hline
 15 & 
\begin{cases}
\frac{d^2x}{dt^2} &= x - 4y, \quad x(0) = 2, \quad y(0) = 0, \\
\frac{d^2y}{dt^2} &= -x + y, \quad x\'(0) = -\sqrt{3}, \quad y\'(0) = \frac{\sqrt{3}}{2}.
\end{cases}
\\
\hline
16 & 
\begin{cases}
\frac{d^2x}{dt^2} + \frac{dy}{dt} &= e^t - x, \quad x(0) = 1, \quad y(0) = 0, \\
\frac{d^2y}{dt^2} + \frac{dx}{dt} &= 1, \quad x\'(0) = 2, \quad y\'(0) = -1.
\end{cases}
\\
\hline
\end{array}
$$

| №  | Зображення  |
|---|---|
|  15 |  ![image](https://github.com/MaksymAndreiev/PythonScientificResearchCourse/assets/29687267/456e5ca5-5e5b-414e-bd4e-1e8bd69f680b) |
|  16 | ![image](https://github.com/MaksymAndreiev/PythonScientificResearchCourse/assets/29687267/0ada08a3-a6fa-4916-ae3c-a1b0efa3282a) |
