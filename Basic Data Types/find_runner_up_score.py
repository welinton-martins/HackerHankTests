def find_runner_up_score():
    # Read the number of scores
    n = int(input().strip())
    # Read the scores as a list of integers
    scores = list(map(int, input().strip().split()))

    # Convert the list to a set to remove duplicates and back to a sorted list
    unique_scores = sorted(set(scores))

    # The runner-up score is the second last in the sorted unique scores
    runner_up_score = unique_scores[-2]
    
    # Print the runner-up score
    print(runner_up_score)

if __name__ == "__main__":
    find_runner_up_score()
