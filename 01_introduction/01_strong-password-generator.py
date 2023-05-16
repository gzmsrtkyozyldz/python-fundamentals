# Strong password generator
# Long at least 16 characters.
# Uses symbol punctuation:
# Includes uppercase and lowercase letters.
# Includes numbers.

from string import punctuation

username = input('Please enter an username:')
password = input('Please enter strong password:')
if len(password) >= 16:
    for i in password:
        pass
else:
    print('Password length must be at least 16 characters..')
nums = False
is_upper = False
is_lower = False
sym = False
for character in password:
    if character.isdigit():
        nums = True
    elif character.isupper():
        is_upper = True
    elif character.islower():
        is_lower = True
    elif character in punctuation:
        sym = True
# When comparing a variable to True, you should use the form if x is True or simply if x.
# The most common incorrect form is if x == True.
if nums is True and is_upper is True and sym is True and is_lower is True: # if nums == True yerine is
    print('Your password is correct..')
else:
    print('Your password is not correct..Please check the terms..')