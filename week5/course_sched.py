class Solution(object):
    def __init__(self):
        self.course_dic = {}
        self.visited = []
        self.visiting = []
    
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.course_dic = {}
        for courses in prerequisites:
            prereq = courses[1]
            course = courses[0]
            if prereq not in self.course_dic:
                self.course_dic[prereq] = []
            self.course_dic[prereq].append(course) # a course may need multiple prereqs
        
        self.visited = [False] * numCourses
        self.visiting = [False] * numCourses
        
        for i in range(numCourses):
            if not self.visited[i] and self.course_finder(i):
                return False
        return True
        
    def course_finder(self, course): # does through dfs
        self.visiting[course] = True
        neighb = []
        if course in self.course_dic:
            neighb = self.course_dic[course]
        for n in neighb:
            if self.visiting[n]:
                return True
            if not self.visited[n] and self.course_finder(n):
                return True
        
        # finished visiting
        self.visiting[course] = False
        self.visited[course] = True  # seen course
        return False
        