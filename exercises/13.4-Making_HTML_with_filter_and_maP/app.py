all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def filter_colors(color):
	return color['sexy'] == True

def generate_li(prop):
	return "<li>" + prop['label'] + "</li>"
	
filtered_list = list(filter(lambda color: filter_colors(color), all_colors))
list_items = list(map(lambda prop: generate_li(prop), filtered_list))

print(list_items)