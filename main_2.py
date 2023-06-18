import matplotlib.pyplot as plt

def search_for_a_vin(plase): #count
    diagonal_right = [0, 4, 8]
    diagonal_left = [2, 4, 6]
    horihontal_start = [0, 3, 6]
    temp_chet_vin = 0

    for i in range(3):

        #vertical
        if plase[i] == 'x' and plase[i + 3] == 'x' and plase[i + 6] == 'x':
            return True
        if plase[i] == '0' and plase[i + 3] == '0' and plase[i + 6] == '0':
            return False



    #horizontal
    if plase[horihontal_start[0]] == 'x' and\
            plase[horihontal_start[1]] == 'x' and\
            plase[horihontal_start[2]] == 'x':
        return True
    if plase[horihontal_start[0]] == '0' and\
            plase[horihontal_start[1]] == '0' and\
            plase[horihontal_start[2]] == '0':
        return False


    #diagonals
    #right
    if plase[diagonal_right[0]] == 'x' and\
            plase[diagonal_right[0+1]] == 'x' and\
            plase[diagonal_right[0+2]] == 'x':
        return True

    if plase[diagonal_right[0]] == '0' and\
            plase[diagonal_right[1]] == '0' and\
            plase[diagonal_right[2]] == '0':
        return False

    #left
    if plase[diagonal_left[0]] == 'x' and\
            plase[diagonal_left[1]] == 'x' and\
            plase[diagonal_left[2]] == 'x':
        return True

    if plase[diagonal_left[0]] == '0' and\
            plase[diagonal_left[1]] == '0' and\
            plase[diagonal_left[2]] == '0':
        return False
    return None



def finding_x_0(place, number_of_values, vals,i = None, cross_turn = False,): #main
    global games_count
    games_count += 1
    if i != None:
        place[i] = '0'
        if cross_turn:
            place[i] = 'x'

        result = search_for_a_vin(place)

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
games_count = 0

vals = finding_x_0(place, posible_turns, vals) #start

print(games_count)
plt.pie(vals, labels=labels,  autopct='%1.1f%%') #paint
plt.title('проценты побед в крестиках и ноликах')
plt.show()
