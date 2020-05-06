destinations = ["Paris, Grance", "Shanghai, China","Los Angeles, USA"]

def get_destination_index(destination):
        return destinations.index(destination)
print(get_destination_index("Los Angeles, USA"))

def get_traveler_location(traveler):
        traveler_destination = traveler[1]
        return get_destination_index(traveler_destination)

attractions = [[].[].[]]
def add_attraction(destination, attraction):
        try:
                destination_index = get_destination_index(destination)
                attraction_for_destination = attractions[destination_index]
                attraction_for_destination.append(attraction)
        except ValueError:
        print(f"{destination} is spelled wrong")

add_attraction("Los Angeles, USA", ['Venice Beach',['beach']])
add_attraction("Paris, France", ['the Louvre', ['art','museum']])

def find_attractions(destination, interests):
        destination_index = get_destination_index(destination)
        attractions_in_city = attractions[destination_index]
        attractions_with_interest = []
        for attraction in attractions_in_city:
                possible_attraction = attraction
                attraction_tags = attraction [1]
                for interest in interests:
                        if interest in attraction_tags:
                                attractions_with_interest.append(possible_attraction[0])
        return attractions_with_interest

def get_attractions_for_traveler(traveler):
        traveler_destination = traveler[1]
        traveler_interests = traveler [2]
        traveler_attractions = find_attractions(traveler_destination,traveler_interests)
        interests_string = (f"Hi {traveler[0]}, we think you will like these places around {traveler_destination}, we think you'll like these places around: {traveler_attractions}")
        print(interests_string)

smills_france = get_attractions_for_traveler(['Fergus Fettes', 'Paris, France', ['momument']])
print(smills_france)

