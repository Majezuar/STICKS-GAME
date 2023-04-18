# THIS CODE WAS PROGRAMMED BY MANUEL ZUÑIGA
import random

actual_size = random.randint(5, 10)
print("\nINITIAL NUMBER OF STICKS:", actual_size)

def turn(actual_size):

    while True:
        selection = random.randint(1, 3)
        validate_answer = validate_option(selection, actual_size)
        if validate_answer:
            break

    actual_size -= selection
    print ("\tThere were taken", selection ,"and still",actual_size, "sticks left.\n")
    return actual_size
 
def validate_option(selection, actual_size):

    if selection <= actual_size:
        return True
    else:
        return False

def main_game():
    end_game = actual_size
    
    while True:
        print("\ \ \ Mano's Turn:")
        end_game = turn(end_game)
        
        if end_game == 0:
            print("\t¡¡¡MANO WINS!!!\n")
            break
        
        print("/ / / Tras's Turn:")
        end_game = turn(end_game)
        
        if end_game == 0:
            print("\t¡¡¡ TRAS WINS !!!\n")
            break
        
main_game()

# THIS CODE WAS PROGRAMMED BY MANUEL ZUÑIGA