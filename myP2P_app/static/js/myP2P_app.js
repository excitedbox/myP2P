
$(document).ready(function() {
    $('.investor').hide();
    $('.borrower').hide();

    var borrow = $('#Borrow').val();

    $("#go").click(function() {

		if ($('#dropdown').val() == borrow) {
//            console.log("borrower");
            $('.borrower').show();

		} else {
//		    console.log("investor");
            $('.investor').show();
		}


	});
});

