users = [
    {
        'id' : 1,
        'name' : "Jane Doe",
        'height' : 5.5,
        'gender' : "female",
        'money' : 100,
        'age' : 23,
        'email' : "jdoe@mail.com",
        'state' : 7 # this is a foreign_key that relates to the other list of states with its corresponding id number
    },
    {
        'id' : 2,
        'name' : "John Smith",
        'height' : 5.8,
        'gender' : "male",
        'money' : 10,
        'age' : 26,
        'email' : "jsmith@mail.com",
        'state' : 23
    },
    {
        'id' : 3,
        'name' : "Stacy",
        'height' : 5,
        'gender' : "female",
        'money' : 90,
        'age' : 26,
        'email' : "spiceGirl@mail.com",
        'state' : 1
    },
    {
        'id' : 4,
        'name' : "Jessica",
        'height' : 5.6,
        'gender' : "female",
        'money' : 120,
        'age' : 52,
        'email' : "spiceGirl@mail.com",
        'state' : 12
    },
    {
        'id' : 5,
        'name' : "Mikael",
        'height' : 6.1,
        'gender' : "male",
        'money' : 200,
        'age' : 37,
        'email' : "mikeymike@mail.com",
        'state' : 35
    },
    {
        'id' : 6,
        'name' : "Daniel",
        'height' : 5.9,
        'gender' : "male",
        'money' : 50,
        'age' : 19,
        'email' : "dandyboy@mail.com",
        'state' : 24
    },
    {
        'id' : 7,
        'name' : "Jennie",
        'height' : 5.3,
        'gender' : "female",
        'money' : 250,
        'age' : 26,
        'email' : "bpgem@mail.com",
        'state' : 14
    },
    {
        'id' : 8,
        'name' : "Lumi",
        'height' : 5.1,
        'gender' : "female",
        'money' : 75,
        'age' : 21,
        'email' : "yingflor@mail.com",
        'state' : 40
    },
    {
        'id' : 9,
        'name' : "Kenneth",
        'height' : 6.1,
        'gender' : "male",
        'money' : 35,
        'age' : 23,
        'email' : "kenken@mail.com",
        'state' : 45
    }
]

states = [
    {'name': 'Alabama', 'abbreviation': 'AL', 'id': 1},
    {'name': 'Alaska', 'abbreviation': 'AK', 'id': 2},
    {'name': 'Arizona', 'abbreviation': 'AZ', 'id': 3},
    {'name': 'Arkansas', 'abbreviation': 'AR', 'id': 4},
    {'name': 'California', 'abbreviation': 'CA', 'id': 5},
    {'name': 'Colorado', 'abbreviation': 'CO', 'id': 6},
    {'name': 'Connecticut', 'abbreviation': 'CT', 'id': 7},
    {'name': 'Delaware', 'abbreviation': 'DE', 'id': 8},
    {'name': 'Florida', 'abbreviation': 'FL', 'id': 9},
    {'name': 'Georgia', 'abbreviation': 'GA', 'id': 10},
    {'name': 'Hawaii', 'abbreviation': 'HI', 'id': 11},
    {'name': 'Idaho', 'abbreviation': 'ID', 'id': 12},
    {'name': 'Illinois', 'abbreviation': 'IL', 'id': 13},
    {'name': 'Indiana', 'abbreviation': 'IN', 'id': 14},
    {'name': 'Iowa', 'abbreviation': 'IA', 'id': 15},
    {'name': 'Kansas', 'abbreviation': 'KS', 'id': 16},
    {'name': 'Kentucky', 'abbreviation': 'KY', 'id': 17},
    {'name': 'Louisiana', 'abbreviation': 'LA', 'id': 18},
    {'name': 'Maine', 'abbreviation': 'ME', 'id': 19},
    {'name': 'Maryland', 'abbreviation': 'MD', 'id': 20},
    {'name': 'Massachussetts', 'abbreviation': 'MA', 'id': 21},
    {'name': 'Michigan', 'abbreviation': 'MI', 'id': 22},
    {'name': 'Minnesota', 'abbreviation': 'MN', 'id': 23},
    {'name': 'Mississippi', 'abbreviation': 'MS', 'id': 24},
    {'name': 'Missouri', 'abbreviation': 'MO', 'id': 25},
    {'name': 'Montana', 'abbreviation': 'MT', 'id': 26},
    {'name': 'Nebraska', 'abbreviation': 'NE', 'id': 27},
    {'name': 'Nevada', 'abbreviation': 'NV', 'id': 28},
    {'name': 'New Hanpshire', 'abbreviation': 'NH', 'id': 29},
    {'name': 'New Jersey', 'abbreviation': 'NJ', 'id': 30},
    {'name': 'New Mexico', 'abbreviation': 'NM', 'id': 31},
    {'name': 'New York', 'abbreviation': 'NY', 'id': 32},
    {'name': 'North Carolina', 'abbreviation': 'NC', 'id': 33},
    {'name': 'North Dakota', 'abbreviation': 'ND', 'id': 34},
    {'name': 'Ohio', 'abbreviation': 'OH', 'id': 35},
    {'name': 'Oklahoma', 'abbreviation': 'OK', 'id': 36},
    {'name': 'Oregon', 'abbreviation': 'OR', 'id': 37},
    {'name': 'Pennsylvania', 'abbreviation': 'PA', 'id': 38},
    {'name': 'Rhode Island', 'abbreviation': 'RI', 'id': 39},
    {'name': 'South Carolina', 'abbreviation': 'SC', 'id': 40},
    {'name': 'South Dakota', 'abbreviation': 'SD', 'id': 41},
    {'name': 'Tennessee', 'abbreviation': 'TN', 'id': 42},
    {'name': 'Texas', 'abbreviation': 'TX', 'id': 43},
    {'name': 'Utah', 'abbreviation': 'UT', 'id': 44},
    {'name': 'Vermont', 'abbreviation': 'VT', 'id': 45},
    {'name': 'Virginia', 'abbreviation': 'VA', 'id': 46},
    {'name': 'Washington', 'abbreviation': 'WA', 'id': 47},
    {'name': 'West Virginia', 'abbreviation': 'WV', 'id': 48},
    {'name': 'Wisconsin', 'abbreviation': 'WI', 'id': 49},
    {'name': 'Wyoming', 'abbreviation': 'WY', 'id': 50}
]

pets = [
    {
        'id' : 123456789,
        'name' : "Meowsalot",
        'species' : "cat",
        'age' : 5,
        'user_id' : 1
    },
    {
        'id' : 987654321,
        'name' : "Barksalot",
        'species' : "dog",
        'age' : 3,
        'user_id' : 1
    },
    {
        'id' : 123123123,
        'name' : "Fluffy",
        'species' : "rabbit",
        'age' : 2,
        'user_id' : 6
    },
    {
        'id' : 456456456,
        'name' : "Purrsloud",
        'species' : "cat",
        'age' : 6,
        'user_id' : 4
    },
    {
        'id' : 789789789,
        'name' : "Paws",
        'species' : "dog",
        'age' : 6,
        'user_id' : 4 
    }
]