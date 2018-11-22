// @TODO: YOUR CODE HERE!
var svgWidth = 960;
var svgHeight = 500;

var margin = {
  top: 20,
  right: 40,
  bottom: 80,
  left: 100
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Create an SVG wrapper, append an SVG group that will hold our chart,
// and shift the latter by left and top margins.


//testing code
// d3.select('body').append('svg').
// attr("width", 50).attr("height", 50)
// .append("circle").attr("cx", 25).attr("cy", 25)
// .attr("r", 25).style("fill", "purple");

var svg = d3
  .select("body")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

// Append an SVG group
var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

var chosenXAxis = "poverty";

function xScale(povdata, chosenXAxis) {
    // create scales
    var xLinearScale = d3.scaleLinear()
      .domain([d3.min(povdata, d => d[chosenXAxis]) * 0.8,
        d3.max(povdata, d => d[chosenXAxis]) * 1.2
      ])
      .range([0, width]);
  
    return xLinearScale;
  
  }

  function renderAxes(newXScale, xAxis) {
    var bottomAxis = d3.axisBottom(newXScale);
  
    xAxis.transition()
      .duration(1000)
      .call(bottomAxis);
  
    return xAxis;
  }

  function renderCircles(circlesGroup, newXScale, chosenXaxis) {

    circlesGroup.transition()
      .duration(1000)
      .attr("cx", d => newXScale(d[chosenXAxis]));
  
    return circlesGroup;
  }
  // function rendertext(textGroup, newXScale, chosenXaxis) {

  //   textGroup.transition()
  //     .duration(1000)
  //     .attr("cx", d => newXScale(d[chosenXAxis]));
  
  //   return textGroup;
  // }


  function updateToolTip(chosenXAxis, circlesGroup) {

    if (chosenXAxis === "poverty") {
      var label = "Poverty:";
    }
    else {
      var label = "Age";
    }
  
    var toolTip = d3.tip()
      .attr("class", "d3-tip")
      .offset([80, -60])
      .html(function(d) {
        return (`${d.state}<br>${label} ${d[chosenXAxis]}`);
      });
  
    circlesGroup.call(toolTip);
  
    circlesGroup.on("mouseover", function(data) {
      toolTip.show(data);
    })
      // onmouseout event
      .on("mouseout", function(data, index) {
        toolTip.hide(data);
      });
  
    return circlesGroup;
  }

  d3.csv("data.csv", function(err, povdata) {
    if (err) throw err;
  
    // parse data
    povdata.forEach(function(data) {
      data.poverty = +data.poverty;
      data.age = +data.age;
      data.noHealthInsurance = +data.noHealthInsurance
      data.state = data.state;
    });
    console.log(povdata)
    var xLinearScale = xScale(povdata, chosenXAxis);

  // Create y scale function
  var yLinearScale = d3.scaleLinear()
    .domain([0, d3.max(povdata, d => d.noHealthInsurance)])
    .range([height,0]);

  // Create initial axis functions
  var bottomAxis = d3.axisBottom(xLinearScale);
  var leftAxis = d3.axisLeft(yLinearScale);
  console.log(yLinearScale)
// append x axis
var xAxis = chartGroup.append("g")
.classed("x-axis", true)
.attr("transform", `translate(0, ${height})`)
.call(bottomAxis);
// append y axis
chartGroup.append("g")
.call(leftAxis);
var circlesGroup = chartGroup.selectAll("circle")
    .data(povdata)
    .enter()
    .append("circle")
    .attr("cx", d => xLinearScale(d[chosenXAxis]))
    .attr("cy", d => yLinearScale(d.noHealthInsurance))
    .attr("r", 25)
    .attr("fill", "blue")
    .attr("opacity", ".375")

    var textGroup = chartGroup.selectAll("text")
    .data(povdata)
    .enter()
    .append("text")
    .classed("stateText",true)
    .attr("x", d => xLinearScale(d[chosenXAxis]))
    .attr("y", d => yLinearScale(d.noHealthInsurance))
    .text(d => d.abbr); 
// var textGroup = chartGroup.append('text')
// .data(povdata)
//     .enter()
//     .append("text")
//     .attr("cx", d => xLinearScale(d[chosenXAxis]))
//     .attr("cy", d => yLinearScale(d.healthcare))
//     .text(function(d){return d.state})

    
    
// var circleattr = circlesGroup
//                 .attr('cx', function (d){return d.state})
//                 .attr("cy", function (d) { return d.state})
//                .attr("r", 20 );
// var circleText = chartGroup.selectAll('text')
//     .data(povdata)
//     .attr('dx',12)
//     .attr('dy','.35em')
//     .text(function(d) {return d.state})


    ;
 // Create group for  2 x- axis labels
 var labelsGroup = chartGroup.append("g")
 .attr("transform", `translate(${width / 2}, ${height + 20})`);
 
 var povlabel = labelsGroup.append("text")
    .attr("x", 0)
    .attr("y", 20)
    .attr("value", "poverty") // value to grab for event listener
    .classed("active", true)
    .text("Poverty measure");
  var agelabel = labelsGroup.append("text")
    .attr("x", 0)
    .attr("y", 40)
    .attr("value", "age") // value to grab for event listener
    .classed("inactive", true)
    .text("Age (median) yrs");
    // append y axis
    chartGroup.append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 0 - margin.left)
    .attr("x", 0 - (height / 2))
    .attr("dy", "1em")
    .classed("aText", true)
    .text("Lacking Health Insurance %");

    var circlesGroup = updateToolTip(chosenXAxis, circlesGroup);


    // x axis labels event listener
  labelsGroup.selectAll("text")
  .on("click", function() {
    // get value of selection
    var value = d3.select(this).attr("value");
    if (value !== chosenXAxis) {

      // replaces chosenXAxis with value
      chosenXAxis = value;

      // console.log(chosenXAxis)

      // functions here found above csv import
      // updates x scale for new data
      xLinearScale = xScale(povdata, chosenXAxis);

      // updates x axis with transition
      xAxis = renderAxes(xLinearScale, xAxis);

      // updates circles with new x values
      circlesGroup = renderCircles(circlesGroup, xLinearScale, chosenXAxis);

      // updates tooltips with new info
      circlesGroup = updateToolTip(chosenXAxis, circlesGroup);

      // changes classes to change bold text
      if (chosenXAxis === "poverty") {
        povlabel
          .classed("active", true)
          .classed("inactive", false);
        agelabel
          .classed("active", false)
          .classed("inactive", true);
      }
      else {
        povlabel
          .classed("active", false)
          .classed("inactive", true);
        agelabel
          .classed("active", true)
          .classed("inactive", false);
      }
    }
  });
  })