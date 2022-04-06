

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

    another_movie = [
        {
        'name' : 'The Matrix', 
        'genre' : 'action'
        }
    ]
    extra_pizza_toppings = {
        'bacon',
        'sausage'
    }
    dict['movies'].append(another_movie)
    add_pizza_toppings(dict, extra_pizza_toppings)
    list.sort(dict['pizza_toppings'])
    print(dict['pizza_toppings'])
    
def add_pizza_toppings(dict, extra_pizza_toppings):
    for p in extra_pizza_toppings:
        dict['pizza_toppings'].append(p)

main()
