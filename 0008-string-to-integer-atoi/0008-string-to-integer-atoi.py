class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if s=="":
            return 0
        sign = 1
        num = 0
        if s[0]=="-" :
            sign =-1 
        elif s[0]=="+":
            sign =1
        start = 0
        if s[0]=="-" or s[0]=="+":
            start=1
        for ch in s[start:]:
            if (ch).isdigit():
                num =num*10+int(ch)
                continue
            else:
                break
        num = int(num)*sign
        if num>(2**31-1):
            return 2**31-1
        elif num<-1*(2**31):
            return -1*(2**31)
        else :
            return num


