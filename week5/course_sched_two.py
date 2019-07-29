class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        self.course_dic = {}
        self.res = [0]*numCourses
        self.idx = numCourses - 1
        for pre in prerequisites:
            a, b = pre[0], pre[1]
            if b not in self.course_dic:
                self.course_dic[b] = []
            self.course_dic[b].append(a)

        self.visited = [False] * numCourses
        self.visiting = [False] * numCourses
        for i in range(numCourses):
            if not self.visited[i] and self.find_helper(i):
                return []

        return self.res

    def find_helper(self, course):
        self.visiting[course] = True
        neighb = []
        if course in self.course_dic:
            neighb = self.course_dic[course]
        for n in neighb:
            if self.visiting[n]:
                return True
            if not self.visited[n] and self.find_helper(n):
                return True

        self.visited[course] = True
        self.visiting[course] = False
        self.res[self.idx] = course
        self.idx -= 1
        return False