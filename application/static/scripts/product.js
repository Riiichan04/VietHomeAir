$("#close-popup-btn").click(function(){
    $(".popup-container").css("display", "none")
})

$("#show-description-popup").click(function (){
    $(".popup-container").css("display", "block")
})

$("#share-btn").click(function () {
    navigator.clipboard.writeText(window.location.href) //Viết url hiện tại vào clipboard
})