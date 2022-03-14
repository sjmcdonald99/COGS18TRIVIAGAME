"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from functions import check_answer, display_score, play_again
##
##

def test_check_answer():

    assert check_answer(2,2) == 1
    assert check_answer (2,1) == 0

def test_display_score():

    assert (callable (display_score))
    
def test_play_again():
    
    assert (callable (play_again))
    



                 
    