$(document).ready(function () {
    $("#buy-course").submit(function (event) {
        event.preventDefault();

        var formActionUrl = $(this).attr("action"); // Получаем URL из action

        var formData = $(this).serialize();

        $.ajax({
            url: formActionUrl, // Используем URL из формы
            type: "POST",
            data: formData,
            dataType: "json",
            success: function (response) {
                $("#buy-course-container").html('<a class="btn btn-primary" href="/basket/" role="button">Перейти в корзину</a>');
                $("#basket-count").text(response.total_items);
            }

        });
    });

    //Реализован на vue.js

    // $("#basket-remove").submit(function (event) {
    //     event.preventDefault();
    //     var $formDiv = $(this).parent();
    //     var formActionUrl = $(this).attr("action"); // Получаем URL из action

    //     var formData = $(this).serialize();

    //     $.ajax({
    //         url: formActionUrl, // Используем URL из формы
    //         type: "POST",
    //         data: formData,
    //         dataType: "json",
    //         success: function (response) {
    //             $formDiv.remove();
    //         }

    //     });
    // });
});