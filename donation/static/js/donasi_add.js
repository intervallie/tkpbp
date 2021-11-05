const alertBox = document.getElementById('alert-box')
const form = document.getElementById('p-form')

const nama = document.getElementById('id_nama')
const nominal = document.getElementById('id_nominal')
const bukti = document.getElementById('id_bukti')

const csrf = document.getElementsByName('csrfmiddlewaretoken')
console.log(csrf)

const url = ""

const handleAlerts = (type, text) => {
    alertBox.innerHTML = `<div class="alert alert-${type}" role="alert">
                            ${text}
                        </div>`
}

form.addEventListener('submit', e => {
    e.preventDefault()

    const fd = new FormData()
    fd.append('csrfmiddlewaretoken', csrf[0].value)
    fd.append('nama', nama.value)
    fd.append('nominal', nominal.value)
    fd.append('bukti', bukti.files[0])

    $.ajax({
        type: 'POST',
        url: url,
        enctype: 'multipart/form-data',
        data: fd,
        success: function(response) {
            console.log(response)
            const sText = `Berhasil menyimpan donasi. Terima kasih sudah berdonasi, TemanSinggah!`
            handleAlerts('success', sText)
        },
        error: function(error) {
            console.log(error)
            handleAlerts('danger', 'Ups.. something went wrong')
        },
        cache: false,
        contentType: false,
        processData: false,
    })
})

console.log(form)