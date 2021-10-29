$(document).ready(function () {
    $.updateList(get_counselor_url + "Jakarta")

    $("#city-select").change(function (e) {
        e.preventDefault();
        $.updateList(get_counselor_url + $(this).find(":selected").text());
    });

    $("#counselor-list").on("click", ".cs-button-submit", function() {
        console.log("trying to submit form")
        var submit_url = `${formSubmitURL}` + $(this).attr("data-pk");
        var counselor_name = $(this).attr("data-counselor-name");
        var serializedForm = $("#consultation_form").serialize();
        $.ajax({
            type: "POST",
            url: submit_url,
            data: serializedForm,
            success: function (response) {
                var success_notification = new bootstrap.Modal(document.getElementById('success-modal'));
                $("#success-message").text(`Anda berhasil membuat jadwal dengan konselor ${counselor_name}`);
                success_notification.show();
                document.getElementById("consultation_form").reset();
            },
            error: function (response) {
                var failed_notification = new bootstrap.Modal(document.getElementById("failed-modal"));
                failed_notification.show();
            }
        });
    });
});

$.extend({
    updateList: function(counselor_url) {
        // Destroy old list
        $("#counselor-list").html("");
        $.ajax({
            type: "GET",
            url: counselor_url,
            dataType: "JSON",
            success: async function (response) {
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
                                        <button type="button" class="btn btn-primary cs-button-submit" data-pk="${x["pk"]}" data-counselor-name="${accountFields["name"]}">Buat jadwal</button>
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
            },
            error: async function(response) {
                var card =
                `<div class="card mt-4 mb-4 border-5 cs-rounded-border">
                    <div class="row g-0">
                        <div class="col-4 col-md-2 col-xl-3 m-3">
                            <svg width=150 height=150>
                                <use href="${get_sad_image}#sad-image"></use>
                            </svg>
                        </div>
                        <div class="col">
                            <div class="card-body">
                                <h5 class="card-title">Mohon maaf, tidak ditemukan konselor di daerah ${$("#city-select").find(":selected").text()}</h5>
                            </div>
                        </div>
                    </div>
                </div>`
                var fadeEffect = $(card).hide();
                $("#counselor-list").append(fadeEffect);
                fadeEffect.fadeIn(500);
                await sleep(100);
            }
        });
    }
});

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}