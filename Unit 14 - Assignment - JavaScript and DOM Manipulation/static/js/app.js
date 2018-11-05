// from data.js
var tableData = data;
var submit = d3.select('#filter-btn');

//create out function that reacts when user clicks the submit button
submit.on('click', function(){

    //we are preventing refresh and also removing any 
    //previous search results or No results paragraphs
    d3.event.preventDefault();
    d3.selectAll('th').remove()
    d3.selectAll('td').remove()
    d3.selectAll('p').remove()
    
    var inputElement = d3.select('#datetime');
    
    var inputValue = inputElement.property('value');
    
    console.log(inputValue);
    // console.log(tableData);
    
    var filteredData = tableData.filter(date => date.datetime === inputValue);

    console.log(filteredData);
    //in this function, data and columns are recognized
    //by d3/js 
    function tabulate(data, columns){
        
        var table = d3.select("#ufo-table").append('table'),
        thead = table.append('thead'),
        tbody = table.append('tbody');

        thead.append('tr')
        .selectAll('th')
        .data(columns)
        .enter()
        .append('th')
        .text(function(column){return column;});


        var rows = tbody.selectAll("tr")
        .data(data)
        .enter()
        .append("tr");

    // create a cell in each row for each column
        var cells = rows.selectAll("td")
        .data(function(row) {
            return columns.map(function(column) {
                return {column: column, value: row[column]};
            });
        })
        .enter()
        .append("td")
            .text(function(d) { return d.value; });
    
    return table;


    }//call the tabulate function as pass our filtered data as well as the columns we want
    //if filtered data is an empty list, tell the user no results
    //and print to console no results. other wise, call our
    //tabulate data function with the following columns
    if(filteredData.length === 0){console.log('noresults');
    d3.event.preventDefault();
    var table = d3.select("#ufo-table").append('table'),
    thead = table.append('thead')
    thead.append('p').text('No Results Try Again') }
    else{

    var data_ = tabulate(filteredData,
    ['datetime','city','state','country','shape','durationMinutes','comments']);
   
    }
    
});


    



