#Write a program that lets the user to enter a course number, then it should display the course's number, instructor, and meeting time.
# Define dictionaries for room numbers, instructors, and meeting times
rooms = {
    "CS101": "3004",
    "CS102": "4501",
    "CS103": "6755",
    "NT110": "1244",
    "CM241": "1411"
}

instructors = {
    "CS101": "Haynes",
    "CS102": "Alvarado",
    "CS103": "Rich",
    "NT110": "Burke",
    "CM241": "Lee"
}

meeting_times = {
    "CS101": "8:00 A.M",
    "CS102": "9:00 A.M",
    "CS103": "10:00 A.M",
    "NT110": "11:00 A.M",
    "CM241": "1:00 P.M"
}

# user to enter a course number
course_number = input("Enter a course number (e.g., CS101, CS102, etc.): ").strip()


if course_number in rooms:
    # Retrieve the course's room number, instructor, and meeting time
    room = rooms[course_number]
    instructor = instructors[course_number]
    meeting_time = meeting_times[course_number]
    
    # Display the information
    print(f"Course: {course_number}")
    print(f"Room Number: {room}")
    print(f"Instructor: {instructor}")
    print(f"Meeting Time: {meeting_time}")
else:
    print("Invalid course number. Please enter a valid course number.")



#Write a program that creates a quiz that displays the state and prompts the user to enter state's capital.
#On top of that the quiz should keep score and display the incorrect and correct answers at the end.
import random

# Define the number of states to quiz
NUM_STATES = 5

# Function to return a dictionary with states and their capitals
def state_cap_dictionary():
    return {
        'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
        'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
        'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
        'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
        'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
        'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'St. Paul', 'Mississippi': 'Jackson',
        'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
        'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
        'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
        'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
        'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
        'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
        'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
    }

def main():
    # Initialize the state_caps dictionary
    state_caps = state_cap_dictionary()
    
    # Initial variables to keep count of the number of correct and incorrect answers
    correct = 0
    incorrect = 0

    # Shuffle the dictionary keys (states) to randomize the order
    states_list = list(state_caps.keys())
    random.shuffle(states_list)

    # Quiz the user for a number of states (NUM_STATES)
    for count in range(NUM_STATES):
        # Get the state by its random index
        state = states_list[count]
        capital = state_caps[state]
        
        # Quiz the user
        print(f'What is the capital of {state}?', end=' ')
        response = input().strip()

        # Check if the user's response is correct
        if response.lower() == capital.lower():
            correct += 1
            print('Correct!')
        else:
            incorrect += 1
            print(f'Incorrect. The correct answer is {capital}.')

    # Display the results
    print('\nQuiz finished!')
    print(f'Correct responses: {correct}')
    print(f'Incorrect responses: {incorrect}')

# Run the program
if __name__ == "__main__":
    main()
