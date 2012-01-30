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
        $("tr.gene").each(function(i, tr) {
            var match = $("td.context", tr).html();
            if(match !== null) {
                var phenotype = $("td.phenotype", tr).html();
                $("td.context", tr).html(match.replace(new RegExp('(' + phenotype + ')', 'gi'),'<span class="match">$1</span>'))
            };
        }) ;
    } 
);