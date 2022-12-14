import keyword
import random
from unittest import result
import mysql.connector

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

def encode(st):
    results = ""
    vowels = {'a':'1','e':'2','i':'3','o':'4','u':'5'}

    for c in st:
        if c in vowels:
            results += vowels[c]
        else:
            results +=c

    return  results
    
def decode(st):
    results = ""
    vowels = {'a':'1','e':'2','i':'3','o':'4','u':'5'}

    for c in st:

        if c.isdigit():
            target_key = [key for key in vowels if vowels[key]==c ]
            results += ''.join(target_key)
        else:
            results +=c

    return  results

def encode_short(s, t=str.maketrans("aeiou", "12345")):
    return s.translate(t)
    
def decode_short(s, t=str.maketrans("12345", "aeiou")):
    return s.translate(t)

def prime_numbers():
    for num in range(1,100):
        for i in range(2,num):
            if num%i == 0:
                j=num/i
                print (num ,'not prime')
                break #to move to the next number, the #first FOR
            else:
                print(num, 'is a prime number')

def print_values_tuples():
    name = ['swati', 'sweety', 'shweta']

    for id in range(len(name)):
        print("Hello : ",name[id])
    
    return name
def print_letters_name(st):

    for i in st:
        print(i)
        print('\n')

def draw_stars():

    number_of_raws = int(input("Number of raw : "))
    results = ""
    for i in range(1,number_of_raws +1):
        results +=" "*((number_of_raws)-i)+ '*'*i+'\n'
    return results

def while_to_ten():
    """Exercice 47"""
    i =0
    while i<11:
        print(i)
        i+=1

# Heritage needs to be done
class Compute():
    def __init__(self,ram,storage):
        print("RAM=",ram)
        print("Storage=",storage)

class Laptop(Compute):
    def __init__(self,ram,storage,model):
        print("Model is:",model)
        super().__init__(ram,storage)

"""Write a code to create a for loop that iterates through a tuple of class objects. 
Then call the methods without being concerned about which class type each object is?
"""
# exercice 55
class Shape:
    def __init__(self):
        print('I am a shape')
        
class Rect(Shape):
    def myself(self):
        print("Myself rectangle")

class Sqrt(Shape):
    def myself(self):
        print("Myself square")

class Robot():
    def __init__(self,name=None):
        self.name = name

    def say_hi(self):
        if self.name:
            print("Hello, I am "+ self.name)

        else:
            print("Hello I am robot without name")

    def set_name(self,name):
        self.name = name
    
    def get_name(self):
        return self.name


    







if __name__ =="__main__":
    # print(question_out_put([109,'swati']))
    # print(keyword.kwlist)
    # str_output()
    # print(use_split())
    # print(wave("a  b"))
    # print(array_diff([1,2,3,4,4],[4,3]))
    # print(remove_str_list(['', "swatiComputers", '', "is", "best", '']))
    # input_N_numbers_in_list()
    # print(encode("Puto"))
    # print(decode("P5t4"))
    # prime_numbers()
    # print_values_tuples()
    # print(draw_stars())
    # print(while_to_ten())
    # print(issubclass(Laptop, Compute))
    # r  = Rect()
    # s = Sqrt()

    # for sh in (r,s):

    #     sh.myself()
    
    robot = Robot()
    robot.set_name("Puto")
    robot.say_hi()




