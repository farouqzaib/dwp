import geopy.distance

LONDON_COORDS = (51.509865, -0.118092)

def filter_people_30_miles_around_london(people):
    '''
    Filters a list of people to return only those 30 miles around London
    Args:
        people (list): List of people

    Returns:
        list: People living 30 miles around London
    '''
    
    people_around_london = []
    for person in people:
        query_coords = (float(person['latitude']), float(person['longitude']))

        try:
            distance = geopy.distance.distance(LONDON_COORDS, query_coords).miles
        except:
            raise Exception('We encountered an error while calculating distance between coordinates.')
            
        if distance <= 30:
            people_around_london.append(person)

    return people_around_london
    