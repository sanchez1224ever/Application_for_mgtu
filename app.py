    
def isfloat(value):                           #проверка на то, чтоб введеное значение было числом
    try:
        float(value)
        return True
    except ValueError:
        return False

def allowed_value(name_param):                #проверка на корректность введёного числа. Будет выдано предупреждение о том что не так с введёнными значением
    good_value = 0
    
    while good_value == 0:
        value = input(f'Введите {name_param}: ')
        if isfloat(value):
            value = float(value)
            if value >= 0:
                return value
                good_value == 1
            else:
                print('!!!Число меньше 0. Введите корректное значение')
        else:
            print('!!!Введено НЕ число. Введите корректное значение')
            
def read_params_lin_reg():                                                  #Чтение параметров для линейной регрессии
    matrix = allowed_value('соотношение матрица-наполнитель') / 5.314144
    density =  allowed_value('плотность') / 2161.565216
    elast_module = allowed_value('модуль упругости') / 1649.415706
    amount_of_hardener = allowed_value('количество отвердителя') / 181.828448
    epox_group = allowed_value('содержание эпоксидных групп') / 28.955094
    temper_flash = allowed_value('температуру вспышки') / 386.067992
    surface_density = allowed_value('поверхностную плотность') / 1291.340115
    resin_comp = allowed_value('потребление смолы') / 359.052220
    angle_of_patch = allowed_value('угол нашивки') / 90
    step_of_patch = allowed_value('шаг нашивки') / 13.732404
    density_of_patch = allowed_value('плотность нашивки') / 86.012427
    return(matrix, density, elast_module, amount_of_hardener, epox_group, temper_flash, surface_density, resin_comp, angle_of_patch, step_of_patch, density_of_patch)

def read_params_nn():                                                  #Чтение параметров для нейронной сети
    density =  allowed_value('плотность') / 2161.565216
    elast_module = allowed_value('модуль упругости') / 1649.415706
    amount_of_hardener = allowed_value('количество отвердителя') / 181.828448
    epox_group = allowed_value('содержание эпоксидных групп') / 28.955094
    temper_flash = allowed_value('температуру вспышки') / 386.067992
    surface_density = allowed_value('поверхностную плотность') / 1291.340115
    module_elast_strech = allowed_value('модуль упругости при растяжении') / 81.417126
    endur_strech = allowed_value('прочность при растяжении') / 3705.672523
    resin_comp = allowed_value('потребление смолы') / 359.052220
    angle_of_patch = allowed_value('угол нашивки') / 90
    step_of_patch = allowed_value('шаг нашивки') / 13.732404
    density_of_patch = allowed_value('плотность нашивки') / 86.012427
    return(density, elast_module, amount_of_hardener, epox_group, temper_flash, surface_density, module_elast_strech, endur_strech, resin_comp, angle_of_patch, step_of_patch, density_of_patch)
            
quit = 0

while quit == 0:                                # Основной цикл программы. Будет работать пока не будет осуществлён выход из неё.
    
    type_param = int(input('Введите номер параметра прогнозирования:\n1 - "Модуль упругости при растяжении" и "Прочность при растяжении" \n2 - "Соотношение матрица-наполнитель"\n0 - выход из программы\n'))
    
    if type_param == 1:
        import pickle
        
        with open('line_reg_module.pkl', 'rb') as file:         #Загрузка модели линейной регресии для предсказания параметра "Модуль упругости при растяжении"
            line_reg_module_model = pickle.load(file)
    
        with open('line_reg_endur.pkl', 'rb') as file:         #Загрузка модели линейной регресии для предсказания параметра "Прочность при растяжении"
            line_reg_endur_model = pickle.load(file)
        
        params = read_params_lin_reg()
        x_pred = [[i for i in params]]
        y_pred_module = line_reg_module_model.predict(x_pred)
        y_pred_endur = line_reg_endur_model.predict(x_pred)
        print('Модуль упругости при растяжении(прогноз): ' + str(round(y_pred_module[0] * 81.417126, 2)))
        print('Прочность при растяжении(прогноз): ' + str(round(y_pred_endur[0] * 3705.672523, 2)) + '\n')
        
    elif type_param == 2:
        from tensorflow import keras
        model_nn_loaded = keras.models.load_model('model_nn')      #Загрузка сохранённой модели нейронной сети
        
        params = read_params_nn()
        x_pred = [[i for i in params]]
        y_pred = model_nn_loaded.predict(x_pred).flatten()[0] 
        print('Соотношение матрица-наполнитель (прогноз): ' + str(round(y_pred * 5.314144, 2)) + '\n')
        
    elif type_param == 0:
        print('Завершение работы программы...')
        quit = 1
        
    else:
        print('!!!Неизвестная команда, выберите из доступных')