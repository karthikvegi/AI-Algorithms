# Reading the input from yaml file
import sys,math,yaml,collections
file = open(sys.argv[1] ,'r')
input_data = yaml.load(file)
file.close()

# Loading data
starting_city =input_data["start"]
destination_city=input_data["end"]
highways=input_data["highways"]
cities=input_data["cities"]

print("Calculating the shortest distance from City%s to City%s using A* algorithm" %(starting_city,destination_city))

# Function to find the connecting cities
def find_connecting_cities(city):
    connecting_cities=[]
    for highway in highways:
        if highway[0]==city:
            connecting_cities.append(highway[1])
    return connecting_cities

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
cost_dict={}

# Adding the starting city to the non visited cities
non_visited_cities.append(current_city)

# A* algorithm begins
while non_visited_cities:
    non_visited_cities.pop()

    ordered_cost_cities=[]
    ordered_cost_distance=[]

    # Picking the next city with minimum path cost
    ordered_cost= collections.OrderedDict(sorted(cost_dict.items()))
    for distance,city in ordered_cost.items():
        ordered_cost_cities.append(city)
        ordered_cost_distance.append(distance)

    if current_city!=starting_city:
        current_city=ordered_cost_cities[0]

    cost_dict={}
    print("Current city:%s | Previous City:%s" %(current_city,previous_city))

    # Destination found
    if current_city==destination_city:
        print("***DESTINATION REACHED | DISTANCE COVERED:%f ***" %ordered_cost_distance[0])
        break;
    else:
        # Highway doesn't exist
        neighbouring_cities= find_connecting_cities(current_city)
        if not neighbouring_cities:
            print("***NO PATH EXISTS***")
            break;
        else:
            print("Neighbouring cities:%s" %neighbouring_cities)

            for city in neighbouring_cities:
                non_visited_cities.append(city)
                path_cost=compute_path_cost(city,previous_city)
                cost_dict[path_cost]=city

            visited_cities.append(current_city)
            print("Visited Cities:%s" %visited_cities)
            print("Non visited cities:%s" %non_visited_cities)
            print("-"*30)
            previous_city=current_city
            current_city=""
