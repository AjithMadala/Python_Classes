#we can pass arguments in any order in keyword arguments but we shouldnt provide any values after keyword arguments


def db_tables(table_name,db_name):
    print(f"Database name is {db_name} and table name is {table_name}")
    
db_tables(db_name="emp",table_name="att")

#positional argument
def greet(name):
    print(f"Hello {name}")
    greet("Rahul")
    
#DEFAULT ARGUMENTS

def greet(name="Guest"):
    print(f"Hello {name}")
    greet()

#postional argument should be defined first and then keyvalue argument
#defining as keyword arguments and in function is good practice