def checkOneL(n1, n2):
    if n1 < n2:
        return True
    else:
        return False

def checkOneG(n1, n2):
    if n1 > n2:
        return True
    else:
        return False

def check(merged_list):
    for i in range(1, len(merged_list), 2):
        curr_num = merged_list[i-1]
        curr_op = merged_list[i]
        next_n = merged_list[i+1]
        
        if curr_op == ">":
            if checkOneL(curr_num, next_n):
                return False


        if curr_op == "<":
            if checkOneG(curr_num, next_n):
                return False

    return True

# NUM : Visited
dc = {1:False, 3:False, 8:False, 6:False, 4:False}

# numList = [8,6,3,1,4]
numList = [1,4,3,8,6]
# numList = [1,3,8,4,6]

opList = ["<", ">", "<", "<"]


def solve(num_list, op_list, dc):

    aux_list = []

    for i in range(len(op_list)):
        aux_list.append(num_list[i])
        aux_list.append(op_list[i])
    aux_list.append(num_list[-1])



    nlist = aux_list[:]

    for i in range(1, len(aux_list), 2):
        
        if not check:
            return
        
        curr_num = aux_list[i-1]
        curr_op = aux_list[i]
        next_n = aux_list[i+1]

        #print(curr_num, curr_op, next_n)

        if curr_op == ">":
            if checkOneG(curr_num, next_n):
                dc[curr_num] = True
                dc[next_n] = True
            else:
                j = i

                if j == 1:
                    aux_list[0], aux_list[2] = aux_list[2], aux_list[0]
                    dc[aux_list[0]] = True

                while j > 0:
                    if checkOneL(curr_num, aux_list[i+1]) and dc[aux_list[i-1]] == True:
                        dc[aux_list[j]] = False
                        aux_list[i-1], aux_list[i+1] = aux_list[i+1], aux_list[i-1]
                        dc[aux_list[i+1]] = True

                    j -= 1

        if curr_op == "<":
            if checkOneL(curr_num, next_n):
                dc[curr_num] = True
                dc[next_n] = True
            else:
                j = i
                
                if j == 1:
                    aux_list[0], aux_list[2] = aux_list[2], aux_list[0]
                    dc[aux_list[0]] = True

                while j > 0:
                    if checkOneG(curr_num, aux_list[i+1]) and dc[aux_list[i-1]] == True:
                        dc[aux_list[j]] = False
                        aux_list[i-1], aux_list[i+1] = aux_list[i+1], aux_list[i-1]
                        dc[aux_list[i+1]] = True

                    j -= 1
    print(*aux_list, sep=" ")


solve(numList, opList, dc)
