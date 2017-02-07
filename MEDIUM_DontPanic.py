# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: ignore (always zero)
# nb_elevators: number of elevators
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, \
    nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]

elevators = {}  # Keep track of elevators floors/positions

for i in range(nb_elevators):
    # elevator_floor: floor on which this elevator is found
    # elevator_pos: position of the elevator on its floor
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    elevators[elevator_floor] = elevator_pos

while True:
    # clone_floor: floor of the leading clone
    # clone_pos: position of the leading clone on its floor
    # direction: direction of the leading clone: LEFT or RIGHT
    clone_floor, clone_pos, direction = input().split()
    clone_floor = int(clone_floor)
    clone_pos = int(clone_pos)

    if clone_floor == exit_floor:
        target = exit_pos
    elif clone_floor in elevators:
        target = elevators[clone_floor]

    if direction == 'RIGHT' and clone_pos > target:
        print('BLOCK')
    elif direction == 'LEFT' and clone_pos < target:
        print('BLOCK')
    else:
        print('WAIT')
