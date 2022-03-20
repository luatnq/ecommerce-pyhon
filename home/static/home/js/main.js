$(document).ready(function() {
    var value = $('#productType').find(":selected").val();
    if (value == 7) {
        $('#list_2').css("display", "none");
    }
});

function saveBook() {
    $.ajax({
        url: "/home/create_book",
        type: "POST",
        data: $("#formCreateBook").serialize(),
        success: (response) => {
            $('#bookModal').modal('hide');
            $('#bookList tbody').html(response.book_list)
        },
    });
}

function saveLaptop() {
    $.ajax({
        url: "/home/create_laptop",
        type: "POST",
        data: $("#formCreateLaptop").serialize(),
        success: (response) => {
            $('#laptopModal').modal('hide');
            laptopList();
        },
    });
}

function bookList() {
    $("#bookList").children().remove();
    $.ajax({
        url: "/home/",
        method: "POST",
        success: function(response) {
            console.log("success");
            $('#bookList tbody').html(data.bookList)
        },
    });
}

function laptopList() {
    $("#laptopList").children().remove();
    $.ajax({
        url: "/home/laptops",
        method: "POST",
        success: function(response) {
            console.log(response);
            $('#list_1').css("display", "none");
            $('#list_2').css("display", "block");
            $('#list_2').html(response.laptop_list)
        },
    });
}

$('#productType').on('change', function() {
    var value = $(this).val();
    console.log(value);
    if (value == 2) {
        laptopList();
    }
});

function editBook() {

}





$(function() {
    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });
});

function getCookie(c_name) {
    if (document.cookie.length > 0) {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1) {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start, c_end));
        }
    }
    return "";
}
// set cookie
$.cookie('cookiename', 'cookievalue');
// read cookie
var myCookie = $.cookie('cookiename');
// delete cookie
$.cookie('cookiename', null);