'''
ENGLISH
def backtracking_template(choices, other_params):
    if no_more_choices(): # BASE CASE
        return whether_or_not_the_problem_was_solvable
    else:
        for choice in choices:
            # edit choice or other_params to try out the choice
            if is_valid(choice):
                if choice_leads_to_a_success()
                    return success
            # undo that choice if necessary
    return failure

CODE SKELETON

def backtracking_template(choices, other_params):
    if base_case():
        return whether_or_not_the_problem_was_solvable
    else:
        for choice in choices:
            # edit choice or other_params to try out the choice
            if is_valid(choice) && backtracking_template(choice, other_params):
                return success
            # undo that choice if necessary
    return failure

'''



def is_shrinkable(word, lexicon):
    if len(word) == 1:
        return True
    else:
        for letter in range(len(word)):
            shrunken_word = word[:letter] + word[letter+1:]
            if shrunken_word in lexicon and is_shrinkable(shrunken_word, lexicon):
                return True
    return False

lexicon = {'i', 'in', 'sin', 'sing', 'sting', 'string', 'staring', 'starting', 'startling'}

print(is_shrinkable("startling", lexicon))

