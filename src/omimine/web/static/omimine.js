function disableButtons()
{
    $(".button").attr('disabled','disabled')
}
function enableButtons()
{
    $(".button").removeAttr('disabled');
}
$(document).ready(function() 
    { 
        $("#results").tablesorter({headers: { 5: { sorter: false}}}); 
    } 
);