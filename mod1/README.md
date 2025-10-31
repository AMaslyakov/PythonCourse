# ДЗ №1

```python
import numpy as np
from matplotlib import pyplot as plt
ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]
plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)
plt.title("Масляков")
plt.show()
```
1. Интерактивный режим (командный интерпретатор python)
   
   ![1. Интерактивный режим - запуск и результат](img/1.3_InteractivePython_PlotWithTerminal.png)

2. Скриптом из командной строки 
   
   ![2. Запуск скрипта из командной строки и результат](img/2.2_Запуск_скрипта.png)

3. IDLE
   
   ![3. Запуск скрипта в IDLE и результат](img/3.2_IDLE_запуск.png)

4. Google.Collab
   
   ![4. Запуск скрипта в Google Colab и результат](img/4_Google_Colab.png)

5. PyCharm
   
   ![5. Запуск скрипта в PyCharm и результат](img/5.2_PycharmRun.png)

6. Visual Studio code
   
   ![6. Запуск скрипта в Visual Studio Code и результат](./img/6.2_VSC_run.png)


