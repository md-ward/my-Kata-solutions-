class Solution:
    def romanToInt(self ,num:str)->int:
        roman_numbers = {'I':             1,
                'V':             5,
                'X':             10,
                'L':             50,
                'C':             100,
                'D':             500,
                'M':             1000}

        result = 0
        for i in range(len(num)):
            if i+1<len(num) and roman_numbers[num[i]]<roman_numbers[num[i+1]]:
                result-=roman_numbers[num[i]]
            else :
                result+=roman_numbers[num[i]]
                    

        return result


