class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        year_pop = [0]*101
        for birth, death in logs:
            year_pop[birth - 1950] += 1
            year_pop[death - 1950] -= 1
        curr_pop = 0
        max_pop = 0
        ear_year = 1950
        for i in range(101):
            curr_pop += year_pop[i]
            if curr_pop > max_pop:
                max_pop = curr_pop
                ear_year = 1950 + i
        return ear_year    
        