# Function to check if highway exists between two cities
# def does_highway_exist(city1, city2):
#     for highway in highways:
#         if [city1,city2]==highway:
#             return True
#     return False
# print(does_highway_exist(2,5))

# print(compute_h_cost(1))

###### Class definition for city ######
# class City:
#     # Object constructor
#     def __init__(self,city_name):
#         self.city_name=city_name
#
#     def compute_g_cost(city1,city2):
#         if city1==starting_city:
#             return 0
#         else:
#             c1x1 = cities[city1][0]
#             c1y1 = cities[city1][1]
#             c2x2 = cities[city2][0]
#             c2y2 = cities[city2][1]
#
#         return math.sqrt(abs(pow(c1x1,2)-pow(c2x2,2)) + abs(pow(c1y1,2)-pow(c2y2,2)))

###### Class definition for city ENDS ######
#
# vars=[]
# for city in cities:
#     var = "City"+str(city)
#     vars.append(var)
#
# # Creating objects for cities
# for var in vars, city in cities:
#     print(var)
#     var=City(city)
#
# print(City1.city_name)

    #use min(list)

# Reading the input from yaml file
import sys,math,yaml
file = open(sys.argv[1] ,'r')
input_data = yaml.load(file)
file.close()

# Loading data
starting_city = input_data["start"]
destination_city=input_data["end"]
highways=input_data["highways"]
cities=input_data["cities"]

print("Calculating the distance from City%s to City%s..." %(starting_city,destination_city))

# Function to find the connecting cities
def find_connecting_cities(city):
    connecting_cities=[]
    for highway in highways:
        if highway[0]==city:
            connecting_cities.append(highway[1])
    return connecting_cities
# print(find_connecting_cities(1))

# Function to compute the total path cost
def compute_path_cost(city1,city2):
    return (compute_g_cost(city1,city2) + compute_h_cost(city1))

# Function to compute the g cost
def compute_g_cost(city1,city2):
    if city1==starting_city:
        return 0
    else:
        c1x1 = cities[city1][0]
        c1y1 = cities[city1][1]
        c2x2 = cities[city2][0]
        c2y2 = cities[city2][1]

    return math.sqrt(abs(pow(c1x1,2)-pow(c2x2,2)) + abs(pow(c1y1,2)-pow(c2y2,2)))
    # return city.previous_city_gscore

# Function to compute the heuristic cost
def compute_h_cost(city):
    c1x1 = cities[city][0]
    c1y1 = cities[city][1]
    c2x2 = cities[4][0]
    c2y2 = cities[4][1]

    return math.sqrt(abs(pow(c1x1-c2x2,2)) + abs(abs(pow(c1y1-c2y2,2))))

# Initilizing variables
visited_cities=[]
non_visited_cities=[]
current_city=previous_city=starting_city

# Adding the starting city to the non visited cities
non_visited_cities.append(current_city)

# A* algorithm
while non_visited_cities:
    # current_city=min(non_visited_cities)
    current_city=non_visited_cities.pop()

    path_cost_list=[]
    print("Current city:%s | Previous City:%s" %(current_city,previous_city))

    if current_city==destination_city:
        print("Destination Reached")
        print("Total distance covered is...")
        break;
    else:
        neighbouring_cities= find_connecting_cities(current_city)
        if not neighbouring_cities:
            print("NO PATH EXISTS")
        else:
            print("Neighbouring cities:%s" %neighbouring_cities)

            for city in neighbouring_cities:
                non_visited_cities.append(city)
                path_cost=compute_path_cost(city,previous_city)
                print("Current city path cost:%f" %path_cost)
                path_cost_list.append(path_cost)

            print("Non visited cities:%s" %non_visited_cities)
            print("Path cost list:%s" %path_cost_list)

            visited_cities.append(current_city)
            previous_city=current_city
