import datetime


people = [
	{ "name": 'Joe', "birthDate": datetime.datetime(1986,10,24) },
	{ "name": 'Bob', "birthDate": datetime.datetime(1975,5,24) },
	{ "name": 'Erika', "birthDate": datetime.datetime(1989,6,12) },
	{ "name": 'Dylan', "birthDate": datetime.datetime(1999,12,14) },
	{ "name": 'Steve', "birthDate": datetime.datetime(2003,4,24) }
]


def calculateAge(birthDate):
    today = datetime.date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

name_list = list(map(lambda person: "Hello, my name is " + person["name"] + " and I am " + str(datetime.datetime.now().year - int(person['birthDate'.strftime('%Y')]) - ((datetime.datetime.now().month, datetime.datetime.now().day) < (int(person['birthDate'].strftime("%m")), int(person['birthDate'].strftime("%d"))))))
print(name_list)

