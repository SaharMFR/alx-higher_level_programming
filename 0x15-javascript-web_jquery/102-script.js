$(function () {
	$('INPUT#btn_translate').click(function () {
		const lang = $('INPUT#language_code').val();
		$.get('https://hellosalut.stefanbohacek.dev/?lang='+ lang, function (data) {
			 $('DIV#hello').text(data.hello);
		});
	});
});
