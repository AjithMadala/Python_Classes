import json
primary_key='sql_steps'

with open('/Users/ajithmadala/Documents/Projects/BigData/Python/json_proj/data/config.json','r') as f:
    config_file = f.read()


# print(config_file)
# print(type(config_file))
dict=(json.loads(config_file))
print(dict.keys())

check_key=['sql_num','action','sql','next_sql']

#checking if key is present or not
# if primary_key in dict.keys():
#     print("sql_steps key is present")
# else:
#     print("sql_steps key is not present")

#function to validate if object is list
# def is_list():
#     if type(dict[primary_key]) is list:
#         print("sql_steps is a list")
#     else:
#         print("sql_steps is a list")
# is_list()

# for sq_step in check_key:
#     for x in dict[primary_key]:
#         if sq_step in x.keys():
#             print(sq_step + " is present")
#         else:
#             print(sq_step + " is not present")

# 1. sql_num == 1
# 2. if the sql_num is not an integer convert to integer and change it in the dictionary itself

# 3. In Action, read and write are acceptable values, in read - database and parquet, in write parquet


for sq_step in check_key:
    for x in dict[primary_key]:
        if sq_step =='sql_num' in x.keys():
            print(sq_step + " is sqlnum")
            
        else:
            print(sq_step + " is not sql num")
            