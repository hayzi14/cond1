shotrange = float(input('Введите дальность выстрела - '))

if shotrange > 28 and shotrange < 30:    
    print ('Попал в цель')

elif shotrange >= 30:    
    print ('Перелёт') 
    
elif shotrange > 0 and shotrange <= 28:    
    print ('Недолёт')

elif shotrange >= 0:    
    print ('Не бей по союзникам')