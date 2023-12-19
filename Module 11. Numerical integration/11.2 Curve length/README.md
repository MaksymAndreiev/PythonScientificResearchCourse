# Task 11.2 (Variant 15)

### Curve length.

Determine the length of the arc of the given curve segment
parametric equations. Construct a curve and a curved line segment, the length of which is calculated.\
Indication. The length of the arc of a plane curve, which is given in the parametric form x = x(t), y = y(t), is
calculated by the formula 
$$L = \int_{t_0}^{t_1} \sqrt{(x'(t))^2 + (y'(t))^2} \, dt$$
where t<sub>0</sub> and t<sub>1</sub> are the values of the parameter at the starting and ending points of the arc.\
Set the functions x(t), y(t) symbolically and calculate the integral expression $\sqrt{(x'(t))^2 + (y'(t))^2} $. Convert
it to a ```numpy``` function to use for numerical integration.

$$\begin{cases}
    x(t) = 6\(\cos(t)\+t\sin(t)\), \\
    y(t) = 6\(\sin(t)\-t\cos(t)\),
\end{cases}
\quad \quad 0 \leq t \leq 4\pi.$$



# Завдання 11.2 (Варіант 15)

### Довжина кривої.

Визначити довжину дуги відрізка кривої, яка задана
параметричними рівняннями. Побудувати криву та криволінійний відрізок,
довжина якого обчислюється.\
Вказівка. Довжина дуги плоскої кривої, яка задана у параметричному вигляді
x = x(t), y = y(t), обчислюється за формулою
$$L = \int_{t_0}^{t_1} \sqrt{(x'(t))^2 + (y'(t))^2} \, dt$$
де t<sub>0</sub> та t<sub>1</sub> – значення параметра в початковій та кінцевій точках дуги.\
Функції x(t), y(t) задайте символьно і обчисліть підінтегральний вираз
$\sqrt{(x'(t))^2 + (y'(t))^2} $. Перетворіть його на ```numpy``` функцію, яку використайте при
чисельному інтегруванні.

$$\begin{cases}
    x(t) = 6\(\cos(t)\+t\sin(t)\), \\
    y(t) = 6\(\sin(t)\-t\cos(t)\),
\end{cases}
\quad \quad 0 \leq t \leq 4\pi.$$
