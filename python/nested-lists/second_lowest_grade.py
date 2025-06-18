"""
Problem: Second Lowest Grade

Task:
Given names and grades of students, print the name(s) of students who have the second lowest grade.
If multiple students have the same second lowest grade, print their names in alphabetical order.

Input:
- First line: An integer n (number of students)
- Next 2 * n lines: Each student’s name followed by their grade

Output:
- Print the names of students with the second lowest grade
- One name per line, sorted alphabetically

Example Input:
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Example Output:
Berry
Harry
"""


if __name__ == '__main__':
    students = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
        
    grades = (score for name,score in students)
    
    unique_grades = sorted(set(grades))
    second_lowest = unique_grades[1]
    
    result = [name for name, score in students if score == second_lowest]
    
    for name in sorted(result):
        print(name)
        
        
        
