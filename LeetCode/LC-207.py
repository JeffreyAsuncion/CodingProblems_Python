"""
207. Course Schedule
Medium

5639

233

Add to List

Share
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 105
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""

## Approach with Andrew Candela
"""
Look up preReqs with Dictionary:
{
    10: [5, 6, 2],
    5: [1, 3],
    3: [1],
}

Look at each value in the dictionary:
    for each course in the prereqs:
        look up the prereqs of that numCourses 
            if there are no prereqs then we can move on
            otherwise recurs into prereqs
                need some way to keep track of courses we've visited
                also keep track of the statues of courses once we figure them out (MEMOIZATION)
"""

from typing import List, Dict, Set
from collections import defaultdict

def building_prereqs(prerequisites: List[List[int]]) -> Dict[int, List[int]]:
    # prereqs -> [[1, 2],[2, 3]]
    prereq_dict = defaultdict(list)
    for req_pair in prerequisites:
        course_num, prereq_course_num = req_pair[0], req_pair[1]
        prereq_dict[course_num].append(prereq_course_num)
        return prereq_dict


class Solution:

    def can_take_course(self, course_num: int) -> bool:
        # base case
        if self.course_status[course_num] is True:
            return True
        # base case
        if self.course_status[course_num] is False or course_num in self.visited_courses:
            return False
        
        # update visited courses
        self.visited_courses.add(course_num)

        for course_prereq in self.prereq_dict[course_num]:
            if self.can_take_course(course_prereq) is False:
                self.course_status[course_num] = False
                return False
            self.course_status[course_num] = True
            return True


    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # first build out the dictionary of prereqs
        self.prereq_dict = building_prereqs(prerequisites)
        self.course_status = {i:None for i in range(numCourses)}    # this is our MEMO
        self.visited_courses = Set[int] = set([])
        # then step through it to see if I can take all the classes in the prereqs dict 
        for prereq_list in self.prereq_dict.values():
            for course_num in prereq_list:
                if can_take_course(course_num) is False:
                    return False

        return True

# Test building_prereqs
# print(building_prereqs([[1, 2],[2, 3]]))






numCourses = 2
prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.



numCourses = 2
prerequisites = [[1,0],[0,1]]
# Output: false