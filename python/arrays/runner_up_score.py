# HackerRank Challenge: Find the Runner-Up Score
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# Input: 
#   5
#   2 3 6 6 5
# Output:
#   5






if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    max_score = max(arr)
    new_arr = [x for x in arr if x != max_score]
    print(max(new_arr))
