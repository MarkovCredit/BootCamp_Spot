

function buildMetadata(sample) {
  
  
  
  var meta_url = `metadata/${sample}`
  // Using `d3.json` to fetch the metadata for a sample
    // Using d3 to select the panel with id of `#sample-metadata`
   d3.json(meta_url).then(function(sample){
    var metadata = d3.select('#sample-metadata');
    metadata.html("")
    // Using `Object.entries` to add each key and value pair to the panel
  
    Object.entries(sample).forEach(function([key,value]){
      var item = metadata.append('p');
      item.text(`${key}: ${value}`);
    })
    console.log(sample)
    
   })
  };

   
    
    
function buildCharts(sample) {
  var url = `sample/${sample}`;
  // @TODO: Use `d3.json` to fetch the sample data for the plots
  d3.json(url).then(function(sample){
    console.log(sample);
    
    

    var trace = {
      x : sample.otu_ids,
      y: sample.sample_values,
      mode : 'markers',
      marker: {
        color : sample.otu_ids,
        size : sample.sample_values 
      },
      
      
    };
    var data = [trace]
    
  var layout = {
  title: ' Size',
  showlegend: false,
  height: 600,
  width: 600
  };
    
    Plotly.newPlot('bubble', data, layout)
  
    // @TODO: Build a Bubble Chart using the sample data

    // @TODO: Build a Pie Chart
    // HINT: You will need to use slice() to grab the top 10 sample_values,
    // otu_ids, and labels (10 each).
    var data_ss = sample.sample_values.slice(0,9)
    var data_sotu = sample.otu_ids.slice(0,9)
    var data_labels = sample.otu_labels.slice(0,9)

    var pie_trace = {
      values: data_ss,
      labels: data_sotu,
      type: 'pie'
    }
    var pie_data = [pie_trace]
  

  var layout_2 = {
      height: 1000,
      width: 600
    };

    Plotly.newPlot('pie',pie_data,layout_2)
    

console.log(sample.sample_values.slice(0,9))
console.log(sample.otu_ids.slice(0,9))
console.log(sample.otu_labels.slice(0,9))

  })
}

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();
