"""
A deliberately bad implementation of 
[Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
This code simulates the swarming behaviour of bird-like objects ("boids").
"""

from matplotlib import pyplot as plt
from matplotlib import animation

import random

# Randomly initialize boid positions and velocities to create a starting point
# This provides a starting state for the simulation.
boids_x=[random.uniform(-450,50.0) for x in range(50)]
boids_y=[random.uniform(300.0,600.0) for x in range(50)]
boid_x_velocities=[random.uniform(0,10.0) for x in range(50)]
boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(50)]
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

def update_boids(boids):
    """
    Update the positions and velocities of boids based on rules that simulate
    group dynamics. The goal is to mimic natural flocking behavior seen in birds.
    """
    xs,ys,xvs,yvs=boids  # Unpack boid data

    # Rule 1: Move towards the center of mass of neighbors
    # HOW: For each boid, compute a small adjustment to its velocity
    # based on the average position of all other boids.
    for i in range(len(xs)):
        for j in range(len(xs)): # Compare boid `i` with boid `j`
            # Add a fraction of the distance to the neighbor's position to the velocity
            # This slowly "pulls" boid `i` toward the center of all `j` boids
            xvs[i]=xvs[i]+(xs[j]-xs[i])*0.01/len(xs)
    for i in range(len(xs)):
        for j in range(len(xs)):
            yvs[i]=yvs[i]+(ys[j]-ys[i])*0.01/len(xs)
    
    # Rule 2: Avoid collisions with nearby boids
    # HOW: If two boids are close (distance < 10), adjust velocities
    # so they move apart.
    for i in range(len(xs)):
        for j in range(len(xs)):
            # Compute the squared distance between boids `i` and `j`
            if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 100: # Check if distance is smaller than threshold
                # Adjust the velocity of `i` to move it away from `j`
                xvs[i]=xvs[i]+(xs[i]-xs[j])
                yvs[i]=yvs[i]+(ys[i]-ys[j])
    
    # Rule 3: Align velocity with nearby boids
    # HOW: If a boid is within a certain range of another boid,
    # adjust its velocity slightly to match that of the nearby boids.
    for i in range(len(xs)):
        for j in range(len(xs)):
            # Compute the squared distance between boids `i` and `j`
            if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 10000:  # Check if within alignment range
                # Adjust velocity to be closer to `j`'s velocity
                xvs[i]=xvs[i]+(xvs[j]-xvs[i])*0.125/len(xs)z
                yvs[i]=yvs[i]+(yvs[j]-yvs[i])*0.125/len(xs)

    # Rule 4: Move boids according to their velocities
    # HOW: Simply add the velocity components to the position
    # components, effectively "moving" the boid.
    for i in range(len(xs)):
        xs[i]=xs[i]+xvs[i] # Update X position based on X velocity
        ys[i]=ys[i]+yvs[i] # Update Y position based on Y velocity
