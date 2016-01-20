*** Summary ***

The main objective of my project is how players' physical characteristics (i.e., 
height and weight) affect the baseball performance (Home run, hitting average).

First, height is positively correlated with home run, but negatively correlated 
with batting average. This means that taller players tend to hit more home runs,
but their batting average is lower. 

Second, weight also shows similar correlations as height. It is positively 
correlated with home run, but negatively correlated with batting average.

From these two graphs, it is somewhat clear that short and light players have
higher hitting average, and long and heavy players have higher home runs. This 
is in line with general understandings - Home run hitters are usually big and 
heavy players. 

In this analysis, I decided not to differentiate the handedness

*** Design ***
1. There are only a few samples with very high/low weight and height. If I plot
them without aggregation, it will confuse the viewers, so I group them into a 
one bucket (weight - 160 or below, 205 above; height - 69 or below, 74 or above).

2. Initially, I tried to show the batting average and home runs for each handedness.
However, the number of players with left handed or both handed is much lower than
that of players with right handed, and it wasn't easy to show them together. Instead,
I decided not to differentiate the handedness, and only focus on weight/height 
vs homerun/batting average. 

3. I used a line chart to show the trend more clearly. I used two y axes so that 
home run and batting average can be displayed in a one chart. If I tried to plot
the data for both weight and height together, it will be too crowded, and it will
be confusing to viewers. Instead, I decided to add a radio button for weight and 
height selection.


*** Feedback ***
*** Resources ***
http://dimplejs.org/ - Dimple documentation
http://d3js.org/ - D3 documentation
https://netbeans.org/ - IDE for HTML/Javascript