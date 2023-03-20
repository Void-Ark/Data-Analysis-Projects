# Project SPORTAN

This is an End-to-end Sports Data Analytics Project.  

In this project, I will cover **web scraping** (from the ESPN Cricinfo website), **python**, **pandas**, and **Power BI** to perform analyses on T20 world cup cricket data.

## Objective

- The team should be able to score at least 180 runs on an average
- They should be able to defend 150 runs on an average

### Openers (2)

| **parameters**    | **Description**                   | **Criteria**  |
|-------------------|-----------------------------------|---------------|
| Batting Average   | Average runs scored in an inning  | >30           |
| Strike Rate       | No. of runs scored per 100 balls  | >140          |
| Innings Bated     | Total inning bated                | >3            |
| Boundary %        | % of runs scored in boundaries    | >50           |
| Batting Position  | Order in which the batter played  | <4            |

### Anchors / Middle Order (3)

| **parameters**    | **Description**                   | **Criteria**  |
|-------------------|-----------------------------------|---------------|
| Batting Average   | Average runs scored in an inning  | >40           |
| Strike Rate       | No. of runs scored per 100 balls  | >125          |
| Innings Bated     | Total inning bated                | >3            |
| Average Ball faced| Avg. ball faced in an innings     | >20           |
| Batting Position  | Order in which the batter played  | <2            |

### Finishers / Lower Order Anchor (1)

| **parameters**    | **Description**                   | **Criteria**  |
|-------------------|-----------------------------------|---------------|
| Batting Average   | Average runs scored in an inning  | >25           |
| Strike Rate       | No. of runs scored per 100 balls  | >130          |
| Innings Bated     | Total inning bated                | >3            |
| Average Ball faced| Avg. ball faced in an innings     | >12           |
| Batting Position  | Order in which the batter played  | <4            |
| Innings Bowled    | Total innings bowled by the bowler| >1            |

### All-rounders / Lower Order

| **parameters**     | **Description**                    | **Criteria**  |
|--------------------|------------------------------------|---------------|
| Batting Average    | Average runs scored in an inning   | >15           |
| Strike Rate        | No. of runs scored per 100 balls   | >140          |
| Innings Bated      | Total inning bated                 | >2            |
| Batting Position   | Order in which the batter played   | >4            |
| Innings Bowled     | Total innings bowled by the bowler | >2            |
| Bawling Economy    | Average runs allowed per over      |  <7           |
| Bawling Strike rate| Avg. no. of balls to take a wicket | <20           |


### Specialist Fast Bawler

| **parameters**     | **Description**                    | **Criteria**  |
|--------------------|------------------------------------|---------------|
| Innings Bowled     | Total innings bowled by the bowler | >4            |
| Bawling Economy    | Average runs allowed per over      | <7            |
| Bawling Strike rate| Avg. no. of balls to take a wicket | <16           |
| Bawling Style      | Bawling style of the player        | '%Fast%'      |
| Bawling Average    | No. of runs allowed per wicket     | <20           |
| Dot ball %         | % of dot balls bawled              | >40           |

