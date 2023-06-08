import matplotlib.pyplot as plt

def search_for_a_visitor(plase): #count
    temp_plase = []
    temp_chet = 0
    #horizontal
    for i in range(len(plase)):
        if i % 3 == 0:
            temp_plase.append([])
        temp_plase[-1].append(plase[i])

    if ['x','x','x'] in temp_plase:
        return True
    if ['0','0','0'] in temp_plase:
        return False


    for i in range(3):
        if temp_plase[i][i] == 'x':
            temp_chet += 1
        if temp_plase[i][i] == '0':
            temp_chet -= 1
    if temp_chet == 3:
        return True
    if temp_chet == -3:
        return False
    temp_chet = 0

    for i in range(3):
        if temp_plase[i][2-i] == 'x':
            temp_chet += 1
        if temp_plase[i][2-i] == '0':
            temp_chet -= 1
    if temp_chet == 3:
        return True
    if temp_chet == -3:
        return False
    temp_chet = 0

    for i in range(3):
        if temp_plase[0][i] == '0' and temp_plase[1][i] == '0' and temp_plase[2][i] == '0':
            return True
        if temp_plase[0][i] == '0' and temp_plase[1][i] == '0' and temp_plase[2][i] == '0':
            return False


    return None

def finding_x_0(place, number_of_values, vals,i = None, cross_turn = False,): #main
    if i != None:
        place[i] = '0'
        if cross_turn:
            place[i] = 'x'

        result = search_for_a_visitor(place)
        # if result == False:
        #     print(result)
        #     for i in range(len(place)):
        #         print(place[i], end=' ')
        #         if (i + 1) % 3 == 0:
        #             print()
        #     print('\n________________\n')

        if result == None:
            vals[2] += 1

        if result:
            vals[0] += 1
        else:
            vals[1] += 1

        if len(number_of_values) == 0:
            return vals


    for i in number_of_values:
        temp = number_of_values.copy()
        temp.remove(i)
        vals = finding_x_0(place.copy(), temp, vals,i, not cross_turn)

    return vals



place = [None, None, None, None, None, None, None, None, None]
posible_turns = [0, 1, 2, 3, 4, 5, 6, 7, 8]
vals = [0, 0, 0]
labels = ['x', '0', 'None']

vals = finding_x_0(place, posible_turns, vals) #start

plt.pie(vals, labels=labels,  autopct='%1.1f%%') #paint
plt.title('проценты побед в крестиках и ноликах')
plt.show()
