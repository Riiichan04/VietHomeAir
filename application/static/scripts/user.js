$("#user-information").click(function () {
    $(".content-property").removeClass("on");
    $(this).addClass("on");
    $("#user-content").load("/user/user-information/");
})
$("#order-history").click(function () {
    $(".content-property").removeClass("on");
    $(this).addClass("on");
    $("#user-content").load("/user/order-history/");
})
$("#viewed-history").click(function () {
    $(".content-property").removeClass("on");
    $(this).addClass("on");
    $("#user-content").load("/user/viewed-history/")
})
$("#review-history").click(function () {
    $(".content-property").removeClass("on");
    $(this).addClass("on");
    $("#user-content").load("/user/review-history/")
})
$("#wishlist").click(function () {
    $(".content-property").removeClass("on");
    $(this).addClass("on");
    $("#user-content").load("/user/wishlist/")
})

$("#logout").click(function () {
    $("#logout-alert").removeClass("d-none");
})

$("#logout-alert").click(function() {
    $("#logout-alert").addClass("d-none");
})

$("#popup-cancel-btn").click(function() {
    $("#logout-alert").addClass("d-none");
})