def make_shirt(size, message):
    """Give an overview of the shirt that will be produced."""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

make_shirt('large', 'I love frocks!')
make_shirt(message="Readability counts.", size='large')
