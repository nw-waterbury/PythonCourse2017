def ordinal(numb):
        if type(numb)!= int:
            return "Not a valid input!"
        else:
            numb=str(numb)
            end = {'1':'st', '2':'nd', '3':'rd'}
            if numb[-2:-1] == '1': return numb+'th'
            elif numb[-1] in end.keys(): return numb+ end[numb[-1]]
            else: return numb+'th'
