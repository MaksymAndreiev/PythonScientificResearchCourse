# Task 13.3 (Variant 15)

### Cauchy problem for a system of first order equations.

Find a numerical solution of the Cauchy problem for a linear inhomogeneous
systems of differential equations of the first order. Plot the graphs of the obtained solutions and the phase
trajectory. Add a legend to the solution graph. When constructing a graph, select the range of change of the argument t
in each case independently.\
*Remark*. In the given graphs, the curves are drawn both to the left and to the right from the initial moment 𝑡 = 𝑡<sub>
0</sub> = 0. The ```odeint``` function will create a solution only for moments of time 𝑡 ≥ 𝑡<sub>0< /sub>. That is, your
graphs should be constructed only in the right half-plane 𝑡 ≥ 0.

$$\begin{cases}
\dot{x} &= x - y + 2\sin(t), \\
\dot{y} &= 2x - y,
\end{cases}
\quad \(x(0) = -1\) and \(y(0) = 2\)$$

# Завдання 13.3 (Варіант 15)

### Задача Коші для системи рівнянь першого порядку.

Знайти чисельний розв’язок задачі Коші для лінійної неоднорідної
системи диференціальних рівнянь першого порядку. Побудувати графіки
отриманих розв’язків та фазову траєкторію. Додати на графік розв’язків легенду.
При побудові графіка діапазон зміни аргументу t в кожному випадку підбирати
самостійно.\
*Зауваження*. На наведених графіках криві намальовано як вліво так вправо від
початкового моменту 𝑡 = 𝑡<sub>0</sub> = 0. Функція ```odeint``` створюватиме розв’язок
лише для моментів часу 𝑡 ≥ 𝑡<sub>0</sub>. Тобто ваші графіки мають бути побудовані лише
у правій півплощині 𝑡 ≥ 0.

$$\begin{cases}
\dot{x} &= x - y + 2\sin(t), \\
\dot{y} &= 2x - y,
\end{cases}
\quad \(x(0) = -1\) and \(y(0) = 2\)$$