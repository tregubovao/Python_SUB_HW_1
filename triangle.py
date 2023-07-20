# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
# Дано a, b_side, c_side - стороны предполагаемого треугольника. 
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, 
# то треугольника с такими сторонами не существует. 
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

a_side = 3
b_side = 5
c_side = 4

if a_side + b_side > c_side and a_side + c_side > b_side and c_side + b_side > a_side:
    if a_side == b_side == c_side:
        print(f'Это раВносторонний треугольник')        
    elif a_side == b_side or b_side == c_side or a_side == c_side:
        print(f'Это РАВНОБЕДРЕННЫЙ треугольник')
    elif (a_side**2 + b_side**2 == c_side**2 
            or a_side**2 + c_side**2 == b_side**2 
            or c_side**2 + b_side**2 == a_side**2):
        print(f'Это ПРЯМОУГОЛЬНЫЙ треугольник')
    else:
        print(f'Это раЗносторонний треугольник')
else:
    print(f'Треугольника с такими сторонами НЕ существует')