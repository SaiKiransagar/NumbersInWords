
one = [ "zero", "one ", "two ", "three ", "four ",
        "five ", "six ", "seven ", "eight ",
        "nine ", "ten ", "eleven ", "twelve ",
        "thirteen ", "fourteen ", "fifteen ",
        "sixteen ", "seventeen ", "eighteen ",
        "nineteen "];

ten = [ "", "", "twenty ", "thirty ", "forty ",
        "fifty ", "sixty ", "seventy ", "eighty ",
        "ninety "];
 

def calculate(n,s):
    str=''
    if n>19:
        str+= ten[n//10] + ' ' + one[n%10]
        str+= s
    elif n>0 and n < 20:
        str+=one[n]
        str+= s
    else:
        str+=''
    return str

        
def output(i):
    if i<0:
        return 'Enter Positive Number'
    elif i < 20:
        return one[i]
    else:
        out=''
        out += calculate(((i//100000)%1000),'Lakh ')
        out += calculate((i//1000)%100,'Thousand ')
        out += calculate(((i//100)%10),'Hundred ')
        if (i>100) and len(calculate(i%100,''))>1:
            out+= 'and '
        out += calculate(i%100,'')
        return out
        

s= int(input('Enter a number for which it needs translation: '))
print(output(s))
