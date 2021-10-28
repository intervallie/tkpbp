$(document).ready(function () {
    var get_counselor_url = $("#get-counselor-url").html();
    var get_counselor_image = $("#get-counselor-image").html();

    $.ajax({
        type: "GET",
        url: get_counselor_url,
        dataType: "JSON",
        success: async function (response) {
            // Destroy old list
            $("#counselor-list").html("");
            // Append counselor list of selected city
            for (var x of response) {
                var accountFields = x["fields"];
                var card =
                `<div class="card mt-4 mb-4 border-5 cs-rounded-border">
                    <div class="row g-0">
                        <div class="col-4 col-md-2 col-xl-3 m-3">
                        <svg width=150 height=150>
                            <use href="${get_counselor_image}#user-profile"></use>
                        </svg>
                        </div>
                        <div class="col">
                        <div class="card-body">
                            <h5 class="card-title">${accountFields["name"]}</h5>
                            <p class="card-text">Description is not available</p>
                        </div>
                        <div class="card-body mt-4">
                            <div class="d-flex justify-content-end">
                            <button class="btn btn-primary cs-button">Buat jadwal</button>
                            </div>
                        </div>
                        </div>
                    </div>
                </div>`
                var fadeEffect = $(card).hide();
                $("#counselor-list").append(fadeEffect);
                fadeEffect.fadeIn(500);
                await sleep(100);
            }
        }
    });
});

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}