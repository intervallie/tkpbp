const threadsElement = document.getElementById("threads")

const xhr = new XMLHttpRequest()
const method = 'GET'
const url = "/threads"
const responseType = "json"

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