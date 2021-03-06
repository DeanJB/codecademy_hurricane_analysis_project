# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]



# write your update damages function here:
def update_damages(damages_list):
    conversions = {"M": 1000000, "B": 1000000000}
    updated_damages = []
    for x in damages_list:
        if x == "Damages not recorded":
            updated_damages.append(x)
        elif x[-1] == "B":
            clean_num = x.strip("B")
            damage_as_float = (float(clean_num) * conversions["B"])
            updated_damages.append(damage_as_float)
        elif x[-1] == "M":
            clean_num = x.strip("M")
            damage_as_float = (float(clean_num) * conversions["M"])
            updated_damages.append(damage_as_float)
    return updated_damages

#testing damage update function
#print(update_damages(damages))

#New variable for damages list
updated_damages = update_damages(damages)

# write your construct hurricane dictionary function here:

def hurricane_data_sets(names, months, years, max_winds, areas, damages, deaths):
    hurricanes = {}
    for hurricane in range(len(names)):
        hurricanes[names[hurricane]] = {"Name": names[hurricane], "Month": months[hurricane], "Year": years[hurricane], "Max Sustained Wind": max_sustained_winds[hurricane], "Areas Affected": areas_affected[hurricane], "Damage": updated_damages[hurricane], "Deaths": deaths[hurricane]}
    return hurricanes                  

hurricane_data = hurricane_data_sets(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)

#------Testing hurricane data dictionary creator function-----
#print(hurricane_data)
#print(hurricane_data["Dean"])



# write your construct hurricane by year dictionary function here:

def hurricanes_by_year(hurricanes):
    years = {}
    for each in hurricanes:
        current_cane = hurricanes[each]
        current_year = current_cane["Year"]
        if current_year not in years:
            years[current_year] = hurricanes[each]
        elif current_year in years:
            years[current_year].update(hurricanes[each])
    return years

#Testing the hurricanes by year function
#print(hurricanes_by_year(hurricane_data))



# write your count affected areas function here:



def areas_by_affected(hurricanes):
    areas_damaged = {}
    for hurricane in hurricanes:
        current_cane = hurricanes[hurricane]
        for area in current_cane["Areas Affected"]:
                if area not in areas_damaged:
                    areas_damaged[area] = 1
                if area in areas_damaged:
                    areas_damaged[area] += 1
    return areas_damaged

        
areas_hit = areas_by_affected(hurricane_data)


#testing out areas affected function below
#print(areas_hit)

# write your find most affected area function here:

def most_affected(areas_hit):
    worst_place_hits = 0
    for each in areas_hit:
        if areas_hit[each] > worst_place_hits:
            the_worst_place = each
            worst_place_hits = areas_hit[each]
    the_worst = (the_worst_place, worst_place_hits)
    return the_worst


hit_most = most_affected(areas_hit)

#testing most affected
#print(hit_most)



# write your greatest number of deaths function here:

def most_deaths(hurricane_data):
    body_count = 0
    big_killer_cane = ""
    for hurricane in hurricane_data:
        current_cane = hurricane_data[hurricane]
        if current_cane["Deaths"] > body_count:
            body_count = current_cane["Deaths"]
            big_killer_cane = current_cane["Name"]
    high_score = (big_killer_cane, body_count)
    return high_score
        



max_mortallity_cane = most_deaths(hurricane_data)

#Testing out most deaths function
#print(max_mortallity_cane)
# write your catgeorize by mortality function here:

def mortality_rate(hurricane_data):
    mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000, 5: 1000000}
    mortality_rating = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for i in hurricane_data:
        current_cane = hurricane_data[i]
        for x in mortality_scale:
            if current_cane["Deaths"] <= mortality_scale[x] and current_cane["Deaths"] > mortality_scale[x -1]:
                mortality_rating[x].append(current_cane)
    return mortality_rating
    

scaled_mortality = mortality_rate(hurricane_data)

#Testing mortality rate function
#print(scaled_mortality[3])



# write your greatest damage function here:

def most_damage_done(hurricane_data):
    damage_done = 0
    big_smashing_cane = ""
    for hurricane in hurricane_data:
        current_cane = hurricane_data[hurricane]
        if type(current_cane["Damage"]) == str:
            continue
        elif current_cane["Damage"] > damage_done and type(current_cane["Damage"]) == float:
            damage_done = current_cane["Damage"]
            big_smashing_cane = current_cane["Name"]
    highest_damage = (big_smashing_cane, damage_done)
    return highest_damage


#Testing most damage function
#print(most_damage_done(hurricane_data))

# write your catgeorize by damage function here:

def damaged_rating(hurricane_data):
    damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000, 5: 1000000000000000000000}
    damage_rating = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for i in hurricane_data:
        current_cane = hurricane_data[i]
        for x in damage_scale:
            if type(current_cane["Damage"]) == str:
                damage_rating[0].append(current_cane)
            elif current_cane["Damage"] <= damage_scale[x] and current_cane["Damage"] > damage_scale[x -1]:
                damage_rating[x].append(current_cane)
    return damage_rating

damages_rated = damaged_rating(hurricane_data)
print(damages_rated[5])