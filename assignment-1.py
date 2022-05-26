'''Assignment 1

This assignment covers your basic profiency with
    Python. It engages your ability to transform
    data without affecting anything outside the program.

This assignment places heavy emphasis on basic Python constructs.
'''

def factorial(x):
    '''Item 1. 
    Factorial. 1 point.
    
    Returns the factorial of an integer.
    An integer's factorial is the product of the integer and all
        integers below it.

    Parameters
    ----------
    x: int
        the integer whose factorial to return

    Returns
    -------
    integer
        the factorial of the argument
    '''
    # Write your code below this line
    output = 0
    if x==0:
        return 1
    else:
        output = 1
    # Multiply all numbers from 1 to x
    for i in range(1, x+1):
        output *= i
    return output


def classify_grade(number_grade):
    '''Item 2.
    Classify Grade. 2 points.
    
    Returns the letter grade equivalent of a number grade.
    For this item, use these letter grade buckets:
        A: 92-100
        B+: 86-91.9
        B: 80-85.9
        C+: 74-79.9
        C: 67-73.9
        D: 60-66.9
        F: 0-59.9

    Parameters
    ----------
    number_grade: float
        the number grade to convert into a letter grade.

    Returns
    -------
    str
        the letter grade equivalent of the number grade.
    '''
    # Write your code below this line
    if number_grade>=92:
        return "A"
    elif number_grade>=86:
        return "B+"
    elif number_grade>=80:
        return "B"
    elif number_grade>=74:
        return "C+"
    elif number_grade>=67:
        return "C"
    elif number_grade>=60:
        return "D"
    elif number_grade>=0:
        return "F"


def average_weight(item_quantity_1, item_weight_1, item_quantity_2, item_weight_2):
    '''Item 3.
    Average Weight. 3 points.
    
    You have purchased two bags of items. 
    The first bag contains one type of item, and the second bag contains another type.
    Return the weighted average weight of the items.
        
    Parameters
    ----------
    item_quantity_1: int
        the quantity of items in the first bag.
    item_weight_1: float
        the weight of each individual item in the first bag.
    item_quantity_2: int
        the quantity of items in the second bag.
    item_weight_2: float
        the weight of each individual item in the second bag.

    Returns
    -------
    float
        the weighted average weight of one item.
    '''
    # Write your code below this line
    item1_weighted = item_quantity_1*item_weight_1
    item2_weighted = item_quantity_2*item_weight_2
    sum_item1_2_weighted = item1_weighted+item2_weighted
    total_weight = item_weight_1+item_weight_2
    return sum_item1_2_weighted/total_weight

def string_sum(string):
    '''Item 4.
    String Sum. 3 points.
    
    Returns the sum of the digits provided in a string.
    For this item:
        1. Sum the digits contained in the string.
        2. Ignore any non-digit characters contained in the string.

    Parameters
    ----------
    string: str
        a string that can contain any character.

    Returns
    -------
    int
        the sum of the digits contained in the string.
    '''
    # Write your code below this line
    output = 0
    for char in string:
        if char.isdigit():
            output+= int(char)
    return output



def distance(x_1, y_1, x_2, y_2):
    '''Item 5.
    Distance. 3 points.

    Returns the distance between two points.
    To get the distance between two points:
        1. Get the difference between the two x-coordinates
        2. Get the difference between the two y-coordinates
        3. Sum the previous two values
        4. Return the square root of the sum

    You may want to import the `math` library for this number.

    Parameters
    ----------
    x_1: float
        the first x-coordinate
    y_1: float
        the first y-coordinate
    x_2: float
        the second x-coordinate
    y_2: float
        the second y-coordinate

    Returns
    -------
    float
        the distance between the two coordinates
    '''
    # Write your code below this line
    # NOTE: The correct distance formula is sqrt((x_2-x_1)^2+(y_2-y_1)^2)) but
    # the instructions above lacks the squaring of x coordinates' difference and
    # y coordinates' difference
    # This is the code that follows the instructions above.

    # import math
    # x_diff = x_1-x_2
    # y_diff = y_1-y_2
    # return math.sqrt(x_diff+y_diff)

    # This is the code that adheres to the correct distance formula
    import math
    x_diff = x_2-x_1
    y_diff = y_2-y_1
    return math.sqrt(x_diff**2+y_diff**2)




def make_change(amount):
    '''Item 6.
    Make Change. 5 points.
    
    Return the combination of coins needed to make change for the given amount,
        which is given in centavos.
    For this item:
        1. You can return 1 peso, 25 centavos, 10 centavos, 5 centavos, and 1 centavo coins.
        2. Use the minimum number of coins possible.

    Parameters
    ----------
    amount: int
        the amount, in centavos, to make change for.

    Returns
    -------
    str
        the string representation of the change to be given.
        Format it like this:
            "1P:{amount}/25C:{amount}/10C:{amount}/5C:{amount}/1C:{amount}"
    '''
    # Write your code below this line
    remainder = amount
    amount_1P = 0
    amount_25C = 0
    amount_10C = 0
    amount_5C = 0
    amount_1C = 0

    while remainder>0:
        if remainder//100 >=1:
            amount_1P = remainder//100
            remainder -= 100*amount_1P
        if remainder//25 >=1:
            amount_25C = remainder//25
            remainder-= 25*amount_25C
        if remainder//10>=1:
            amount_10C = remainder//10
            remainder -= 10*amount_10C
        if remainder//5>=1:
            amount_5C = remainder//5
            remainder -= 5*amount_5C
        if remainder//1>=1:
            amount_1C = remainder//1
            remainder -= 1*amount_1C

    return (f"1P:{amount_1P}/25C:{amount_25C}/10C:{amount_10C}/5C:{amount_5C}/1C:{amount_1C}")


