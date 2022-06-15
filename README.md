# Application_for_mgtu
Приложение создано для прогнозирования свойств композитного материала.
В качестве модели прогнозирования Модуля упругости при растяжении и Прочности при растяжении композитного материала используется линейная регрессия. 
Прогнозирование соотношения матрица-наполнитель выполнена на основе модели нейронной сети.
В программе производится импортирование пред обученных моделей линейной регрессии и нейронной сети.
После запуска приложения появляется главный интерфейс, в котором предлагается выбрать параметры для прогнозирования.
Ввод команд осуществляется вводом соответствующей цифры в консоль:
1 – Модуль упругости при растяжении и Прочность при растяжении;
2 – Соотношение матрица-наполнитель;
0 – выход из приложения.
При вводе не существующей команды появляется сообщение «!!!Неиз-вестная команда, выберите из доступных» и предлагается повторно сделать ввод. 
Так будет продолжаться до тех пор, пока не будет введена известная команда.
При вводе в консоль «0» осуществляется выход из программы и выводится сообщение «Завершение работы программы...».
При вводе «0» или «1» предлагается поочерёдно ввести параметры композитного материала.
На этапе ввода параметров реализована проверка на ввод допустимых значений. Если введено не числовое значение (буквы, специальные символы и тому подобное) 
будет выведено сообщение «Введено НЕ число. Введите корректное значение». При вводе отрицательного числа выводится сообще-ние «Число меньше 0. 
Введите корректное значение». В обоих случаях так будет продолжаться до тех пор, пока не будет введено корректное число.
По итогу работы программа осуществит вывод прогнозируемых свойств материала и предложит произвести новую операцию.
