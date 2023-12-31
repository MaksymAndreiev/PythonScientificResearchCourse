# Task 9.4

### Partial derivatives. Normal to the surface.

Calculate the partial derivative functions 𝑧(𝑥, 𝑦) at the point (𝑥<sub>0</sub>, 𝑦<sub>0</sub>).
Plot the graph of the function, plot the point (𝑥<sub>0</sub>, 𝑦<sub>0</sub>, 𝑧<sub>0</sub> = 𝑧(𝑥<sub>0</sub>, 𝑦 <sub>
0</sub>)) and the vector normal to the surface at this point. Draw the lines of intersection of the surface with
vertical planes 𝑥 = 𝑥<sub>0</sub> and 𝑦 = 𝑦<sub>0</sub>. Construct tangent vectors to
of these lines at the point (𝑥<sub>0</sub>, 𝑦<sub>0</sub>, 𝑧<sub>0</sub>). As a result, you should get an image
something like the following.

![image](https://github.com/MaksymAndreiev/PythonScientificResearchCourse/assets/29687267/6dfbd93a-a5d2-4a4b-953c-83de401d91fe)

***Remark***. To make the normal to the surface look like a normal, you need to set
the same lengths of the ranges of coordinate changes 𝑥, 𝑦, 𝑧, for example, on all axes,
with the instructions\
```ax.set_xlim(-2, 2)```\
```ax.set_ylim(-2, 2)```\
```ax.set_zlim(-1, 3)```\
If this is not done, the normal vector in the figure may not look like
normal.

$$
\begin{array}{|r|r|}
\hline
\text № & Function & Points\\
\hline
15 &
z = x^2 + xy + y^2 - x + 3y & x_{0} = -0.5; \quad y_{0} = 0.7;
\\
\hline
16 &
z = x^2 - 2xy + y^4 - y^5 & x_{0} = -0.5; \quad y_{0} = 0.7;
\\
\hline
\end{array}
$$

# Завдання 9.4

### Частинні похідні. Нормаль до поверхні.

Обчислити частинні похідні функції 𝑧(𝑥, 𝑦) в точці (𝑥<sub>0</sub>, 𝑦<sub>0</sub>).
Побудувати графік функції, зобразити точку (𝑥<sub>0</sub>, 𝑦<sub>0</sub>, 𝑧<sub>0</sub> = 𝑧(𝑥<sub>0</sub>, 𝑦<sub>
0</sub>)) і вектор
нормалі до поверхні в цій точці. Зобразити лінії перетинання поверхні з
вертикальними площинами 𝑥 = 𝑥<sub>0</sub> і 𝑦 = 𝑦<sub>0</sub>. Побудувати дотичні вектори до
цих ліній в точці (𝑥<sub>0</sub>, 𝑦<sub>0</sub>, 𝑧<sub>0</sub>). В результаті ви повинні отримати зображення щось
на зразок наступного.

![image](https://github.com/MaksymAndreiev/PythonScientificResearchCourse/assets/29687267/6dfbd93a-a5d2-4a4b-953c-83de401d91fe)

***Зауваження***. Щоб нормаль до поверхні виглядала як нормаль, потрібно задати
однакові по всім осям довжини діапазонів зміни координат 𝑥, 𝑦, 𝑧, наприклад,
інструкціями\
```ax.set_xlim(-2, 2)```\
```ax.set_ylim(-2, 2)```\
```ax.set_zlim(-1, 3)```\
Якщо це не зробити, то вектор нормалі на рисунку може не виглядати як
нормаль.

$$
\begin{array}{|r|r|}
\hline
\text № & Функції & Точки\\
\hline
15 &
z = x^2 + xy + y^2 - x + 3y & x_{0} = -0.5; \quad y_{0} = 0.7;
\\
\hline
16 &
z = x^2 - 2xy + y^4 - y^5 & x_{0} = -0.5; \quad y_{0} = 0.7;
\\
\hline
\end{array}
$$
