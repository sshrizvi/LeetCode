def romanToInt(s: str) -> int:
    num = 0
    for i in range(len(s)):
        if (i < len(s)-1):
            if s[i] == 'I':
                if s[i+1] in ['V','X']:
                    num = num - 1
                else:
                    num = num + 1

            elif s[i] == 'V':
                    num = num + 5

            elif s[i] == 'X':
                if s[i+1] in ['L','C']:
                    num = num - 10
                else:
                    num = num + 10

            elif s[i] == 'L':
                    num = num + 50

            elif s[i] == 'C':
                if s[i+1] in ['D','M']:
                    num = num - 100
                else:
                    num = num + 100

            elif s[i] == 'D':
                    num = num + 500

            elif s[i] == 'M':
                    num = num + 1000

            else:
                pass
        
        else:
            if s[i] == 'I':
                    num = num + 1

            elif s[i] == 'V':
                    num = num + 5

            elif s[i] == 'X':
                    num = num + 10

            elif s[i] == 'L':
                    num = num + 50

            elif s[i] == 'C':
                    num = num + 100

            elif s[i] == 'D':
                    num = num + 500

            elif s[i] == 'M':
                    num = num + 1000

            else:
                pass
        
    return num

print(romanToInt("LVIII"))