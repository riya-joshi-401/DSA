def rotate( li, n):
    
    li.insert(0,li[-1])
    del li[-1]
    return li
