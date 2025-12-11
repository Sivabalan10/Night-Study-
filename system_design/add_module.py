def final_amt(add = []): # 3
        sum = 0
        for val in add:
            sum += val()
        
        return sum