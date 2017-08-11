def ordinal(numb):
    try:
        numb = int(numb)
    except:
        return "Input Not Valid"
    numb=str(numb)
    end = {'1':'st', '2':'nd', '3':'rd'}
    if numb[-2:-1] == '1': return numb+'th'
elif numb[-1] in endings.keys(): return numb+ endings[n[-1]]
    else: return numb+'th'
