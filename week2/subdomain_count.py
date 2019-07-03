from collections import Counter

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        
        Successful
        
        Faster than 95% submissions
        Less memory than 77% submissions
        """
        count = Counter()
        for domain in cpdomains:
            domain_split = domain.split(" ")
            visited = int(domain_split[0])
            count[domain_split[1]] += visited
            
            num_splits = len(domain_split[1].split("."))
            
            dsplit = domain_split[1].split(".", 1) # only split at first period
            for i in range(num_splits -1):
                count[dsplit[1]] += visited
                dsplit = dsplit[1].split(".", 1)
        
        result = []
        for i in count:
            result.append(str(count[i]) + " " + i)
        return result