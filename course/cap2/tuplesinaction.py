# Tuples in action

# Tuples as records

lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokio', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE34567'), ('ESP', 'XDA205856')]

# Retrieve tuple information
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

# Tuple unpacking
for country, _ in traveler_ids:
    print(country)

# Parallel assignment
latitude, longitude = lax_coordinates # tuple unpacking
print(latitude)
print(longitude)

# Tuple Unpacking prefix an argument

divmod(20, 8)
t = (20, 8)
divmod(*t)
print(divmod(*t))

quotient, remainder = divmod(*t)
print(quotient, remainder)

# Grab excess items

a, b, *rest = range(5)


metro_areas = [
    ('Tokio', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -77.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4F} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))

# Named tuples
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])