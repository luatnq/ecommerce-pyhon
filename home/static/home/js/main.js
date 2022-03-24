$(document).ready(function() {
    var value = $('#productType').find(":selected").val();
    if (value == 1) {
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
            $('#list_2').css("display", "none");
            $('#list_1').css("display", "block");
            $('#list_1').html(response.book_list)
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

function saveBookItem() {
    $.ajax({
        url: "/home/create_book_item",
        type: "POST",
        data: $("#formCreateBookItem").serialize(),
        success: (response) => {
            $('#bookItemModal').modal('hide');

        },
    });
}


function bookList() {
    // $("#bookList").children().remove();
    $.ajax({
        url: "/home/",
        method: "POST",
        success: function(response) {
            console.log("success");
            $('#list_2').css("display", "none");
            $('#list_1').css("display", "block");
            $('#bookList tbody').html(response.books)
        },
    });
}

function laptopList() {
    $("#laptopList").children().remove();
    $.ajax({
        url: "/home/laptops",
        method: "POST",
        success: function(response) {
            console.log(response.laptop_list);
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
    if (value == 1) {
        bookList();
    }
});

function editBook(id) {
    $.ajax({
        url: "/home/book_detail",
        method: "POST",
        data: { id: id },
        success: (response) => {
            console.log(response)

            let item = JSON.parse(response);
            $("#id").val(item[0].pk);
            console.log(item[0].pk);
            $("#bookName").val(item[0].fields.bookName);
            $("#barcode").val(item[0].fields.barcode);
            $("#quantity").val(item[0].fields.quantity);
            $("#author").val(item[0].fields.author);

            $('#editBookModal').modal('show');
        },
    });
}

function updateBook() {
    $.ajax({
        url: "/home/update_book",
        type: "POST",
        data: $("#formEditBook").serialize(),
        success: (response) => {

            $('#editBookModal').modal('hide');
            $('#list_2').css("display", "none");
            $('#list_1').css("display", "block");
            $('#list_1').html(response.book_list)
        },
    });
}

// $('#editBookModal').on("click", ".show-form-update", editBook);





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