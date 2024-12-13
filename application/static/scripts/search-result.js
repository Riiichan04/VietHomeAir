$("#filter").click(function () {
    $("#filter-container").removeClass('d-none');
})

$(".btn-close").click(function (){
    $('#filter-container').addClass('d-none');
})
$(".select-option").click(function (){
    console.log("hehehehehehehhe")
    $(this).addClass("active");
})