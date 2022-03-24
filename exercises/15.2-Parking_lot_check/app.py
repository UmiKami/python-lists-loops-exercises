parking_state = [
  [1,1,1], 
  [0,0,0], 
  [1,1,2]
]

#Your code go here:

def get_parking_lot():
  state = {}
  state['total_slots'] = sum(list(map(lambda arr: arr.count(2)+arr.count(1), parking_state)))
  state['available_slots'] = sum(list(map(lambda arr: arr.count(2), parking_state)))
  state['occupied_slots'] = sum(list(map(lambda arr: arr.count(1), parking_state)))

  return state

print(get_parking_lot())
