import comb

weight_value = {10:60,20:100,30:120}

power_set_list =  comb.list_powerset(weight_value.keys())
result = {}
for x in power_set_list:
    key = ','.join([str(z) for z in x])
    value = sum([weight_value[y] for y in x]) if sum(x) <= 50 else 0

    result.update({key:value}) 
print(max(result.values()))    
