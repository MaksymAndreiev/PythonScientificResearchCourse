# Task 13.2 (Variant 15)

### Second order differential equation.

Find the numerical solution of the second differential equation
of order with initial conditions y(0) = 4, y'(0) = 1 (Cauchy problem). Plot the solution graph, phase trajectory, and
starting point. Construct a solution tangent to the graph at the starting point. Choose the change interval x on the
graph yourself.\
*Hint*. The equation of the tangent to the curve 𝑦 = 𝑦(𝑥) at the point (𝑥<sub>0</sub>, 𝑦<sub>0</sub>) has the form
𝑦 = 𝑦<sub>0</sub> + 𝑦′(𝑥<sub>0</sub>) ∙ (𝑥 − 𝑥<sub>0</sub>), where 𝑥<sub>0</sub> , 𝑦<sub>0</sub>, 𝑦′(𝑥<sub>0</sub>) in
this problem can be taken from the initial conditions.\
*Remark*. In the given graphs, curves are drawn both to the left and to the right of the starting point 𝑦(𝑥<sub>
0</sub>) = 𝑦<sub>0</sub>. The ```odeint``` function will only generate a solution
for the abscissa 𝑥 ≥ 𝑥<sub>0</sub> = 0. That is, the graph of the solution should be constructed only in the right
half-plane of 𝑥 ≥ 0.

$$y'' - 4y' + 29y = 0$$

# Завдання 13.2 (Варіант 15)

### Диференціальне рівняння другого порядку.

Знайти чисельний розв’язок диференціального рівняння другого
порядку з початковими умовами y(0) = 4, y'(0) = 1 (задача Коші). Побудувати
графік розв’язку, фазову траєкторію та початкову точку. Побудувати дотичну до
графіка розв’язку в початковій точці. На графіку інтервал зміни x підібрати
самостійно.\
*Вказівка*. Рівняння дотичної до кривої 𝑦 = 𝑦(𝑥) в точці (𝑥<sub>0</sub>, 𝑦<sub>0</sub>) має вигляд
𝑦 = 𝑦<sub>0</sub> + 𝑦′(𝑥<sub>0</sub>) ∙ (𝑥 − 𝑥<sub>0</sub>), де 𝑥<sub>0</sub>, 𝑦<sub>0</sub>, 𝑦′(𝑥<sub>0</sub>) в цій
задачі можна взяти з початкових
умов.\
*Зауваження*. На наведених графіках криві намальовано як вліво так вправо від
початкової точки 𝑦(𝑥<sub>0</sub>) = 𝑦<sub>0</sub>. Функція ```odeint``` створюватиме розв’язок лише
для абсцис 𝑥 ≥ 𝑥<sub>0</sub> = 0. Тобто графік розв’язку має бути побудований лише у
правій півплощині 𝑥 ≥ 0.

$$y'' - 4y' + 29y = 0$$