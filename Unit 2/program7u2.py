def remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
duplicate = [1,1,11,2,3,2,12,1,1]
print(remove(duplicate))