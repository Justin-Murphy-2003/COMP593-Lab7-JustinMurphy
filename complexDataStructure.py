

def main():
    dict = {
        'name' : 'Justin',
        'student_id' : 10261574,
        'pizza_toppings' : [
            'mushrooms',
            'pepperoni',
            'olives'
        ],
        'movies' : [ 
            {
                'name' : 'The Lego Movie',
                'genre' : 'family'
            },
            {
                'name' : 'Free Guy',
                'genre' : 'comedy'
            }
        ]
    }

    another_movie = {
        'name' : 'The Matrix', 
        'genre' : 'action'
    }
    
    extra_pizza_toppings = {
        'bacon',
        'sausage'
    }
    dict['movies'].append(another_movie)
    add_pizza_toppings(dict, extra_pizza_toppings)
    list.sort(dict['pizza_toppings'])
    print(dict)
    sentences(dict)
    
def add_pizza_toppings(dict, extra_pizza_toppings):
    for p in extra_pizza_toppings:
        dict['pizza_toppings'].append(p)

def sentences(dict):
    print("Hi Jeremy, my name is", dict['name'], "and my student number is", dict['student_id'])
    toppings = ''
    for p in dict['pizza_toppings']:
        toppings += p + ' '
    print("My ideal pizza has", toppings)
    genres = ''
    for m,g in enumerate(dict['movies']):
        genres += g['genre']
        if m == len(dict['movies']) -2:
            genres += ', & '
        elif m == len(dict['movies']) -1:
            genres += ' '
        else:
            genres += ', '
    print("I like to watch", genres + "movies")

    movie_names = ''
    for m,g in enumerate(dict['movies']):
        movie_names += g['name']
        if m == len(dict['movies']) -2:
            movie_names += ', & '
        elif m == len(dict['movies']) -1:
            movie_names += ' '
        else:
            movie_names += ', '
    print("Some of my favourites are " + movie_names)
main()
