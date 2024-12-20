let currentRating = 0

$("#close-popup-btn").click(function () {
    $(".popup-container").css("display", "none")
})

$("#show-description-popup").click(function () {
    $(".popup-container").css("display", "block")
})

$("#share-btn").click(function () {
    navigator.clipboard.writeText(window.location.href) //Viết url hiện tại vào clipboard
})
// Click vào số sao ở mục đánh giá để bình luận số sao
$(".comment-star-icon").click(function () {
    const currentElement = $(this).index() + 1  //Lấy số sao muốn đánh giá
    const listElement = $(".comment-star-icon")
    console.log(currentRating)
    //Xử lý trường hợp click lại số sao vừa đánh giá để clear số sao đánh giá
    if ($(this).hasClass("fa-solid") && currentElement === currentRating) {
        listElement.removeClass("fa-solid")
        listElement.addClass("fa-regular")
        currentRating = 0
        $("#review-current-star").text("0.0")
    } else {
        //Tắt mask từ cho số sao cần hiển thị
        currentRating = currentElement
        for (let i = 0; i < currentElement; i++) {
            listElement.eq(i).addClass("fa-solid")
            listElement.eq(i).removeClass("fa-regular")
        }
        //Bật mask cho số sao còn lại
        for (let i = currentElement; i < 5; i++) {
            listElement.eq(i).removeClass("fa-solid")
            listElement.eq(i).addClass("fa-regular")
        }
        $("#review-current-star").text(currentRating + ".0")
    }
})