# first analyze a scenario in which,a  user enter data into dataBase

def insert_into_data(name,age):
    print("name: ",name)
    print("age: ",age)
    print("Inserted into DataBase")
    
# insert_into_data("hamza","fourty")
# issue1: 
# now when a junior developer comes, he/she will see both inputs are string, so he/she will enter str.
#output
# "name:  hamza
# age:  fourty
# Inserted into DataBase"

# issue # 1, solution:
# Type Hints (Type Annotations) are optional labels that tell programmers and tools what type a 
# variable, parameter, or return value is expected to have, but Python does not enforce them at runtime.
def insert_into_data1(name : str,age: int):
    print("name: ",name)
    print("age: ",age)
    print("Inserted into DataBase")
    
# insert_into_data1("hamza","fourtyOne")

#output:
# name:  hamza
# age:  fourtyOne
# Inserted into DataBase

# so to overcome it another solution can be type enforcing:

def insert_into_data2(name : str,age: int):
    
    if type(name) == str and type(age) == int:
     print("name: ",name)
     print("age: ",age)
     print("Inserted into DataBase")
    else:
        raise TypeError("Incorrect Datatype")
    
# insert_into_data2("hamza","fourtyOne")  # this solution works, but this is not scalable, because more function
# can be in code, so for each function we have to do this. so this is where, pydantic comes which help in 
# data validation.

# now another issue is if variables have specific requirements then how can that be handled?
# we want age to be non-neg
def insert_into_data3(name : str,age: int):
    
    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError('age is neg')
        else:
             print("name: ",name)
             print("age: ",age)
             print("Inserted into DataBase")
    else:
        raise TypeError("Incorrect Datatype")
    
insert_into_data3("hello",-2) # so for more varibles we have to put validation for every variable, this is also
# solved by pydantic.



# Issue #1: Type hints only provide guidance and do not enforce data types 
# at runtime; Pydantic solves this by automatically validating and enforcing data types.
# Issue #2: Manually writing validation logic (e.g., checking that age is non-negative) becomes repetitive and hard to 
# maintain; Pydantic also solves this through built-in validation rules and validators