# Task 13.2

### Second order differential equation.

Find the numerical solution of the second differential equation
of order with initial conditions y(0) = 4, y'(0) = 1 (Cauchy problem). Plot the solution graph, phase trajectory, and
starting point. Construct a solution tangent to the graph at the starting point. Choose the change interval x on the
graph yourself.\
***Hint***. The equation of the tangent to the curve 𝑦 = 𝑦(𝑥) at the point (𝑥<sub>0</sub>, 𝑦<sub>0</sub>) has the form
𝑦 = 𝑦<sub>0</sub> + 𝑦′(𝑥<sub>0</sub>) ∙ (𝑥 − 𝑥<sub>0</sub>), where 𝑥<sub>0</sub> , 𝑦<sub>0</sub>, 𝑦′(𝑥<sub>0</sub>) in
this problem can be taken from the initial conditions.\
***Remark***. In the given graphs, curves are drawn both to the left and to the right of the starting point 𝑦(𝑥<sub>
0</sub>) = 𝑦<sub>0</sub>. The ```odeint``` function will only generate a solution
for the abscissa 𝑥 ≥ 𝑥<sub>0</sub> = 0. That is, the graph of the solution should be constructed only in the right
half-plane of 𝑥 ≥ 0.

$$
\begin{array}{|r|r|}
\hline
\text № & Task
\\
\hline
15 &
y'' - 4y' + 29y = 0
\\
\hline
16 &
y'' - 2y' + 26y = 0
\\
\hline
\end{array}
$$

| №  | Image                                                                                                                           |
|----|---------------------------------------------------------------------------------------------------------------------------------|
| 15 | ![image](https://github.com/MaksymAndreiev/PythonScientificResearchCourse/assets/29687267/2cc25788-29cc-45d6-a33e-edb368f0eb1c) |
| 16 | ![image](https://github.com/MaksymAndreiev/PythonScientificResearchCourse/assets/29687267/e2d3c094-736c-443a-95dc-f2b23633c791) |

# Завдання 13.2

### Диференціальне рівняння другого порядку.

Знайти чисельний розв’язок диференціального рівняння другого
порядку з початковими умовами y(0) = 4, y'(0) = 1 (задача Коші). Побудувати
графік розв’язку, фазову траєкторію та початкову точку. Побудувати дотичну до
графіка розв’язку в початковій точці. На графіку інтервал зміни x підібрати
самостійно.\
***Вказівка***. Рівняння дотичної до кривої 𝑦 = 𝑦(𝑥) в точці (𝑥<sub>0</sub>, 𝑦<sub>0</sub>) має вигляд
𝑦 = 𝑦<sub>0</sub> + 𝑦′(𝑥<sub>0</sub>) ∙ (𝑥 − 𝑥<sub>0</sub>), де 𝑥<sub>0</sub>, 𝑦<sub>0</sub>, 𝑦′(𝑥<sub>0</sub>) в цій
задачі можна взяти з початкових
умов.\
***Зауваження***. На наведених графіках криві намальовано як вліво так вправо від
початкової точки 𝑦(𝑥<sub>0</sub>) = 𝑦<sub>0</sub>. Функція ```odeint``` створюватиме розв’язок лише
для абсцис 𝑥 ≥ 𝑥<sub>0</sub> = 0. Тобто графік розв’язку має бути побудований лише у
правій півплощині 𝑥 ≥ 0.

$$
\begin{array}{|r|r|}
\hline
\text № & Завдання
\\
\hline
15 &
y'' - 4y' + 29y = 0
\\
\hline
16 &
y'' - 2y' + 26y = 0
\\
\hline
\end{array}
$$

| №  | Зображення                                                                                                                      |
|----|---------------------------------------------------------------------------------------------------------------------------------|
| 15 | ![image](https://github.com/MaksymAndreiev/PythonScientificResearchCourse/assets/29687267/2cc25788-29cc-45d6-a33e-edb368f0eb1c) |
| 16 | ![image](https://github.com/MaksymAndreiev/PythonScientificResearchCourse/assets/29687267/e2d3c094-736c-443a-95dc-f2b23633c791) |
