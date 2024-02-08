$(function () {
	const translate = () => {
		const lang = $('INPUT#language_code').val();
		$.get('https://hellosalut.stefanbohacek.dev/?lang='+ lang, function (data) {
			$('DIV#hello').text(data.hello);
		});
	};

	$('INPUT#btn_translate').click(translate);
	$('INPUT#language_code').keydown(function (ev) {
		if (ev.key === 'Enter') translate();
	});
});
