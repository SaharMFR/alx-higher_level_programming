$(function () {
	$('DIV#add_item').click(function () {
		$('UL.my_list').append('<li>Item</li>');
	});
	$('DIV#remove_item').click(function () {
		const lastChild = $('UL.my_list').children().last();
		if (lastChild) {
			lastChild.remove();
		}
	});
	$('DIV#clear_list').click(function () {
		$('UL.my_list').empty();
	});
});
