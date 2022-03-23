
search: str = "abc"
one_char: str = "b"


count_contains: int = 0
check_contains: bool = False
while count_contains < len(search) and check_contains is False:
    if one_char == search[count_contains]:
        check_contains = True   
    count_contains = count_contains + 1
if check_contains is True:
    print(True)
if check_contains is False:
    print(False)
count_contains = 0 
check_contains = False
