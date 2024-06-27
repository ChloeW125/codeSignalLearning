document.getElementById("planet").addEventListener("click", function() {
    // TODO: In one line, create a new CustomEvent 'orbitCompleted' with a detail indicating a message and dispatch it
    let orbit = new CustomEvent("orbitCompleted", {detail: {message: "Orbit has been completed!",}});
    document.getElementById("planet").dispatchEvent(orbit);
});
// TODO: Add a listener for 'orbitCompleted' to alert the message from the event detail
document.getElementById("planet").addEventListener("orbitCompleted", function(e) {
    alert(e.detail.message);
})