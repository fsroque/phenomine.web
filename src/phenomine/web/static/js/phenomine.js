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
function formError()
{
	$("#form\\.control\\.group").addClass('error');
	$("#form\\.control\\.group\\.controls").append('<p class="help-block">You must specify a list of phenotypes.</p>');
}
$(document).ready(function() 
    { 
		$("#form\\.actions\\.searchHome").addClass('btn').addClass('btn-success');
		$("#form\\.actions\\.clearHome").addClass('btn');
		$("#form\\.phenotypes").elastic();
		var dontSort = [];
		                $('#results thead th').each( function () {
		                    if ( $(this).hasClass( 'no_sort' )) {
		                        dontSort.push( { "bSortable": false } );
		                    } else {
		                        dontSort.push( null );
		                    }
		                } );
		$("#results").dataTable( {
			"bPaginate": false,
			"bFilter": false,
			"aoColumns": dontSort,
			"oLanguage": {
				      "sInfo": "Found <strong>_TOTAL_</strong> matches"
				    }, 
			"oTableTools": {
						"sSwfPath": "http://localhost/~chico/copy_cvs_xls.swf",
						"aButtons": [
										{
											"sExtends": "copy",
											"bSelectedOnly": true,
											"sToolTip": "Copy selected rows"
										},
										{
											"sExtends": "csv",
											"bSelectedOnly": true,
											"sFileName": "phenomine.csv",
											"sToolTip": "Save as CSV"
										},
										{
											"sExtends": "xls",
											"bSelectedOnly": true,
											"sFileName": "phenomine.xls",
											"sToolTip": "Save as Excel file"
										},
									],
						"sRowSelect": "multi",
			        },
		    "sDom": "<'row'<'span6'i><'span6'T>r>t<'row'<'span6'p>>"
		    } );
		$.extend( $.fn.dataTableExt.oStdClasses, {
		    "sWrapper": "dataTables_wrapper form-inline"
		} );
        $("tr.gene").each(function(i, tr) {
            var match = $("td.context", tr).html();
            if(match !== null) {
                var phenotype = $("td.phenotype", tr).html();
                $("td.context", tr).html(match.replace(new RegExp('(' + phenotype + ')', 'gi'),'<strong>$1</strong>'));
            };
        }) ;
    } 
);