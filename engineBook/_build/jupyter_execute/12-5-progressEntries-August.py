# August Progress Entries
## 8/1/20
### Attendance: &#9745; Brody, &#9745; Derek, &#9745; Dylan, &#9745; Ian, &#9745; Jack
Today we started to put the field together so we can now test our robot with an official goal. Along with that we completed the drive base and connected the middle intakes to the drive base. We have shortened our drive base by 1 hole to make building it easier and it should not affect the stability of the drive base. Another problem we ran into was that the back left and back right motors are hard to quick swap because of a metal plate on the bottom of the robot. For now we will keep everything the same and maybe find a way to make those motors easier to swap in the future. 

## 8/2/20
### Attendance: &#9745; Brody, &#9745; Derek, &#9745; Dylan, &#9745; Ian, &#9745; Jack
Changed rubber band position and tension to allow for faster and more efficient intakes. There are no pictures here because it was just moving rubber bands up or down 1-2 notches on a gear.

## 8/6/20
### Attendance: &#9745; Brody, &#9745; Derek, &#9745; Dylan, &#9745; Ian, &#9745; Jack
Today we made the hood for our robot and started testing how it can score in goals. The hood is made out of rubber bands right now as we do not have the polycarbonate we need to complete the hood like our original design. Currently the hood does have some problems but from more testing we have concluded that they should all be solved with the polycarbonate and foam design.

### Pictures of the Hood
<img src="././_images/8-August/8-6-20/hoodFrontView.JPG" alt="hoodFrontView.JPG" style="width: 150px;"/>
<img src="././_images/8-August/8-6-20/hoodHingeBackView.JPG" alt="hoodHingeBackView.JPG" style="width: 200px;"/>
<img src="././_images/8-August/8-6-20/hoodHingeFrontView.JPG" alt="hoodHingeFrontView.JPG" style="width: 175px;"/>
<img src="././_images/8-August/8-6-20/hoodSideView.JPG" alt="hoodSideView.JPG" style="width: 150px;"/>

## 8/7/20
### Attendance: &#9745; Brody, &#9745; Derek, &#9745; Dylan, &#9745; Ian, &#9745; Jack
Today we connected the front intakes to the robot and made the hood able to fold into the robot. The front intakes have been working well but there is a slight problem with the rubber band “hook” on the intakes as it interferes with the center goal post. We can move this easily and it should not be a problem for very long. Unfortunately our main problem with the intakes is that the right intake seems to have a lot of friction compared to the left one. More testing need to be done to find out the cause of this problem as the motor seems to be fine. Along we these problem the intakes can not fold up into size requirements right now because there is a piece that need to be cut and we currently can not do that.
The hood of our robot can now be locked down using a screw catching on a plate. The hood has a bit more tension then we would like so it does come up sometimes and we might have to rework it in the future, but it will work for testing purposes.

### Robot Pictures
<img src="././_images/8-August/8-7-20/allignmentMechanism.JPG" alt="allignmentMechanism.JPG" style="width: 200px;"/>
<img src="././_images/8-August/8-7-20/frontOfRobot.JPG" alt="frontOfRobot.JPG" style="width: 200px;"/>
<img src="././_images/8-August/8-7-20/hoodStartingPosition.JPG" alt="hoodStartingPosition.JPG" style="width: 200px;"/>
<img src="././_images/8-August/8-7-20/intakesAroundMiddleGoal.JPG" alt="intakesAroundMiddleGoal.JPG" style="width: 200px;"/>
<img src="././_images/8-August/8-7-20/rightIntake.JPG" alt="rightIntake.JPG" style="width: 200px;"/>
<img src="././_images/8-August/8-7-20/rightIntakeJoint.JPG" alt="rightIntakeJoint.JPG" style="width: 200px;"/>
<img src="././_images/8-August/8-7-20/robotBackView.JPG" alt="robotBackView.JPG" style="width: 150px;"/>
<img src="././_images/8-August/8-7-20/robotFrontView.JPG" alt="robotFrontView.JPG" style="width: 150px;"/>
<img src="././_images/8-August/8-7-20/robotLeftSideView.JPG" alt="robotLeftSideView.JPG" style="width: 200px;"/>
<img src="././_images/8-August/8-7-20/robotRightSideView.JPG" alt="robotRightSideView.JPG" style="height: 145px;"/>

## 8/8/20
### Attendance: &#9745; Brody, &#9745; Derek, &#9745; Dylan, &#9745; Ian, &#9745; Jack
Fixed various problems with the robot.
Fixed cantilever axle on middle intake.
Replaced temporary rubber band ramp in front of robot with grip mat.
Also added an extra half cut c-channel to make this stick out more.
Changed the standoffs in the front of the intakes into spacers to hopefully solve the high friction issue.
Added bracing to the bottom 2 plates to make the robot stronger.
Replaced sketchy connected axle in back of robot with one solid axle.
Added missing parts in some areas that were not symmetrical.

### Robot Pictures
<img src="././_images/8-August/8-8-20/middleRollersTopGear.JPG" alt="middleRollersTopGear.JPG" style="width: 200px;"/>
<img src="././_images/8-August/8-8-20/middleRollersTopGearSideView.JPG" alt="middleRollersTopGearSideView.JPG" style="width: 200px;"/>
<img src="././_images/8-August/8-8-20/robotBack.JPG" alt="robotBack.JPG" style="width: 200px;"/>
<img src="././_images/8-August/8-8-20/robotBottomView.JPG" alt="robotBottomView.JPG" style="width: 200px;"/>
<img src="././_images/8-August/8-8-20/robotRamp.JPG" alt="robotRamp.JPG" style="width: 150px;"/>

## 8/10/20
### Attendance: &#9745; Brody, &#9745; Derek, &#9745; Dylan, &#9745; Ian, &#9745; Jack
We updated the Slew::driveSlew(double accel) member function. Before we used to just have slew that increased as the joystick increased but now we have implemented the code to realize when the robot is turning and to automatically slow down the drive base when turning even while pushing the joysticks all the way. This addition to the code helps the driver make turns more accurate and easier. We also redid the slew code for the drive base and implemented a basic P loop that gets the difference of the current joystick position and the current output of the robot it then determines whether it needs to add or subtract to get to the target value and then adds/subtracts the given amount that the human inputted into the member function.

```cpp
int Slew::driveSlew(double fwdAccel, double deccel, double revAccel){
leftJoystick = master.get_analog(ANALOG_LEFT_Y);
rightJoystick = master.get_analog(ANALOG_RIGHT_Y);
if(leftJoystick/rightJoystick < 0 || leftJoystick/rightJoystick >=2)driveMax =6000;
if(rightJoystick/leftJoystick < 0 || rightJoystick/leftJoystick >=2)driveMax =6000;

if(master.get_analog(ANALOG_LEFT_Y) < 5 && master.get_analog(ANALOG_LEFT_Y) > -5 ) leftJoystick = 0;
if(master.get_analog(ANALOG_RIGHT_Y) < 5 && master.get_analog(ANALOG_RIGHT_Y) > -5 ) rightJoystick = 0;

leftError = leftJoystick*94.488 - LslewOutput; //1.58
leftOvershoot = deccel - abs(LslewOutput);
if(abs(leftError) == 400)LslewOutput = 0;
if(leftError > 0){if(leftJoystick == 0){ if(leftOvershoot >0){deccel -= leftOvershoot;}LslewOutput +=deccel;}else if(LslewOutput < driveMax){LslewOutput +=fwdAccel;}}
if(leftError < 0){if(leftJoystick == 0){ if(leftOvershoot >0){deccel -= leftOvershoot;}LslewOutput -=deccel;}else if(LslewOutput > -driveMax){LslewOutput -=revAccel;}}
rightError = rightJoystick*94.488 - RslewOutput;
rightOvershoot = deccel - abs(RslewOutput);
if(abs(rightError) == 400) RslewOutput = 0;
if(rightError > 0){if(rightJoystick == 0){ if(rightOvershoot >0){deccel -= rightOvershoot;}RslewOutput +=deccel;}else if(RslewOutput < driveMax){RslewOutput +=fwdAccel;}}
if(rightError < 0){if(rightJoystick == 0){ if(rightOvershoot >0){deccel -= rightOvershoot;}RslewOutput -=deccel;}else if(RslewOutput > -driveMax){RslewOutput -=revAccel;}}
printf("left, LOutput, leftError  %F %F %F \n", rightJoystick, LslewOutput, RslewOutput);

if(RslewOutput > 12000)RslewOutput =12000;
if(LslewOutput > 12000)LslewOutput =12000;

if(LslewOutput == 0) LF.set_brake_mode(MOTOR_BRAKE_COAST); LB.set_brake_mode(MOTOR_BRAKE_COAST);
if(RslewOutput == 0) RF.set_brake_mode(MOTOR_BRAKE_COAST); RB.set_brake_mode(MOTOR_BRAKE_COAST);
LF.move_voltage(LslewOutput);
LB.move_voltage(LslewOutput);
RF.move_voltage(-RslewOutput);
RB.move_voltage(-RslewOutput);

driveMax = 12000;

return 0;
```

## 8/18/20
### Attendance: &#9745; Brody, &#9745; Derek, &#9745; Dylan, &#9745; Ian, &#9745; Jack
We began working on the Intake::autoSort() member function. The robot is now able to identify the opposing alliance’s ball color and will shoot it out the back of the robot. It knows what color is the opposing color by having the use input which alliance they are on and then the robot uses that information to know which color to look for. The robot autosorts by running two member functions of the intake class. First it runs autoSort() then the bulk of the autosorting is done by Intake::calculateSort(int opposingColor). The autosort member function is a switch statement that takes the global variable int Alliance which stores whether we are on the Red or Blue alliance and based on its value will pass a different value into the calculateSort member function. Then the calculateSort function actually takes a snapshot with the vision sensor and checks it for the opposingColor and if found it will run the intakes to send the ball into the back of the robot. 

```cpp
void Intake::calculateSort(int opposingColor){
 	while (true) {
    	 pros::vision_object_s_t latestsnapshot = vis.get_by_sig(0, opposingColor);
    	 std::cout << "sig:" << latestsnapshot.signature << std::endl; //debug
    	 if(latestsnapshot.signature != 0){/*do mvmt to send out back*/}
    	 pros::delay(2);
  	}
}	

Intake& Intake::autoSort(){
  	switch (alliance){
    	case 1:{ calculateSort(REDBALL); break;/*Red Alliance*/}
    	case 2:{ calculateSort(BLUEBALL); break;/*Blue Alliance*/}
  	}
return *this;
}
```

## 8/25/20
### Attendance: &#9745; Brody, &#9745; Derek, &#9745; Dylan, &#9745; Ian, &#9745; Jack
Today we mapped new ideas for improving our GUI. We believe that once we start programming autonomous programs it will be a hassle to constantly download and restart the code. To fix this inconvenience we came up with a new GUI tab that would alter the variables of the drive function so we could perfect the kP, kD, and slew rate values with ease.

<img src="././_images/8-August/8-25-20/guiPlans.jpg" alt="guiPlans.jpg" style="width: 300px;"/>