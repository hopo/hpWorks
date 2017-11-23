# https://py.checkio.org/mission/say-history/

"""
In this mission you should write a function that introduce a person with a given parameters in attributes.
Input: Two arguments. String and positive integer.
Output: String.
"""

def say_hi(name, age):
    """
        Hi!
    """
    # your code here
    return "Hi. My name is Alex and I'm 32 years old"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", "First"
    assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", "Second"
    print('Done. Time to Check.')
