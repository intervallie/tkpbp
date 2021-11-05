function handleThreadFormError(msg, display) {
    var myErrorDiv = document.getElementById("thread-create-form-error")
    if (display === true) {
        myErrorDiv.setAttribute("class", "d-block alert alert-danger")
        myErrorDiv.innerText = msg
    } else {
        myErrorDiv.setAttribute("class", "d-none alert alert-danger")
    }
}

function handleThreadCreateFormDidSubmit(event) {
    event.preventDefault()
    const myForm = event.target
    const myFormData = new FormData(myForm)
    const url = myForm.getAttribute("action")
    const method = myForm.getAttribute("method")
    const xhr = new XMLHttpRequest()
    const responseType = "json"
    xhr.responseType = responseType
    xhr.open(method, url)
    xhr.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest")
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest")
    xhr.onload = function() {
        if (xhr.status === 201) {
            handleThreadFormError("", false)
            const newThreadJson = xhr.response
            const newThreadElement = formatThreadElement(newThreadJson)
            const ogHtml = threadsContainerElement.innerHTML
            threadsContainerElement.innerHTML = newThreadElement + ogHtml
            myForm.reset()
        } else if (xhr.status === 400) {
            const errorJson = xhr.response
            const contentError = errorJson.content
            let contentErrorMsg;
            if (contentError) {
                contentErrorMsg = contentError[0]
                if (contentErrorMsg) {
                    handleThreadFormError(contentErrorMsg, true)
                } else {
                    alert("An error occured. Please try again.")
                }
            } else {
                alert("An error occured. Please try again.")
            }
        } else if (xhr.status === 401) {
            alert("You must login!")
            window.location.href = "/login"
        } else if (xhr.status === 500) {
            alert("There was a server error, please try again.")
        }
    }
    xhr.onerror = function() {
        alert("An error occured. Please try again later.")
    }
    xhr.send(myFormData)
}
const threadCreateFormEl = document.getElementById("thread-create-form")
threadCreateFormEl.addEventListener("submit", handleThreadCreateFormDidSubmit)

const threadsContainerElement = document.getElementById("threads")

function loadThreads(threadsElement) {
    const xhr = new XMLHttpRequest()
    const method = 'GET'
    const url = "/threads"
    const responseType = "json"

    xhr.responseType = responseType
    xhr.open(method, url)
    xhr.onload = function() {
        const serverResponse = xhr.response
        var listedItems = serverResponse.response
        var finalThreadStr = ""
        var i;
        for (i = 0; i < listedItems.length; i++) {
            var threadObj = listedItems[i]
            var currentItem = formatThreadElement(threadObj)
            finalThreadStr += currentItem
        }
    }
    xhr.send()
}

loadThreads(threadsContainerElement)

function handleDidLike(thread_id, currentCount) {
    console.log(thread_id, currentCount)
}
function likeButton(thread) {
    return "<button class='button btn-sm' onclick=handleDidLike(" +
    thread.id + "," + thread.likes + ")>" + thread.likes + "Like</button>"
}
function formatThreadElement(thread) {
    var formattedThread = "<div class='mb-4 thread' id='thread-" + thread.id
    + "'><p>" + thread.content +
        "</p><div class='btn-group'>" + likeButton(thread) +
        "</p></div>"
    return formatThread
}