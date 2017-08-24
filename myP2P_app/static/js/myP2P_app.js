
$(document).ready(function() {
    $('.investor').hide();
    $('.borrower').hide();
    $('.result').hide();
    $('.register').hide();


    var borrow = $('#Borrow').val();

    $("#go").click(function() {

		if ($('#dropdown').val() == borrow) {
//            console.log("borrower");
            window.location.replace("http://127.0.0.1:8000/register_details_borrowers/");

		} else {
//		    console.log("investor");
            $('.investor').show();
            window.location.replace("http://127.0.0.1:8000/register_details_lenders/");
		}
	});

	    $("#submit-account").click(function() {
            $('.result').show();
            $('#submit-account').hide();
            $('.register').show();
	    });

});

