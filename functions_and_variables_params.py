# We declare *args in the function to specify it can take a variable number of parameters
def sum(title: str, *numbers: int) -> int:
    print(title)
    result = 0
    for n in numbers:
        result += n
    return result


# We declare **kwargs in the function to specify it can take
def new_sum(title, **grades: int) -> int:
    print(title)
    result = 0
    for n in grades.values():
        result += n
    return result


print(sum("Grades", 13, 32, 54, 43, 9))
print(sum("grade", 2, 65, 321))
print(new_sum("New grades", maths=14, history=13))



def person(name: str, age: int, heigh: float) -> tuple[str, int] or tuple[str, int, float]:
    if heigh == 0:
        return name, age
    return name, age, heigh


name, age, heigh = person("Julie", 23, 1.64)
print(name, age, heigh)


# ----------------------- FUNCTIONS AND TUPLES -----------------------

def get_information():
    return "Bobby", 34, 1.81


def display_information(name, age, heigh):
    print(f"Name: {name}, Age: {age}, Heigh: {heigh}")


# We can unpack the tuple returned by the function with the syntax below
name, age, heigh = get_information()
print(name, age, heigh)

# We can pass an unpacked tuple as a multiple set of parameters to the function
info = get_information()
display_information(*info)  # equivalent to display_information(info[0], info[1], info[2])