import keyword

def question_out_put(str):
    return str,str[0],str*2

def str_output():
    str = "{s}{c}{j}".format(j='Jaipur',s='Swati',c ='Computers')
    print(str)

def use_split():
    str =  "apple#banana#kiwi#orange#TOTO"
    return (str.split("#",3))

def wave(words):
    """wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]"""
    result = []
    chars = list(words)
    for index, char in enumerate(chars):
        if char.isalpha():
            copy = chars[:]
            copy[index] = copy[index].upper()
            result.append(''.join(copy))
    return result

def array_diff(array, single_array_value ):
    #your code here
    result =[]
    
    if len(single_array_value)<1:
        return array

    for value1 in array:
      
        for value2 in  single_array_value:
             if value1 != value2:
                result.append(value1)
         
    return result

def array_diff_short(a, b):
    return [x for x in a if x not in b]
    
def find_missing(sequence):
    t = sequence
    return (t[0] + t[-1]) * (len(t) + 1) / 2 - sum(t)

def remove_str_list(word):
    result = list(word).remove('')

    return result

def input_N_numbers_in_list():
    """Play with input"""
    nums = []
    n= int(input("enter number"))

    for i in range(0,n):
        ele = int(input("Enter number"))
        nums.append(ele)

    print(nums)






if __name__ =="__main__":
    # print(question_out_put([109,'swati']))
    # print(keyword.kwlist)
    # str_output()
    # print(use_split())
    # print(wave("a  b"))
    # print(array_diff([1,2,3,4,4],[4,3]))
    # print(remove_str_list(['', "swatiComputers", '', "is", "best", '']))
    input_N_numbers_in_list()



