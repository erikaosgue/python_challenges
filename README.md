 Python Challenges

Tasks:books:

[0. Triangle Quest](https://github.com/erikaosgue/python_challenges/blob/master/0-triangle_quest.py)

You are given a positive integer `N`. Print a numerical triangle of height `N-1`

like the one below:

    1
    22
    333
    4444
    55555
    ......

Can you do it using only arithmetic operations, a single for loop and print statement?
Use no more than two lines. 

[1. Reverse Words](https://github.com/erikaosgue/python_challenges/blob/master/1-reverse_words_and_swap_cases.py)
 
Complete the 'reverse_words_order_and_swap_cases' function

The function is expected to return a STRING.
The function accepts STRING sentence as parameter.
Example:
    
    reverse_words_order_and_swap_cases("aWESOME is cODING")
    
    result = Coding IS Awesome


[2. Swap Cases](https://github.com/erikaosgue/python_challenges/blob/master/2-swap_case.py)

You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

[3. split and Join](https://github.com/erikaosgue/python_challenges/blob/master/3-split_and_join_str.py)

You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Input Format
The first line contains a string consisting of space separated words.

Output Format
Print the formatted string as explained above.

[4.](https://github.com/erikaosgue/python_challenges/blob/master/4-pairing_socks.py)

Count the amount of pairs numbers that exists in a given array
where n first parameter is the length of the array, second parameter is a list of numbers

usage:

n
x, y, z

Example:
$ ./4-pairing_socks.py
3
1 2 2
1 <= is the output



[5.](https://github.com/erikaosgue/python_challenges/blob/master/5-counting_valleys.py)
 
Complete the 'countingValleys' function

The function is expected to return an INTEGER.
The function accepts following parameters:
1. INTEGER steps
2. STRING path

[6.](https://github.com/erikaosgue/python_challenges/blob/master/6-jumping_on_the_clouds.py)

count the amount of valleys that a hikers does
A mountain is a sequence of consecutive steps above sea level. Starting with a setup from sea level and ending with a step down to sea level

A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level
valley ends only when it is a step above sea level 

[7. write a function for leap year](https://github.com/erikaosgue/python_challenges/blob/master/7-write_a_function.py)

Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function

[8. Numpy array](https://github.com/erikaosgue/python_challenges/blob/master/8-numpyt_array.py)

You are given a space separated list of nine integers. Your task is to convert this list into a 3X3 NumPy array. 

[9. Repeated String](https://github.com/erikaosgue/python_challenges/blob/master/9-repeated_string.py)

There is a string,`s` , of lowercase English letters that is repeated infinitely many times. Given an integer, `n`, find and print the number of letter a's in the first

letters of the infinite string.

Example

    s = 'abcac'
    n = 10

The substring we consider is `abcacabcac`, the first `10` characters of the infinite string. There are `4` occurrences of a in the substring. 

[10](https://github.com/erikaosgue/python_challenges/blob/master/10-parallel_processing.py)
[11](https://github.com/erikaosgue/python_challenges/blob/master/11-sort_roman_numbers.py)

Function that sorts names with roman numbers
Example:
input_array = ['Juan X', 'Sebastian XL', 'Cristian III', 'Julio IV', 'Juan XII']
output: ['Cristian III', 'Juan X', 'Juan XII', 'Julio IV', 'Sebastian XL']

[12](https://github.com/erikaosgue/python_challenges/blob/master/12-sort_transaction.py)

Count the amount of names, that are in the array and sort first by the count then by name, where the count should start with the biggest value

Example:

input_array = ['Dog', 'Cat', 'Bird', 'Snake', 'Dog', 'Snake', 'Snake'], 'Bird'
output = ['Snake 3', 'Bird 2', 'Dog 2', 'Cat 1']


[13. housrglass 2D array]()

Given a 6x6 2D Array, arr :
    1 1 1 0 0 0
    0 1 0 0 0 0
    1 1 1 0 0 0
    0 0 0 0 0 0
    0 0 0 0 0 0
    0 0 0 0 0 0

An hourglass in A is a subset of values with indices falling in this pattern in  arr's graphical representation:
    a b c
      d
    e f g

There are 16 hourglasses in arr. An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum. The array will always be 6x6.

In the example above the output should be
output:
    7

[14  Left Rotation]()

Given an array ```a``` of ```n``` integers and a number, ```d``` , perform ```d```   left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.

Returns

int a'[n]: the rotated array

Example:

    5 4 
    1 2 3 4 5

5 is the len of the array, 4 number of left rotations
output:

    5 1 2 3 4

[15 New year caos]()

It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker indicating their initial position in the queue from 1 to n. Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker. One person can bribe at most two others.

Determine the minimum number of bribes that took place to get to a given queue order. Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.

Returns:
No value is returned. Print the minimum number of bribes necessary or Too chaotic if someone has bribed more than  people.


[16]

[17]