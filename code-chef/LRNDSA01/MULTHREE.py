t=int(input())
while(t>0):
    k, d0, d1 = map(int, input().split())
    if(k==2):
        if((d0+d1)%3==0):
            print('YES')
        else:
            print('NO')
    else:
        d2 = (d0+d1) % 10
        if(d2%5==0):
            print('NO')
            t-=1
            continue
        sum_first_digits = d0+d1+d2
        num_middle_digits = (k-3)//4
        num_last_digits = (k-3) % 4
        sum_middle_digits = num_middle_digits*20
        sum_last_digits = 0
        while (num_last_digits > 0):
            sum_last_digits +=( (d2*2) % 10)
            d2 = ((d2*2) % 10)
            num_last_digits-= 1
        total_sum = sum_first_digits+sum_middle_digits+sum_last_digits
        if(total_sum% 3 == 0):
            print("YES")
        else:
            print("NO")
        t-=1
