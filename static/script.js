function set_multiselect()
{
	var multiselect = $('.multiselect');

	$(multiselect).find('select').each(function(){
		$(this).append(
			$('<option />')
			.val('0')
			.text($(this).attr('title'))
			.addClass('label')
		)
		.addClass('disabled')
		.prop('disabled', true)
	});

	get_geo(
		$(multiselect).find('select').first(),
		[$(multiselect).find('select').first().attr('data-query')]
	);

	$(multiselect).find('select').each(function(){

		$(this).on('change', function(){

			if(!$(this).val() || !$(this).next().is('select'))
				return false;

			var parent_val = false,
				query_val;

			if(typeof $(this).attr('data-parent') !== 'undefined')
				parent_val = $(multiselect).find('select[name=' + $(this).next().attr('data-parent') + ']').val();

			query_val  = parent_val || $(this).val();

			if(parseInt(query_val) === 0)
				return false;

			if($(this).children().length > 1)
			{
				var current = $(this);

				do
				{
					current = $(current).next();
					$(current).find('option:not(.label)').remove();
				}
				while(!$(current).is(':last-child'));
			}

			get_geo($(this).next(), [
				$(this).next().attr('data-query'),
				query_val
			]);
		});
	});
}

var geo_cache = [];

function get_geo(dropdown, query)
{
	var fill_dropdown = function(data){

			for(var x in data)
			{
				$(dropdown).append(
					$('<option />')
					.val(data[x].id)
					.text(data[x][$(dropdown).attr('name')])
				)
			}

			$(dropdown).prop('disabled', false).removeClass('disabled');
		};

	if(!geo_cache[query.join('.')])
		geo_cache[query.join('.')] = [];
	else
		return fill_dropdown(geo_cache[query.join('.')]);

	$(dropdown).addClass('loading');

	$.ajax({
		dataType : 'json',
		type : 'GET',
		url  : '/geo/' + query.join('/'),
		success : function(h) {

			fill_dropdown(h.data);
			geo_cache[query.join('.')] = h.data;

		},
		error : function(h) {
			
			if(h.error == 'empty')
			{
				$(dropdown).find('option:not(.label)').remove();
			}

		},
		complete : function()
		{
			$(dropdown).removeClass('loading');
		}
	});

	
}

$(document).ready(set_multiselect);