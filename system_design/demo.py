
# ordering
cash  = 100

if __name__ == "__main__":
    def getamt(): # 1 
        return cash

    def cal_gst(): # 2
        return (cash * (0.1))
    
    def sgst():
        return 10

    def discount():
        return -(cash * 0.3)
    
    def final_amt(add = []): # 3
        sum = 0
        for val in add:
            sum += val()
        
        return sum

    print(final_amt([cal_gst, getamt, sgst, discount])) # 4




