from treasure_island import cross_road_move, river_move, which_door
def main() -> None:
    print("Welcome to the Treasure Hunt. \n Your mission should you choose to accept is to find the treasure!")
    is_alive = True
    while is_alive:
        is_alive = cross_road_move(input("You come to a cross road. which direction do you take 'left' or 'right' "))
        if is_alive:
            is_alive = river_move(input("You come across a river. Do you 'wait' or 'swim' ? "))
            if is_alive:
                door = which_door(input("You've made it this far. There are three doors which do you choose among 'red', 'yellow, 'blue'? "))
                print(door)
                break
            else:
                print("You were attacked by a shark. Game Over!")
        else:
            print("You were attacked by pirates and died. Game Over!")


if __name__ == "__main__":
    main()