function disableButtons()
{
    $(".button").attr('disabled','disabled')
	$(".button").addClass('disabled');
	$("#form\\.phenotypes").attr('disabled','disabled')
	$("#form\\.phenotypes").addClass('disabled');
	$('#form\\.search input').attr('disabled','disabled')
	$('#form\\.search label').addClass('muted')
}
function enableButtons()
{
    $(".button").removeAttr('disabled');
	$(".button").removeClass('disabled');
	$("#form\\.phenotypes").removeAttr('disabled');
	$("#form\\.phenotypes").removeClass('uneditable-input');
	$('#form\\.search input').removeAttr('disabled')
	$('#form\\.search label').removeClass('muted')
	
}
function formError()
{
	$("#form\\.control\\.group").addClass('error');
	$("#form\\.control\\.group\\.controls").append('<p class="help-block">You must specify a list of phenotypes.</p>');
}
var shared = {
   style: {
      tip: true,
	  classes: 'ui-tooltip-green ui-tooltip-shadow ui-tooltip-rounded'
   }
};
$(document).ready(function() 
    { 
		//style buttons
		$("#form\\.actions\\.searchHome").addClass('btn').addClass('btn-success');
		$("#form\\.actions\\.clearHome").addClass('btn');
		//initiate elastic input field
		$("#form\\.phenotypes").elastic();
		//tooltips
		$('#form\\.phenotypes').qtip( $.extend({}, shared, { 
		   content: 'Input phenotypes in the box, one per line.',
		   position: { my: 'right center', at: 'left center' }
		}));
		$('#form\\.search\\.no').qtip( $.extend({}, shared, { 
		   content: 'If text mining is disabled, the server will only output genes which are directly associated with a given phenotype in morbidmap. Phenotypes are matched only by name.',
		   position: { my: 'top center', at: 'bottom center' }
		}));
		$('#form\\.search\\.partial').qtip( $.extend({}, shared, { 
		   content: 'The search will aditionally include the phenotype description text. Any exact match for the phenotype in an OMIM entry will return the associated genes. Only phenotypes for which the molecular basis is known (\'#\' prefix in OMIM) are included.',
		   position: { my: 'top center', at: 'bottom center' }
		}));
		$('#form\\.search\\.full').qtip( $.extend({}, shared, { 
		   content: 'This option will extend the partial search to include phenotypes or loci for which the underlying molecular basis is not known (\'%\' prefix in OMIM).',
		   position: { my: 'top center', at: 'bottom center' }
		}));
		// datatables
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
						"sSwfPath": "http://www.ii.uib.no/~fro061/webservices/copy_cvs_xls.swf",
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
		// highlight matching text snippets
        $("tr.gene").each(function(i, tr) {
            var match = $("td.context", tr).html();
            if(match !== null) {
                var phenotype = $("td.phenotype", tr).html();
                $("td.context", tr).html(match.replace(new RegExp('(' + phenotype + ')', 'gi'),'<strong>$1</strong>'));
            };
        }) ;
    } 
);