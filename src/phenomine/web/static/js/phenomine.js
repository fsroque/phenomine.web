function disableButtons()
{
    $(".button").attr('disabled','disabled')
	$(".button").addClass('disabled');
	$("#form\\.phenotypes").attr('disabled','disabled')
	$("#form\\.phenotypes").addClass('disabled');
	$("#form\\.search").attr('disabled','disabled')
	$("#form\\.search").addClass('disabled');
}
function enableButtons()
{
    $(".button").removeAttr('disabled');
	$(".button").removeClass('disabled');
	$("#form\\.phenotypes").removeAttr('disabled');
	$("#form\\.phenotypes").removeClass('uneditable-input');
	$("#form\\.search").removeAttr('disabled');
	$("#form\\.search").removeClass('uneditable-input');
	
}
$(document).ready(function() 
    { 
		$("#form\\.actions\\.searchHome").addClass('btn').addClass('btn-success');
		$("#form\\.actions\\.clearHome").addClass('btn');
		$("#form\\.phenotypes").elastic();
        // $("#results").tablesorter({headers: { 5: { sorter: false}}}); 
        $("tr.gene").each(function(i, tr) {
            var match = $("td.context", tr).html();
            if(match !== null) {
                var phenotype = $("td.phenotype", tr).html();
                $("td.context", tr).html(match.replace(new RegExp('(' + phenotype + ')', 'gi'),'<span class="match">$1</span>'))
            };
        }) ;
    } 
);