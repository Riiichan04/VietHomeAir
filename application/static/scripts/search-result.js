$("#filter").click(function () {
    $("#overlay").css("visibility","visible")
    $("#filter-container").removeClass('d-none');
})

$(".btn-close").click(function (){
    $("#overlay").css("visibility","hidden")
    $('#filter-container').addClass('d-none');
})
$(".select-option").click(function (){
    $(this).addClass("active");
})