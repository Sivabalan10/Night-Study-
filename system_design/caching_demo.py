step = 0
time = 0

database = [f"data {i}" for i in range(100)] # call -> heavy load -> server slow - hard disk ROM

cache_data = [] # - in memory RAM 

user20 = "" # goal -> data 20 

def search_req(target):
    global step
    # cache search
    for data in cache_data:
        step += 1
        if target in data: 
            user20 = data
            return print("Data found in cache- total steps = ",step)
            

    # database search
    for data in database:
        step += 1
        if target in data: 
            user20 = data
            cache_data.append(data)
            return print("Data found in database- total steps = ",step)

    

# req 1
search_req("20") 
time += 1

# req 2
search_req("20") 
time += 1

# req 3
search_req("20") 
time += 1

# req 4
search_req("20") 
time += 1

# req 5
search_req("20") 
time += 1

print(f"Total time - {time}, Total steps - {step}") # total steps