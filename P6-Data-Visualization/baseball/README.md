*** Summary ***

The main objective of my project is to find out how players' physical 
characteristics (i.e., height and weight) affect the baseball performance 
(Home run, hitting average).

First, height is positively correlated with home run, but negatively correlated 
with batting average. This means that taller players tend to hit more home runs,
but their batting average is lower. 

Second, weight also shows similar correlations as height. It is positively 
correlated with home run, but negatively correlated with batting average.

From these two graphs, it is somewhat clear that short and light players have
higher hitting average, and long and heavy players have higher home runs. This 
is in line with general understandings - Home run hitters are usually big and 
heavy players. 

In this analysis, I decided not to differentiate the handedness.

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

** tommi_28863820h **
I found it interesting that there was such a clear correlation between 
homeruns/batting average and weight/height. I did have a quick look at this 
dataset myself and perhaps my initial bias prevented me from discovering these 
relationships myself. Also it is interesting that homeruns and batting averages 
correlate oppositely to weight and height (homeruns have a positive correlation 
while batting averages have negative).

I think the takeaway of this visualization is to show the relationship between 
height and weight and the batting averages and amount of homeruns. I think the 
visualization does this very well. This may be obvious to most but perhaps 
adding units to the y-axes as well is a good idea? Also perhaps, as previously 
mentioned, the visualization conveys a false (although I'm not sure if this is 
false, not a baseball expert :slightly_smiling: ) indication of a relationship 
between batting averages and homeruns through the use of the grey horizontal 
lines.

Overall I think there is a clear story in the visualization and the 
visualization conveys it's message very well


** mb842x1d **
I have very little knowledge of Baseball but I found it interesting that height 
and weight of the players do affect HR/batting average in such clear manner. 
I think the ultimate conclusion is shorter or less weight players will have 
higher number of HRs but if you want higher batting average go for some one 
tall and big :slightly_smiling:

One thing that confused me at first was the horizontal lines (the ones in gray) 
that you have connecting the two Y-axis.This could be because of my naivety on 
the game but are the HRs related to batting average? Those lines seem to 
indicate that.

Apart from that, I think the presentation is clear and well communicated.

** From my friend ** 
What questions do you have about the data?
I didn't look at the data, so it is not clear how long the data has been
collected, and how many people are involved. Basically, it doesn't include
basic information about the data.

What relationships do you notice?
It clearly shows the pattern of home run and batting average vs weight and height
In some cases, it is not always increasing or decreasing, but the tendency
is still clear

Is there something you don’t understand in the graphic?
The number of samples in each point is not plotted here. It would be interesting
to see them together.

*** Resources ***
http://dimplejs.org/ - Dimple documentation
http://d3js.org/ - D3 documentation
https://netbeans.org/ - IDE for HTML/Javascript