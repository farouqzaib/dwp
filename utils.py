import geopy.distance

LONDON_COORDS = (51.509865, -0.118092)#London coordinate (Latitude, Longitude) gotten from Google

def filter_people_50_miles_around_london(people):
    '''
    Parses a list of people and returns only those 50 miles around London
    Args:
        people (list): List of people

    Returns:
        list: People living 50 miles around London
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
    