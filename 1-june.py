def reverseString(s):
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(0,len(s)//2):
            j=len(s)-1-i
            s[i],s[j]=s[j],s[i]
        return s
s= ["h","e","l","l","o"]
print(reverseString(s))