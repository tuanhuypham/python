try: 
    a = int(input())
    b = int(input())

    x = divmod(a,b)
    print("a//b :",a//b)
    print("a mod b",a%b)
    print("divmod : ",x)
except Exception as e:
    print("Error Code:",e)
