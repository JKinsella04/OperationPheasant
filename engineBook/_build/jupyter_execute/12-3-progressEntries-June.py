# June Progress Entries
## 6/21/20
### Attendance: &#9744; Brody, &#9745; Derek, &#9744; Dylan, &#9744; Ian, &#9744; Jack
Starting to work on a new robot design with CAD, the biggest advantage of this design over our previous robots is that it can score and de-score at the same time.
We quickly ran into a problem with our current drive base as it is not designed to move the balls out of the goals and into the intakes. The main problem is the motors and a piece of c-channel that are blocking the balls from traveling in the robot. 
We fixed the problem with the motors blocking the balls by moving the front motor to above the back wheel, this fixes some of the problems but we will have to redesign the drive base if we want to continue using this robot design because of the structural support c-channel in the back that is blocking the balls.

### Goals for new robot
less than a second to score 3 balls in an empty goal
less than 2 seconds to completely swap out a full goal
less than a second to take a ball from the bottom to the top.

### CAD of New Robot Design
<img src="././_images/6-June/6-21-20/fullRobot.png" alt="fullRobot.png" style="width: 200px;"/>
<img src="././_images/6-June/6-21-20/newDrive.png" alt="newDrive.png" style="width: 200px; height: 135px;"/>
<img src="././_images/6-June/6-21-20/newIntakePosition.png" alt="newIntakePosition.png" style="width: 200px;"/>
<img src="././_images/6-June/6-21-20/newRobotFront.png" alt="newRobotFront.png" style="width: 200px; height: 150px;"/>
<img src="././_images/6-June/6-21-20/sideOfNewDrive.png" alt="sideOfNewDrive.png" style="width: 200px; height: 150px;"/>

## 6/25/20
### Attendance: &#9744; Brody, &#9745; Derek, &#9744; Dylan, &#9744; Ian, &#9744; Jack
 Today the old CAD was redone and finished, with all the problems we were previously having we started over completely with a new drive base and intake system. 
The new drive base uses 3.25in omni wheels as they are closer to the ground so our intakes have more room above the wheels and will not interfere with each other. The wheels are geared 60:36 at 200rpm for an output rpm of 333rpm. This output rpm is slightly faster than our old drive base but the smaller wheels will give us more control at this speed.
The new intakes swing out at the start of a match to ~5.15in outside of the 18in restriction or ~6.9in from the front of the robot (measured from the start of the drive base) This will give us enough space to start lifting the balls up in our robot quicker than before allowing us to put the drive motors in a normal place unlike our previous designs.
Along with that the new intakes consist of 2 parts that are chained together, the first part can go fully into a goal to start descoring while the other moves the balls in to the rest of the robot, the chain that connects the two parts of the intake is laid in a way that it can go around the goal posts and will not get caught
The new indexer/ball tower system has been redesigned to fit in with the new front intakes, It starts sooner on the robot so the motors do not have to move to a different location and is also protected from the goal by pieces of c-channel. The main difference between the old and new systems is that on the back of the robot, we now have two extra rollers that allow us to get rid of balls that we do not want by spinning the intake in reverse. We have also added a vision sensor to the front of the robot with future plans to automate this function. 
Programing of the new robot
We have kept the inertial sensors and tracking wheels from the old drive base in the new robot so we can continue to develop those systems
We have added a vision sensor to hopefully automate the sorting of balls. Whenever we start scoring on a goal the vision sensor can detect the goal and switch to manual sorting mode.

### Completed CAD
<img src="././_images/6-June/6-25-20/frontOfSnail.png" alt="frontOfSnail.png" style="width: 200px;"/>
<img src="././_images/6-June/6-25-20/newSnailSide.png" alt="newSnailSide.png" style="width: 200px;"/>
<img src="././_images/6-June/6-25-20/perspectiveSnail.png" alt="perspectiveSnail.png" style="width: 200px;"/>
<img src="././_images/6-June/6-25-20/snailOrtho.png" alt="snailOrtho.png" style="width: 200px;"/>

## 6/26/20
### Attendance: &#9744; Brody, &#9745; Derek, &#9744; Dylan, &#9744; Ian, &#9744; Jack
Changed the intakes on the new robot to better fit inside the size requirements. The old intakes could not fold up properly without majorly hitting the back wheels and they would stick out, this was fixed by changing the spacing on the intakes to lift them higher up so they stay above the wheels. We do not know how this change will impact picking up balls as we do not have a physical robot to test this on
Fixed random things in cad 
There was chain missing on the first two front rollers
There was no intake flaps on the front intakes
Fixed standoffs not lining up properly with c-channel holes
Fixed alignment of back U-channel 
Fixed cortex blocking the right intake motor from folding properly 

### Intake Changes
<img src="././_images/6-June/6-26-20/intakeAngle.png" alt="intakeAngle.png" style="width: 200px;"/>
<img src="././_images/6-June/6-26-20/intakeSide.png" alt="intakeSide.png" style="width: 200px;"/>

## 6/28/20
### Attendance: &#9744; Brody, &#9744; Derek, &#9744; Dylan, &#9744; Ian, &#9745; Jack
We fixed the Auton Builder. It now stores the inputs from the GUI in independent global variables. The way the Auton Builder works is we press the goal that we want to go to, then the 2nd and 3rd goal we want to go to. After that when it switches to the Autonomous phase the robot knows it starting position and then runs the specific string of code needed to get from the starting position to the wanted goal, then it loops back in the code and based of the new position which is the 1st goal it figures it way to the 2nd goal. It then repeats this to get from the 2nd to the 3rd.

```cpp
	while(startPos == 0){ setStart(); arcChecker(); pros::delay(20);}
   	while(firstPos == 0 && startPos !=0){ setFirst(); arcChecker(); pros::delay(20);}
   	pros::delay(500);
   	while(secondPos == 0 && firstPos != 0){ setSecond();arcChecker(); pros::delay(20);}
   	pros::delay(500);
   	while(thirdPos == 0 && secondPos != 0 && firstPos != 0){ setThird(); arcChecker(); pros::delay(20);}
 	pros::delay(20);
```