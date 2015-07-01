#!/usr/bin/env python3
#hw5.py
#
#Class: CSCI 490-B3
#Program: Route Optimization
#Author: RJ Catalano
#Z-number: z1716703
#Date Due: 03/25/2015
#Purposes: To incorporate 5 different algorithms to achieve an optimal route through 
#               two cities in France, including Breadth First Search, A*, Depth First Search, and Depth First Iterative Deepening
#Execution: ./hw5.py [start] [end]
import sys

class Node:

    def __init__(self, name, parent, f, g, h):
        self.name = name
        self.parent = parent
        self.f = f
        self.g = g
        self.h = h
        

    def nodesExpanded(self):
        print("Number of nodes expanded:", nodeCount)

    def attributes(self):
        return (self.name, self.f)
    def getParent(self):
        return self.parent
    def getName(self):
        return self.name

    def expand(self):
        print ("Expanding ", self.name, " f=", self.f, " g=", self.g, " h=", self.h, sep='')
         
def BFS (cityRoads, start, end, depth=18):
    openList    =[]
    closedList  =[]
    solution    =[]				#declare lists
    print ("BFS:")

    node = start				#define the starting node, add it to the closed list, begin node counter
    i = 0
    if depth < 18:
        closedList.append((start, i))
    else: 
        closedList.append(start)
    
    while cityRoads:				#begin nested loop
        print ("Expanding", node)
        
        newChildren = []       			#define children lists
        children    = []
        sortedList  = []

        if (node == end):	
            if depth < 18:		#if node is found, add it to closed list and break from loop
                closedList.append((end, i))
            else:
                closedList.append(end)
            break
       
        for key in cityRoads[node].keys():	#second loop, look through dict append keys into a list to be sorted
            key = key.upper()
            sortedList.append(key)
            
        sortedList.sort()
        
        for city in sortedList:                #third loop to append values into open list and the child lists
            if city not in openList and city not in closedList:
                if depth < 18:
                    openList.append((city,i+1))
                    newChildren.append((city,i+1))
                    children.append((city,i+1))
                else:
                    openList.append(city)
                    newChildren.append(city)                                        
                    children.append(city)
        
        print ("Children (", " ".join(children), ')')   #print results
        print ("New children (", " ".join(newChildren),')')
        print ("Open list is (", " ".join(openList), ')')
        print ("Closed List is (", " ".join(closedList), ')') 
        print ("")

        newCity = openList.pop(0)		#pop the next city to be searched from the front of the open list
        if depth < 18:
            node = newCity[0]
        else:
            node = newCity
   
        if not newChildren:
            newChildren.append("Nil")

        if newCity not in closedList and depth < 18:		#add the next city to the closed list and count up the number of nodes expanded
            closedList.append((newCity, i))
        else:    
            closedList.append(newCity)        
        i += 1

    solution.insert(0, end)
    while node is not start:			#working backwards, find the children of the last node, find the one indexed closest to the start, and repeat 
        minList = []
        for city in cityRoads[node].keys():
            city = city.upper()
            if city in closedList:
                index = closedList.index(city)
                minList.append(index)
        mIndex = min(minList)
        node = closedList[mIndex]
        solution.insert(0, closedList[mIndex])
    
    print ("Breadth-first-search solution:", solution) #print the solution and the nodes expanded
    print (i, "nodes expanded")       


def DFS (cityRoads, start, end, depth=18):
    openList    =[]
    closedList  =[]
    solution    =[]                             #declare lists
#    print ("DFS:")

    node = start                                #define the starting node, add it to the closed list, begin node counter
    i = 0
    level = 0
    if depth < 18:
        openList.append((start, level))
    else: 
        openList.append(start)

    while openList and len(openList) < 10:                            #begin nested loop
        newChildren = []                        #define children lists
        children    = []
        sortedList  = []

        newCity = openList.pop(0)               #pop the next city to be searched from the front of the open list
        if depth < 18:
            node = newCity[0]
            level = newCity[1]
        else:
            node = newCity
        print ("Expanding", node)

        if (node == end):                       #if node is found, add it to closed list and break from loop
            if depth < 18:
                closedList.append((end, level))
            else:
                closedList.append(end)
            break

        if newCity not in closedList:           #add the next city to the closed list and count up the number of nodes expanded
            closedList.append(newCity)


        for key in cityRoads[node].keys():      #second loop, look through dict$
            key = key.upper()
            sortedList.append(key)
        
        sortedList.sort(reverse=True)
        
        for city in sortedList:                #third loop to append values int$

            depthReached = False
            if level == depth:
                print ("Depth has been reached")
                depthReached = True
                break
            if depth < 18:
                cities = [x[0] for x in openList]
                closed = [x[0] for x in closedList]
                if city not in cities and city not in closed:
                    openList.insert(0, (city, level+1))
                    newChildren.insert(0, (city, level+1))
                children.insert(0, (city, level+1))
            else:
                if city not in openList and city not in closedList:
                    openList.insert(0, city)
                    newChildren.insert(0, city)
                children.insert(0, city)
            
        if not newChildren:
            newChildren.insert(0,"Nil")
        if depth < 18:
            if not depthReached:
                print ("Children (", " ".join("(%s %s)" % tup for tup in children), ')')   #print results
                print ("New children (", " ".join("(%s %s)" % tup for tup in newChildren),')')
            if not openList:
                print ("Open list is NIL")
            else:
                print ("Open list is (", " ".join("(%s %s)" % tup for tup in openList), ')')
            print ("Closed List is (", " ".join("(%s %s)" % tup for tup in closedList), ')')
        else:
            print ("Children (", " ".join(children), ')')   #print results
            print ("New children (", " ".join(newChildren),')')
            print ("Open list is (", " ".join(openList), ')')
            print ("Closed List is (", " ".join(closedList), ')')
        print ("")

        i+=1
    if depth < 18:
        return i
    solution.insert(0, end)
    while node is not start:                    #working backwards, find the children of the last node, find the one indexed closest to the start, and repeat 
        minList = []
        for city in cityRoads[node].keys():
            city = city.upper()
            if city in closedList:
                index = closedList.index(city)
                minList.append(index)
        mIndex = min(minList)
        node = closedList[mIndex]
        solution.insert(0, closedList[mIndex])

    print ("Depth-first-search solution:", solution) #print the solution and the nodes expanded
    print (i, "nodes expanded")



def DFID (cityRoads, start, end, depth):
    i = 0
    nodes = 0
    while i <= depth:
        print("DFID Level ", i, ":", sep='')
        print("")
        levels = DFS (cityRoads, start, end, i)
        i += 1
        nodes += levels
    print (nodes, "total nodes expanded")
def A_Star(cityRoads, cityLongs, start, end, startingH):
#// A*
    openList = []
    closedList = [] #initialize the open, closed list, nodes, i and g
    nodes = []
    solution = []
    i = 0
    g = 0
    h = startingH

    nodes.append(Node(start, "none", g+h, g, h)) 
    openList.append((nodes[i].name, nodes[i].f))   #put the starting node on the open list (you can leave its f at zero)
    if (startingH == 0):
        print ("A* with H=0:")
    else:
        print ("A* with H=East-West Distance:")    
    while openList:       										#while the open list is not empty
        children = []
						             						#    find the node with the least f on the open list, call it "q"
        q = openList.pop(0)										#    pop q off the open list
        temp = [x for x, y in enumerate(nodes) if nodes[x].name == q[0]]				
        index = temp[0]
       
        nodes[index].expand()
	
        if nodes[index].name == end:            							#    	if successor is the goal, stop the search
            break							
													#    generate q's successors and set their parents to q
        for city in cityRoads[q[0]]:   									#    for each successor                  
             children.append(city.upper())
             if startingH == 0:
                 h = 0
             else:
                 h = 8*abs(int(cityLongs[city.capitalize()]) - int(cityLongs[end.capitalize()]))	#        successor.h = distance from goal to successor
            
             g = int(cityRoads[q[0]][city]) + nodes[index].g     					#        successor.g = q.g + distance between successor and q             
													#        successor.f = successor.g + successor.h
             f = g + h			
            
             cList = [i for i, v in enumerate(closedList) if v[0] == city.upper()]
             if cList:											#        if a node with the same position as successor is in the CLOSED list, skip
                 continue
             oList = [i for i, v in enumerate(openList) if v[0] == city.upper()]
             if oList:											#        if a node with the same position as successor is in the OPEN list which has lower f than successor, update the value, then skip
                 j = [y[0] for y in openList].index(city.upper())
                 value = openList[j]
                 if f < value[1]:
                     print ("***Revaluing open node", city, "from", value[1], "to", g+h)
                     del openList[j]
                     openList.insert(j, (city.upper(), g+h))     
                 continue 
             nodes.append(Node(city.upper(), nodes[index].name, f, g, h))				#        otherwise, add the node to the open list
             openList.append(nodes[-1].attributes())
        openList.sort(key=lambda x: (x[1], x[0]))
        closedList.append(q)										#    push q on the closed list

        print ("Children are (", " ".join(children), ")")
        print ("Open list is (", " ".join("(%s %s)" % tup for tup in openList), ")")       													#    end
        print ("Closed list is (", " ".join("(%s %s)" % tup for tup in closedList), ")")
        print ("")
													#end
    solution.append(nodes[index].getName())
    parent = nodes[index].getParent()
    length = nodes[index].f
    while nodes[index].getName() is not start:						
        temp = [x for x, y in enumerate(nodes) if nodes[x].name == parent]
        index = temp[0]
        solution.insert(0, nodes[index].getName())
        parent = nodes[index].getParent()

    print ("")
    if (startingH == 0):
        print("A-star-search solution with h=0: (", " ".join(solution), ")")
    else:
        print("A-star-search soution: (", " ".join(solution), ")")
    print ("Path-length:", length)
    print(len(nodes)-1, "nodes expanded")



fromCity = sys.argv[1].upper()
toCity = sys.argv[2].upper()

cityRoads = {}
cityLongs = {}

with open ("france-roads1.txt", "r") as f: #get france roads
    for line in f:
        li=line.strip()
        if not li.startswith("#"):
             if li.endswith(":"):
                 newCity = li.strip(':')
                 cityRoads[newCity] = {}
             else:
                 token = li.split()
                 if token:
                     newToCity = token[0]
                     distance = token[1]
                     cityRoads[newCity][newToCity] = distance 
                     
                     
with open ("france-long1.txt", "r") as f: #get france longitude
    for line in f:
        li=line.strip()
        if not li.startswith("#"):
             token = li.split()
             if token:
                 city = token[0]
                 longitude = token[1]
                 cityLongs[city] = longitude


print (len(cityRoads))
BFS(cityRoads, fromCity, toCity)

print ("")
print ("")

DFS(cityRoads, fromCity, toCity)

print ("")
print ("")

A_Star(cityRoads, cityLongs, fromCity, toCity, 0)

print ("")
print ("")
h = 8*abs(int(cityLongs[fromCity.capitalize()]) - int(cityLongs[toCity.capitalize()]))
A_Star(cityRoads, cityLongs, fromCity, toCity, h)

print ("")
print ("")

DFID(cityRoads, fromCity, toCity, 3)
