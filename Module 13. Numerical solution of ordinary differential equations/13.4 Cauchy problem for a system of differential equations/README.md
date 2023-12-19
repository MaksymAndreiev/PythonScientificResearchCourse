# Task 13.4 (Variant 15)

### Cauchy problem for a system of differential equations.

Find a numerical solution of the Cauchy problem for a system of second-order differential equations that is not reduced to the normal form. Plot the graphs of the obtained solutions and add a legend to the figure.
In terms $\(\dot{x}\)$ denotes $\(\frac{dx}{dt}\)$, $\(\ddot{x}\)$ denotes $\(\frac{d^2x }{dt^2}\)$, $\(\dot{y}\)$ denotes $\(\frac{dy}{dt}\)$, etc. When constructing graphs, the range of change of the argument t in each case to choose independently.\
Remark. The given curves are drawn both to the left and to the right of the initial one
points 𝑡 = 𝑡<sub>0</sub> = 0. The ```odeint``` function creates solutions only for time points
𝑡 ≥ 𝑡<sub>0</sub>. And your graphs should only be plotted in the right half-plane 𝑡 ≥ 0.

$$\begin{cases}
\frac{d^2x}{dt^2} &= x - 4y, \quad x(0) = 2, \quad y(0) = 0, \\
\frac{d^2y}{dt^2} &= -x + y, \quad x\'(0) = -\sqrt{3}, \quad y\'(0) = \frac{\sqrt{3}}{2}.
\end{cases}$$

# Завдання 13.4 (Варіант 15)

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

$$\begin{cases}
\frac{d^2x}{dt^2} &= x - 4y, \quad x(0) = 2, \quad y(0) = 0, \\
\frac{d^2y}{dt^2} &= -x + y, \quad x\'(0) = -\sqrt{3}, \quad y\'(0) = \frac{\sqrt{3}}{2}.
\end{cases}$$
