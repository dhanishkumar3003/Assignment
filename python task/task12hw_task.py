detail=[
    {'name':'shreya','age':15},
    {'name':'pratiksha','age':13},
    {'name':'prerna','age':15}
]
sorted_list = sorted( detail, key=lambda val: val['age'] )
print(sorted_list)