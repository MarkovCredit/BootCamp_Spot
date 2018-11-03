// from data.js
var tableData = data;

//declare button to watch events
var submit = d3.select('#filter-btn');

//trigger function when submit button is clicked on 
submit.on('click', function(){

    d3.event.preventDefault();

    var inputElement = d3.select('#datetime');

    var inputValue = inputElement.property('value');

    console.log(inputValue);
    // console.log(tableData);

    var filteredData = tableData.filter(date => date.datetime === inputValue);

    console.log(filteredData);
    
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


    var data_ = tabulate(filteredData,
    ['datetime','city','state','country','shape','durationMinutes','comments']);
    //return columns uppercased
    data_.selectAll('thead th')
    .text(function(column){
        return column.chartAt(0).toUpperCase() + column.substr(1);

    });

    
});
    



