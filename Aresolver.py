from termcolor import colored, cprint # This lib is so I can color the output and everything is easier to understand in the example
# Created by Diego Magdaleno, a young, introvert and dumb computer science student.
# Dedicated to all those people that helped me being a better person.
# This is a public algorithm, take is a gift. 
# Thank you <3.
# Resolves dependencies


class Node: # A node is any "Vector in a graph"
   def __init__(self, name):
      self.name = name
      # Edges are the lines or relations, that are going to be in array
      self.edges = []
    
    # Connects the nodes, by adding edges
   def addEdge(self, node):
      self.edges.append(node)

# Define all nodes, again like the vectors of the graph that we are going add
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')

# Lets make this a little more graphic, here is how it would look into a graphic
# We use the function we define previously, the addEdge, this means its going to add a "line"
# this is going to "look" something like this a <--------> b. This of course is for human understanding
# For a computer it looks like a bunch of 0s and 1s.

a.addEdge(b)    # a depends on b
a.addEdge(d)    # a depends on d
b.addEdge(c)    # b depends on c
b.addEdge(e)    # b depends on e
c.addEdge(d)    # c depends on d
c.addEdge(e)    # c depends on e

# Now we have our basic structure, lets start actually resolving the dependencies.

# Lets define a new function, this one is the "main" one since the plan is that this resolves deps.
# So we need an starting point, to make things easier for ourselves, lets start with "a".
# We are going to need to do some crazy recursive function here since for every nonde, we need to go 
# to the other connected node 

def dep_resolve(node):
   print (node.name)
   for edge in node.edges:
      dep_resolve(edge)

# NOTE: We arent doing them in order yet, be careful with that!
print("Check my output!")
dep_resolve(a) # Call the function and give it the node of "a"

# Important check the output here 

# Now its important to figure out the order Why? You may ask, well look at out block of edges again, as you can see
# the node "a" depends on node "b" and node "d". So if cant be installed yet, however, neither "d" and "e" depend on other 
# nodes, so we can assume those can be installed

# By the logic we previously used, we can go to one conclussion: Software can be installed, one all deps are complete or it doesnt depend on anything 

# I am going to make a new function, with a new name, just so you can see the different prints 

# Now its time implement the algorithm here, this ones resolves the deps in order using a correct technique, lets break it out, we want to start 
# installaing a package once all its dependencies have been resolved, once we reach that point we can append the current list (array) of resolved 
# dependencies 

# The function now looks like this, this also means, as you can see if now takes two arguments

def dep_resolve_order(node, resolved): # We algo get a "resolved" here now 
   print (node.name)
   for edge in node.edges:
      dep_resolve_order(edge, resolved)
   resolved.append(node)

# This array, is now to fill the argument it takes, since it now takes the "resolved"

resolved = []


print("I am resolved in order now")
# Call the function again, but now with the resolved argument 
dep_resolve_order(a, resolved)
print("The green ones are the contents of the resolved list")
for node in resolved: # for each node in the resolved array that stores all 
       cprint (node.name, 'green'), 

# Check the output now 

# Now you can see there is a big elephant in the room, some nodes appared twice, but we don't want do that, Why reinstall and redonwload?
# There is a thing we need to do now, if it appears once, then it shouldn't appear a second time.

# So we come to a conclussion: When a package has already been resolved, we don’t need to visit it again.

# So we can just add logic to perform this, so basically what we do, is, if we already saw the package, then don't add it to the array again 

resolved = [] # Clean the array, ofc we dont need to clean it in a real life example, here i am doing this, beacuse I am going to fill it with new info
# with the other data 

def dep_resolve_unique(node, resolved):
   print (node.name)
   for edge in node.edges:
      if edge not in resolved: # If it isnt in resolved, run the function, if it is, then dont
         dep_resolve_unique(edge, resolved)
   resolved.append(node)

dep_resolve_unique(a, resolved)
print("The red contents, is an ordered, unique dependency list")
for node in resolved: # for each node in the resolved array that stores all 
       cprint (node.name, 'red'), 

# We are almost done, except we have a problem now: Circular dependencies 

# Suppose we add the following to our dependencies 
# d.addEdge(b)
# Sadly I cant give you an example of this, since python would refuse to interpret, but I can explain whats happening here

# As we see:
# Node ‘d’ now depends on ‘b’. But ‘b’ depends on ‘c’ and ‘c’ depends on ‘d’ and ‘d’ depends on ‘b’ and… We’ve now got a circular dependency which can never be solved

# In this case we can never determine if "b" or "d" should be installed, firts, because they both depend in each, other, this is just and endless circle. However, this isnt
# a problem we have on our algorithm is a problem of the depenedencies, we cant fix it, but we can detect problems in it and tell the user "Hey I cant handle this!"

# But now a question, when a circular dependency happens? This is easy:
# A circular dependency is occurring when we see a software package more than once, unless that software package has all its dependencies resolved.

# Since we already have figured out how to don't repeat packages that are already satisfied, is now time to just add a check for circular deps

resolved = [] # Clean the array

def dep_resolve_circ(node, resolved, seen): # Now we take 3 arguments!
   print (node.name)
   seen.append(node)
   for edge in node.edges:
      if edge not in resolved:
         if edge in seen:
            raise Exception('Circular reference detected: %s -> %s' % (node.name, edge.name))
         dep_resolve(edge, resolved, seen)
   resolved.append(node)

dep_resolve_circ(a, resolved, []) # Array for seen 
print("I detect circular deps.")
for node in resolved:
   cprint (node.name, 'yellow'),
