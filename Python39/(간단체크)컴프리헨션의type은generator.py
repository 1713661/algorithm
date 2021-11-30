print((1 if c1!=c2 else 0) for c1,c2 in zip("pig","wig")) # <generator object <genexpr> at 0x0000019F64889510>

print(type((1 if c1!=c2 else 0) for c1,c2 in zip("pig","wig"))) # <class 'generator'>

print(list((1 if c1!=c2 else 0) for c1,c2 in zip("pig","wig"))) # [1, 0, 0]

print(iter((1 if c1!=c2 else 0) for c1,c2 in zip("pig","wig"))) # <generator object <genexpr> at 0x000001D363119510> 에러안나는걸로봐서 iterable객체맞는듯?
# iter(호출가능한객체, 반복을끝낼값)