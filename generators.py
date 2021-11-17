
def make_song(count,beverage):
    while count>=0:
        if count==1:
            yield f"Only 1 bottle of {beverage} left!"
        elif count==0:
            yield f'No more {beverage}!'
        else: 
             yield (f"{count} bottles of {beverage} on the wall")
        count-=1