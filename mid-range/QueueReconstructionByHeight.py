class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        rec = []
        for p in people:
            rec.insert(p[1], p)
        return rec
