#!/bin/python3
import collections


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony',
    'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots',
    'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    if start_word == end_word:
        return [start_word]
    dictionary = open(dictionary_file).read().split()
    wordstack = []
    wordstack.append(start_word)
    wordqueue = collections.deque([])
    wordqueue.append(wordstack)
    while len(wordqueue) != 0:
        teststack = wordqueue.popleft()
        dictionarycopy = dictionary.copy()
        for word in dictionarycopy:
            if _adjacent(teststack[-1], word) is True:
                if end_word == word:
                    teststack.append(word)
                    return teststack
                copy_of_teststack = teststack.copy()
                copy_of_teststack.append(word)
                wordqueue.append(copy_of_teststack)
                dictionary.remove(word)
    return None


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if ladder == []:
        return False
    for i in range(len(ladder) - 1):
        if _adjacent(ladder[i], ladder[i + 1]) is False:
            return False
    else:
        return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    x = 0
    if len(word1) != len(word2):
        return False
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            x = x + 1
    if x > len(word1) - 2:
        return True
    else:
        return False
