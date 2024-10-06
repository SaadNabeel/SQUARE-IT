
def create_squares(start, end):
    squares = [i**2 for i in range(start, end + 1)]
    return squares


def separate_odds_and_evens(squares):
    odd_squares = [x for x in squares if x % 2 != 0]
    even_squares = [x for x in squares if x % 2 == 0]
    return odd_squares, even_squares


start_range = int(input("Enter the starting number of the range: "))
end_range = int(input("Enter the ending number of the range: "))


squares_list = create_squares(start_range, end_range)


odd_squares, even_squares = separate_odds_and_evens(squares_list)


print("Squares of numbers between {} and {}: {}".format(start_range, end_range, squares_list))
print("Odd squares: {}".format(odd_squares))
print("Even squares: {}".format(even_squares))
