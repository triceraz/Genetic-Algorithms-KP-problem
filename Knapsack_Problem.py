import random

items = """
1	15	40	0.5
2	23	65	0.8
3	7	35	0.3
4	12	50	0.6
5	30	90	1.2
6	45	150	1.5
7	20	75	0.9
8	55	200	2.0
9	10	55	0.4
10	50	180	1.8
11	33	120	1.3
12	18	85	0.7
13	25	95	1.0
14	60	220	2.5
15	40	160	1.6
16	35	140	1.4
17	28	110	1.1
18	70	250	3.0
19	80	290	3.5
20	22	90	0.85
21	17	75	0.65
22	65	240	2.8
23	38	145	1.35
24	90	310	3.8
25	5	30	0.2
26	14	55	0.55
27	48	175	1.7
28	85	280	3.6
29	32	125	1.25
30	21	88	0.75
31	77	270	3.2
32	8	40	0.35
33	42	155	1.45
34	66	235	2.85
35	95	320	4.0
36	13	60	0.58
37	31	130	1.28
38	19	78	0.72
39	56	210	2.2
40	9	45	0.38
41	27	115	1.1
42	88	300	3.75
43	11	50	0.5
44	75	265	3.1
45	41	150	1.55
46	37	135	1.38
47	16	72	0.6
48	20	80	0.9
49	53	190	2.1
50	6	32	0.25
"""


#Uses list comprehension to create a list of each line, 
#for each line creates a new list inside that splits at the tab between, creating a 2d-list. Filters out empty lines.

items_list = [line.split("\t") for line in items.split("\n") if line != ""] 
        
#Creates n number of random solutions using a nested for loop

n = 500

random_solutions = []

for i in range(n):
    list = []
    for i in range(len(items_list)):
        list.append(random.randint(0,1))
    random_solutions.append(list)
    
#Take each solution and calculate the value, value = 0: if weight > 500kg or volume > 30m^2

def value_of_solution(solution):
    value = 0
    weight = 0
    volume = 0
    counter = 0
    print(solution)
    for num in solution:
        if num == 0:
            counter += 1
            continue
        elif num == 1:
            value += float(items_list[counter][2])
            weight += float(items_list[counter][1])
            volume += float(items_list[counter][3])
            counter += 1
            if weight > 1000 or volume > 40:
                value = 0
    print(value)
    print(weight)
    print(volume)
    
# Calculates the values of the random solutions                
for solution in random_solutions:
    value_of_solution(solution)
