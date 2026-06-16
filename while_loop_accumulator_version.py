def get_starting_number():
    while True: 
        how_many_beers = input("How many bottles of beer on the wall? ")
        if how_many_beers.isdigit()==True and int(how_many_beers)>=1:
            return int(how_many_beers)
        else:
            print(f"{how_many_beers} is not a valid response to the question, how many bottles of beer on the wall.")

def sing(how_many_beers):
    n=how_many_beers
    while n>0:
        if n==1:
            current_bottles=f"{n} bottle"
        else:
            current_bottles=f"{n} bottles"
        next_number=n-1
        if next_number==0:
            next_bottles="no more bottles"
            last_line="Take it down"
            ending="!"
        elif next_number==1:
            next_bottles=f"{next_number} bottle"
            last_line="Take one down"
            ending="."
        else:
            next_bottles=f"{next_number} bottles"
            last_line="Take one down"
            ending="."

        print(f"{current_bottles} of beer on the wall, {current_bottles} of beer.")
        print(f"{last_line}, pass it around, {next_bottles} of beer on the wall{ending}")
        n-=1