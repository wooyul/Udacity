//Read data and call draw function
function read(myRadio) {
    d3.select('svg').remove();
    d3.csv("data/baseball_data.csv", function(data) {
        draw(data, myRadio.value);
    });
    }
  
function draw(data, userInput) {
    "use strict";
    var margin = 75,
    width = 1100 - margin,
    height = 500 - margin;

    var svg = d3.select("body")
            .append("svg")
            .attr("width", width + margin)
            .attr("height", height + margin)
            .append('g')
            .attr('class','chart');
        
    var myChart = new dimple.chart(svg, data);
    
    data.forEach(function(d) {
        //Categorization of height
        if (d["height"] <=69) {
            d["height"] = "69 or below";
        } else if (d["height"] <=70) {
            d["height"] = "70";
        } else if (d["height"] <=71) {
            d["height"] = "71";
        } else if (d["height"] <=72) {
            d["height"] = "72";
        } else if (d["height"] <=73) {
            d["height"] = "73";
        } else {
            d["height"] = "74 or above";
        } 
        
        //Categorization of weight
        if (d["weight"] <=160) {
            d["weight"] = "160 or below";
        } else if (d["weight"] <= 175) {
            d["weight"] = "160 - 175";
        } else if (d["weight"] <= 185) {
            d["weight"] = "175 - 185";
        } else if (d["weight"] <= 195) {
            d["weight"] = "185 - 195";
        } else if (d["weight"] <= 205) {
            d["weight"] = "195 - 205";
        }
        else {
            d["weight"] = "205 above";
        }
    });
    
    //Customrzation of x axis title and ordering based on x-axis data.
    if (userInput === "height") {
        var x = myChart.addCategoryAxis("x", ["height"]);
        x.title = "Height of players in inches";
        x.addOrderRule((["69 or below", "70", "71", "72", "73","74 or above"]))
    } else {
        var x = myChart.addCategoryAxis("x", ["weight"]);
        x.title = "Weight of players in pounds";
        x.addOrderRule((["160 or below", "160 - 175", "175 - 185", "185 - 195", "195 - 205","205 above"]))
    }
            
    var y1 = myChart.addMeasureAxis("y", "HR");
    var y2 = myChart.addMeasureAxis("y", "avg");
    y1.title = "Home Run";
    y2.title = "Batting Average"
    y2.tickFormat = ',.3f';
    x.fontSize = 15;
    y1.fontSize = 15;
    y2.fontSize = 15;
    
    var series1 = myChart.addSeries("Home Run", dimple.plot.line, [x, y1]);
    var series2 = myChart.addSeries("Batting Average", dimple.plot.line,[x, y2]);
    series1.aggregate = dimple.aggregateMethod.avg;  
    series2.aggregate = dimple.aggregateMethod.avg; 
    series1.lineMarkers = true;
    series2.lineMarkers = true;
    myChart.addLegend(200, 10, 360, 20, "right");
    myChart.draw();
};
