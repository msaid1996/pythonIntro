student_1 = {
    "name": "kate",
    "stream": "data",
    "number": 3,
    "snacks": ["biscuits","nutella"],       #list
    "other_dict": {                         #sub dict
        "other_key": "other value",
        "key_2": "val"
    }
}

print(student_1)        # returns the whole key & value pairs

# select 1 specific key in dict
print(student_1["stream"])          #returns 'data'

#select 1 specific value "biscuit" pair within a list (key) in a dict
print(student_1["snacks"][0])       #returns 'biscuit'

#select key in sub dict in main dict
print(student_1["other_dict"]["key_2"])       #returns 'val'


#------------------------reassignment
print("----------------------------------------")

print(student_1)            #old
student_1["name"] = "bob"
print(student_1)            #update

#--------------------------remove
print("----------------------------------------")

print(student_1)            #old
student_1["snacks"].remove("nutella")           #removing nutella - possible as it is in a list
print(student_1)            #new

#---------------------------return the values
print("----------------------------------------")

print(student_1)            #old
student_1.keys()           #return values
print(student_1)            #new

#-ex
print("-------------------- Exercise:")
m_profile = {
    "name": "miza",
    "course": "data",
    "start date": "February 2020",
    "end date": "April 2020",
    "topics": {
        "SQL": ["a","b"],
        "Python": ["a","b"],
        "Nosql": ["a","b"],
        "Big Data": ["a","b"],
    }
}

print(m_profile)        # returns the whole key & value pairs

a_profile = {
    "name": "miza",
    "course": "data",
    "date": [{"sdate":2019},
             {"edate":2020}],
    "topics": {
        "SQL": ["a","b"],
        "Python": ["a","b"],
        "Nosql": ["a","b"],
        "Big Data": ["a","b"],
    }
}
print("---------------------print a_profile")
print(a_profile)

#collect 2020
print("---------------------collect 2020")
print(a_profile["date"][1]["edate"])



