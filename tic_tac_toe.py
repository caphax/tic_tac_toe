#cpahax49ry2t7r892  trt
def search_for_a_visitor(plase):
    temp_plase = []
    temp_chet = 0
    for i in range(len(plase)):
        if i % 3 == 0:
            temp_plase.append([])
        temp_plase[-1].append(plase[i])

    if ['x','x','x'] in temp_plase:
        print('\nvin x\n')
        return True
    if ['0','0','0'] in temp_plase:
        print('\nvin 0\n')
        return True


    for i in range(3):
        if temp_plase[i][i] == 'x':
            temp_chet += 1
        if temp_plase[i][i] == '0':
            temp_chet -= 1
    if temp_chet == 3:
        print('\nvin x\n')
        return True
    if temp_chet == -3:
        print('\nvin 0\n')
        return True
    temp_chet = 0

    for i in range(3):
        if temp_plase[i][2-i] == 'x':
            temp_chet += 1
        if temp_plase[i][2-i] == '0':
            temp_chet -= 1
    if temp_chet == 3:
        print('\nvin x\n')
        return True
    if temp_chet == -3:
        print('\nvin 0\n')
        return True
    temp_chet = 0

    for i in range(3):
        if temp_plase[:i].count(temp_plase[0][i]) == len(temp_plase[:, i]):
            print(f"\nvin {temp_plase[0][i]}\n")
            return True




    return False

def finding_x_0(place, number_of_values, i = None, cross_turn = False,):
    if i != None:
        place[i] = '0'
        if cross_turn:
            place[i] = 'x'



        if len(number_of_values) == 0:
            if search_for_a_visitor(place):
                for i in range(len(place)):
                    print(place[i], end=' ')
                    if (i + 1) % 3 == 0:
                        print()
                print('\n________________\n')
            return None


    for i in number_of_values:
        temp = number_of_values.copy()
        temp.remove(i)
        finding_x_0(place.copy(), temp, i, not cross_turn)





    return place





place = [None, None, None, None, None, None, None, None, None]
posible_turns = [0, 1, 2, 3, 4, 5, 6, 7, 8]

finding_x_0(place, posible_turns)
