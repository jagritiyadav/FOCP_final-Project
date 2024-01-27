# Import the sys module for handling command line arguments
import sys

# Function to read the log file and return a list of cat activities
def read_log_file(file_path):
    """
    Read the log file and return a list of tuples containing cat activities.
    Each tuple is of the form (cat_type, entry_time, exit_time).
    """
    activities = []

    try:
        # Open the log file for reading
        with open(file_path, 'r') as file:
            # Iterate through each line in the file
            for line in file:
                # Check if the line is the end of the log
                if line.strip() == 'END':
                    break
                # Split the line into cat_type, entry_time, and exit_time
                cat_type, entry_time, exit_time = line.strip().split(',')
                # Convert entry_time and exit_time to integers and add to the list
                activities.append((cat_type, int(entry_time), int(exit_time)))
    except FileNotFoundError:
        # Handle the case where the file is not found
        print(f'Cannot open "{file_path}"!')
        sys.exit(1)

    return activities

# Function to analyze cat shelter activities and print the required output
def analyze_cat_shelter(activities):
    """
    Analyze the cat shelter activities and print the required output.
    """
    correct_cat_visits = 0
    intruding_cats_doused = 0
    total_time_in_house = 0
    visit_lengths = []

    # Iterate through each cat activity
    for cat_type, entry_time, exit_time in activities:
        # Check if it's our cat
        if cat_type == 'OURS':
            correct_cat_visits += 1
            total_time_in_house += exit_time - entry_time
            visit_lengths.append(exit_time - entry_time)
        # Check if it's an intruding cat
        elif cat_type == 'THEIRS':
            intruding_cats_doused += 1

    # Calculate average, longest, and shortest visit lengths
    if correct_cat_visits == 0:
        avg_visit_length = longest_visit = shortest_visit = 0
    else:
        avg_visit_length = sum(visit_lengths) // correct_cat_visits
        longest_visit = max(visit_lengths)
        shortest_visit = min(visit_lengths)

    # Print the analysis results
    print("\nLog File Analysis\n==================\n")
    print(f'Cat Visits: {correct_cat_visits}')
    print(f'Other Cats: {intruding_cats_doused}\n')
    print(f'Total Time in House: {total_time_in_house // 60} Hours, {total_time_in_house % 60} Minutes\n')
    print(f'Average Visit Length: {avg_visit_length} Minutes')
    print(f'Longest Visit:        {longest_visit} Minutes')
    print(f'Shortest Visit:       {shortest_visit} Minutes')

# Check if the script is being run directly
if __name__ == "__main__":
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 2:
        print('Missing command line argument!')
        sys.exit(1)

    # Get the log file path from the command line arguments
    log_file_path = sys.argv[1]
    # Read the log file and get the list of cat activities
    cat_activities = read_log_file(log_file_path)
    # Analyze the cat shelter activities and print the results
    analyze_cat_shelter(cat_activities)
