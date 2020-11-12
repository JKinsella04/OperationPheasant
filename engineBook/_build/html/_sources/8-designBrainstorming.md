# Change Up Design Brainstorming

## Problem Statememt
The challenge of Change Up is to *score* Balls and *connect rows* to score more points than the opposing Alliance at the end of the match.

## Design Statement
Design, build, test, and compete with a Robot capable of efficiently *scoring Balls* and *connecting rows* in Change Up.

## Constraints
- The Robot must not exceed 18" by 18" by 18" before the match starts
- The Robot must be completed by 9/X/20.
- There is a limit of eight (8) V5 motors per Robot.
- We will need multiple Autonomous Programs since the Autonomous of our Alliance partner will be difficult to predict.

## Robot Criteria
- Must be capable of *scoring Balls* and *connecting rows*.
- Must be capable of holding multiple *Balls* at once.

## Robot Componets
- Drive Base; must be fast and resistant to pushing
- Lift or Snail Design; must be fast, capable of *scoring* and *descoring* in all *Goals*.
- Intakes; must be able to grab *Balls* in any position i.e. versatile.
- Rollers; must be able to shoot the *Balls* into the *Goal* on first try and quickly.

## Drive Base Designs
### Holonomic/X-Drive
### Mecanum Drive
### Omni Wheel Drive
### Omni and Traction Wheel Drive
## Lifts and Trays
### Simple Tray
### Complex Tray
### Four bar (4bar)
### Double Reverse Four Bar (DR4B)
### Six bar
## Intake Designs
### Flaps
### Wheel Intake

## Lift/Tray Design Matrix
| Design       | Stability | Extension | Speed | Complexity | Total |
|--------------|-----------|-----------|-------|------------|-------|
| Simple Tray  | 1         | N/A       | 4     | 2          | 7     |
| Complex Tray | 1         | N/A       | 4     | 0          | 5     |
| 6 Bar        | 2         | 2         | 2     | 3          | 9     |
| 4 Bar        | 3         | 3         | 1     | 4          | 11    |
| DR4B         | 4         | 4         | 3     | 1          | 12    |

Based on our design matrix for Lifts/Trays, the DR4B scored the highest however, we decided to do a 6 Bar as an early season bot beacuse it scored only 3 less and this competition it will fit easier in size than a DR4B will.

## Robot Archetypes Matrix
| Design    | Ball Capacity | Complexity | Versatility | Total |
|-----------|---------------|------------|-------------|-------|
| Tray Bot  | 6             | 2          | 2           | 10     |
| Snail Bot | 3             | 1          | 5           | 9     |
| Tiny Boi  | 2             | 5          | 0           | 7     |

Based on our design matrix for Robot Archetypes, the Tray Bot scored the highest. We will go with this design because we believe that it will be a very successful design.

## Intake Design Matrix
| Design | Complexity | Traction | Total |
|--------|------------|----------|-------|
| Flaps  | 1          | 2        | 3     |
| Wheels | 2          | 1        | 3     |

Based on our design matrix, the two types of intakes tied. We decided to first attempt a flap style intake as it will be able to enter the *Goals* easier than a wheel intake would.

## Drive Base Matrix
| Design          | Traction | Strafing | Stability | Complexity | Speed | Resistance to Pushing | Total |
|-----------------|----------|----------|-----------|------------|-------|-----------------------|-------|
| Mecanum         | 2        | 2        | 2         | 1          | 2     | 0                     | 9     |
| Omni            | 1        | 0        | 3         | 2          | 2     | 2                     | 10    |
| Omni + Traction | 3        | 0        | 0         | 3          | 0     | 3                     | 9     |
| X-drive         | 0        | 3        | 1         | 0          | 3     | 1                     | 6     |

Based on our design matrix, omni wheels are the best overall, but the ability to strafe would be very valuable during Autonomous for this reason we have decided to use a mecanum drive base.

> For the design marticies, higher values are better. Simple designs score higher on the complexity category for this reason.