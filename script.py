# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille',
         'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September',
          'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977,
         1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160,
                       175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], [
    'Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M',
           'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11,
          2068, 269, 318, 107, 65, 19325, 51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

# write your update damages function here:


def update_damages(old_list):
    updated_damages = []
    conversion = {'M': 1000000,
                  'B': 1000000000}
    for i in old_list:
        if i == 'Damages not recorded':
            updated_damages.append(i)
        elif i[-1] == 'M':
            updated_damages.append(float(i.strip('M'))*conversion['M'])
        elif i[-1] == 'B':
            updated_damages.append(float(i.strip('B'))*conversion['B'])
    return updated_damages


updated_damages = update_damages(damages)


# write your construct hurricane dictionary function here:
def create_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
    hurricanes = {}
    num_hurricanes = len(names)

    for i in range(num_hurricanes):
        hurricanes[names[i]] = {'Name': names[i],
                                'Month': months[i],
                                'Year': years[i],
                                'Max Sustained Wind': max_sustained_winds[i],
                                'Areas Affected': areas_affected[i],
                                'Damage': updated_damages[i],
                                'Deaths': deaths[i]}
    return hurricanes


hurricanes = create_hurricane_dict(
    names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)


# write your construct hurricane by year dictionary function here:


def dict_by_year(hurricanes):
    hur_by_year = {}
    for i in hurricanes:
        current_year = hurricanes[i]['Year']
        current_cane = hurricanes[i]
        if current_year not in hur_by_year:
            hur_by_year[current_year] = [current_cane]
        else:
            hur_by_year[current_year].append(current_cane)
    return hur_by_year


hur_by_year = dict_by_year(hurricanes)


# write your count affected areas function here:

def affected_areas(hurricanes):
    aff_areas = {}
    for i in hurricanes:
        aa = hurricanes[i]['Areas Affected']
        for a in aa:
            if a not in aff_areas:
                aff_areas[a] = 1
            else:
                aff_areas[a] += 1
    return aff_areas


aff_areas = affected_areas(hurricanes)


# write your find most affected area function here:

def most_affected(aff_areas):
    max_area = 'Central Coast'
    max_count = 0
    for k, v in aff_areas.items():
        if max_count < v:
            max_area = k
            max_count = v
    return {max_area: max_count}


most_aa = most_affected(aff_areas)


# write your greatest number of deaths function here:

def max_deaths(hurricanes):
    hur_name = 'Cuba'
    death_num = 0
    for k, v in hurricanes.items():
        if death_num < v['Deaths']:
            hur_name = k
            death_num = v['Deaths']
    return {hur_name: death_num}


most_deaths = max_deaths(hurricanes)

# write your catgeorize by mortality function here:


def mortality_scales(hurricanes):
    hurs_by_mortailty_scale = {0: [], 1: [], 2: [], 3: [], 4: []}
    for i in hurricanes.values():
        if i['Deaths'] >= 0 and i['Deaths'] <= 100:
            hurs_by_mortailty_scale[0].append(i)
        elif i['Deaths'] > 100 and i['Deaths'] <= 500:
            hurs_by_mortailty_scale[1].append(i)
        elif i['Deaths'] > 500 and i['Deaths'] <= 1000:
            hurs_by_mortailty_scale[2].append(i)
        elif i['Deaths'] > 1000 and i['Deaths'] <= 10000:
            hurs_by_mortailty_scale[3].append(i)
        else:
            hurs_by_mortailty_scale[4].append(i)
    return hurs_by_mortailty_scale


hurs_by_mortality_scale = mortality_scales(hurricanes)


# write your greatest damage function here:

def most_damaged(hurricanes):
    most_damaged_area = 'Cuba'
    most_damaged_cost = 0
    for k, v in hurricanes.items():
        if v['Damage'] == 'Damages not recorded':
            continue
        else:
            if most_damaged_cost < v['Damage']:
                most_damaged_area = k
                most_damaged_cost = v['Damage']
    return {most_damaged_area: most_damaged_cost}


most_damage_hur = most_damaged(hurricanes)


# write your catgeorize by damage function here:

def damage_scales(hurricanes):
    hurs_by_damage_scale = {0: [], 1: [], 2: [], 3: [], 4: []}
    for i in hurricanes.values():
        if i['Damage'] == 'Damages not recorded':
            continue
        else:
            if i['Damage'] >= 0 and i['Damage'] <= 100000000:
                hurs_by_damage_scale[0].append(i)
            elif i['Damage'] > 100000000 and i['Damage'] <= 1000000000:
                hurs_by_damage_scale[1].append(i)
            elif i['Damage'] > 1000000000 and i['Damage'] <= 10000000000:
                hurs_by_damage_scale[2].append(i)
            elif i['Damage'] > 10000000000 and i['Damage'] <= 50000000000:
                hurs_by_damage_scale[3].append(i)
            else:
                hurs_by_damage_scale[4].append(i)
    return hurs_by_damage_scale


hurs_by_damage_scale = damage_scales(hurricanes)
