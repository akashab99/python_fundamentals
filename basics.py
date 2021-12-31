def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)

    return the_mean

student_grades ={"Marry": 9.1, "Sim": 8.8, "John": 7.5}
print(mean(student_grades))
