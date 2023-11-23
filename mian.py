# Write a function called reverse_string that takes a string as input and returns its reverse.
# example  "hello" => "olleh"
def reverse(string):
    string = string[::-1]
    return string

s = "hello"

print(s)
print(reverse(s))



# Write a function called is_palindrome that takes a string as input and
# returns True if the string is a palindrome and False otherwise.
# examoles "sosa" => False
# example  "A man, a plan, a canal: Panama" => True



def is_Palindrome(n):
    n = n.lower()   #convert to lowercase
    nn = n.replace(":", "")  #To remove a specific character, such as ":"
    return nn == nn[::-1]

print(is_Palindrome("radar"))
print(is_Palindrome("sosa"))



# Write a function called remove_duplicates that takes a list as input and
# returns a new list with duplicate elements removed.
# example [3,2,2,4,5] => [3,2,4,5]

def Remove(duplicate):
    new_list = []
    for num in duplicate:
        if num not in new_list:
            new_list.append(num)
    return new_list

duplicate = [3,2,2,4,5]
print(Remove(duplicate)) # here we keep the order of number in the list

# or quick way but the order of number will be in ascending order
duplicate = [3,2,2,4,5]
print(list(set(duplicate)))


# Write a function called list_sum that takes a list of numbers as input and
# returns the sum of all elements.
# example [5,5,5] => 15

def list_sum(num):
    return sum(num)

list = [5, 5, 5]
list_summ = list_sum(list)

print(list_summ)

# an other way

def list_sum(list):
    ret=0
    for i in list:
        ret += i
    return ret

print (list_sum([5,5,5]) )

# Write a function called remove_element that takes a list and an element
# as input and removes all occurrences of that element from the list.
# The function should return the modified list.
# example [1,2,6,5,3], 3 => [1,2,6,5]


def remove_element(element, list):
  list.remove(element)
  return list

list = [1,2,6,5,3]
print(remove_element(3, list))


