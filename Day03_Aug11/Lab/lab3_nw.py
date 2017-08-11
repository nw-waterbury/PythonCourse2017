# Create the following functions: with exceptions, errors, and such
# Create a test for those functions



#Hello. to HELLO!
def shout(txt):
    try:
		new_txt= txt.upper() + "!"
    except AttributeError:
        return "Invalid entry. We are working with strings!"
    return new_txt

# Name to emaN
def reverse(txt):
    if " " in str(txt):
        raise SyntaxError('This function is just for one word!')
    try:
        return txt[::-1]
    except NameError: return "Invalid entry. We are working with strings!"
    except TypeError: return "Invalid entry. We are working with strings!"

# Hello world! to world! Hello
def reversewords(txt):
    try:
         new_txt=txt.split(" ")
    except AttributeError:
         return "Invalid entry. We are working with strings!"
    new_txt2=new_txt[::-1]
    return ' '.join(new_txt2)


# Hello world! to !dlrow olleH
def reversewordletters(txt):
    try:
        switched=txt[::-1]
    except TypeError:
        return "Invalid entry. We are working with strings!"
    return switched

#pig latin

def piglatin(txt):
    try:
        words = txt.split()
    except AttributeError:
        return "Invalid entry. We are working with strings!"
    vowels = ['a', 'e', 'i', 'o', 'u']
    mylist = []
    for ch in words:
        first_letter = list(ch)[0]
        #The rules of pig latin are a little unclear.
        #This is a good effort at one version.
        if first_letter in vowels:
            ch += 'ay'
        else:
            ch = (ch[1:] + first_letter + 'ay')
        mylist.append(ch)
    return ' '.join(mylist)
