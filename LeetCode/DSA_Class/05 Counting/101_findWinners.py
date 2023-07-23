"""
 Find Players With Zero or One Losses

Solution
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.
 

Example 1:

Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
Example 2:

Input: matches = [[2,3],[1,3],[5,4],[6,4]]
Output: [[1,2,5,6],[]]
Explanation:
Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, answer[0] = [1,2,5,6] and answer[1] = [].
"""

# class Solution:
#     def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
def findWinners(matches):
    winner_dict = {}
    loser_dict = {}
    winner_list = []
    loser_list = []

    for match in matches:
        winner, loser = match[0], match[1]
        if winner in winner_dict:
            winner_dict[winner] += 1
        else:
            winner_dict[winner] = 1
        if loser in loser_dict:
            loser_dict[loser] += 1
        else:
            loser_dict[loser] = 1

    for key, value in winner_dict.items():
        if key not in loser_dict.keys():
            winner_list.append(key)

    
    for key, value in loser_dict.items():
        if value == 1:
            loser_list.append(key)           

    return ([sorted(winner_list), sorted(loser_list)])



matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output = [[1,2,10],[4,5,7,8]]
print(findWinners(matches))
# [winner, loser]
# Explanation:
# Players 1, 2, and 10 have not lost any matches.
# Players 4, 5, 7, and 8 each have lost one match.
# Players 3, 6, and 9 each have lost two matches.
# Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
matches = [[2,3],[1,3],[5,4],[6,4]]
# Output: [[1,2,5,6],[]]
print(findWinners(matches))