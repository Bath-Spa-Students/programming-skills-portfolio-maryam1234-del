def make_shirt(size='large', message='I love Python!'):
    """Give an overview of the shirt that will be produced."""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Programming is hard.')
