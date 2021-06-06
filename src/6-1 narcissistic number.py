"""
打印水仙花数
"""

for i in range(100,1000):
    hundred_digit=i//100
    ten_digit=(i-hundred_digit*100)//10
    unit_digit=i-hundred_digit*100-ten_digit*10
    if hundred_digit**3 + ten_digit**3 +unit_digit**3==i:
        print(i)