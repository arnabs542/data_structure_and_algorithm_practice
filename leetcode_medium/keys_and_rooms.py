'''
There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may
have some keys to access the next room.
Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where
N = rooms.length.  A key rooms[i][j] = v opens the room with number v.
Initially, all the rooms start locked (except for room 0).
You can walk back and forth between rooms freely.
Return true if and only if you can enter every room.

Example 1:
Input: [[1],[2],[3],[]]
Output: true
Explanation:
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.

Example 2:
Input: [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can't enter the room with number 2.

Note:
1 <= rooms.length <= 1000
0 <= rooms[i].length <= 1000
The number of keys in all rooms combined is at most 3000.
'''


def can_visit_all_rooms(rooms):
    visited = {}
    for room in range(len(rooms)):
        visited[room] = 0

    visited[0] = 1
    keyset = set()
    for key in rooms[0]:
        keyset.add(key)

    while len(keyset) > 0:
        for key in keyset:
            keys_to_add = []
            keys_to_del = []
            if visited[key] == 0:
                visited[key] = 1
                for k in rooms[key]:
                    keys_to_add.append(k)
                keys_to_del.append(key)
            else:
                keys_to_del.append(key)
        for key in keys_to_add:
            keyset.add(key)
        for key in keys_to_del:
            keyset.remove(key)

    for room in range(len(rooms)):
        if visited[room] != 1:
            return False
    return True

print(can_visit_all_rooms([[1],[2],[3],[]]))
print(can_visit_all_rooms([[1,3],[3,0,1],[2],[0]]))
