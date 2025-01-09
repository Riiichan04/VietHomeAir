let currentSection = 1
let countUploadedImage = 0

function showSection(section) {
    $(".page-section").addClass("d-none")
    $(`#section-${section}`).removeClass("d-none")
}

let sessionObject = {
    'categoryId': -1,
    'listBnbService': [],
    'name': '',
    'description': '',
    'location': {
        'name': '',
        'lat': -1,
        'lon': -1
    },
    'rule': {
        'checkinId': -1,
        'checkoutId': -1,
        'refundId': -1,
        'secureId': -1
    },
    'ownerId': -1
}

function createLocalStorage() {
    if (localStorage.getItem('bnb-info') === null) {
        localStorage.setItem('bnb-info', JSON.stringify(sessionObject))
    }
}

function updateLocalStorage() {
    localStorage.setItem('bnb-info', JSON.stringify(sessionObject))
}

function setCategory(id) {
    sessionObject.categoryId = id
    updateLocalStorage()
}

function getAddressLocation(address) {
    return fetch("https://nominatim.openstreetmap.org/search.php?q=${ADDRESS}&format=jsonv2")
        .then(async result => {
            if (result.ok) {
                return result.json().then(data => {
                    sessionObject.location.name = address
                    sessionObject.location.lat = data[0].lat
                    sessionObject.location.lon = data[0].lon
                })
            }
            else {
                return "Có lỗi!!!"
            }
        })
}

$("#section-1 .section-card").click(function () {
    const index = $(this).index()
    const categoryId = index + 1
    if (categoryId === sessionObject.categoryId) {
        sessionObject.categoryId = -1
        $(".section-card").css({'background-color': 'rgba(0,0,0,0)'})
    } else {
        setCategory(categoryId)
        $(".section-card").css({'background-color': 'rgba(0,0,0,0.1)'})
        $(this).css({'background-color': 'rgba(0,0,0,0)'})
    }

    if (sessionObject.categoryId !== -1) {
        $("#section-1 .show-section").attr("disabled", false)
    }
    else {
        $("#section-1 .show-section").attr("disabled", true)
    }
})

$("#section-2 .section-card").click(function () {
    const index = $(this).index()
    const serviceIndex = index + 1
    if (sessionObject.listBnbService.indexOf(serviceIndex) !== -1) {
        sessionObject.listBnbService = sessionObject.listBnbService.filter(ele => ele !== serviceIndex)
        $(this).css({'background-color': 'rgba(0,0,0,0.1)'})
    } else {
        sessionObject.listBnbService.push(serviceIndex)
        $(this).css({'background-color': 'rgba(0,0,0,0)'})
        updateLocalStorage()
    }

     if (sessionObject.listBnbService.length >= 4) {
        $("#section-2 .show-section").attr("disabled", false)
    }
    else {
        $("#section-2 .show-section").attr("disabled", true)
    }
})

$("#section-3 input[type=file]").change(function () {
    if ($(this).val()) {
        countUploadedImage++
    }
    if (countUploadedImage === 5) {
        $("#section-3 .show-section").attr("disabled", false)
    }
    else {
        $("#section-3 .show-section").attr("disabled", true)
    }
})

async function getPostInfo() {
    sessionObject.name = $("form #bnb-name").val()
    sessionObject.description = $("form #bnb-description").val()
    sessionObject.ownerId = userId
    sessionObject.location = await getAddressLocation($("form #bnb-location").val())
    return sessionObject
}