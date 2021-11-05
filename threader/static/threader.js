function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

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
        } else if (xhr.status === 403) {
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
        var listedItems = serverResponse
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

function handleThreadActionButton(thread_id, currentCount, action) {
    console.log(thread_id, currentCount)
    const url = "/action"
    const method = "POST"
    const data = JSON.stringify({
        id: thread_id,
        action: action
    })
    const xhr = new XMLHttpRequest()
    const csrftoken = getCookie('csrftoken');
    xhr.open(method, url)
    xhr.setRequestHeader("Content-Type", "application/json")
    xhr.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest")
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest")
    xhr.setRequestHeader("X-CSRFToken", csrftoken)
    xhr.onload = function() {
        loadThreads(threadsContainerElement)
    }
    xhr.send(data)
    return
}
function likeButton(thread) {
    return "<button class='btn btn-primary btn-sm' onclick=handleThreadActionButton(" +
    thread.id + "," + thread.likes + ",'like')>" + thread.likes + "Like</button>"
}
function unlikeButton(thread) {
    return "<button class='btn btn-outline-primary btn-sm' onclick=handleThreadActionButton(" +
    thread.id + "," + thread.likes + ",'unlike')>Unlike</button>"
}
function retweetButton(thread) {
    return "<button class='btn btn-outline-success btn-sm' onclick=handleThreadActionButton(" +
    thread.id + "," + thread.likes + ",'retweet')>Retweet</button>"
}
function formatThreadElement(thread) {
    var formattedThread = "<div class='mb-4 thread' id='thread-" + thread.id
    + "'><p>" + thread.content +
        "</p><div class='btn-group'>" +
            likeButton(thread) +
            unlikeButton(thread) +
            retweetButton(thread) +
        "</p></div>"
    return formatThread
}