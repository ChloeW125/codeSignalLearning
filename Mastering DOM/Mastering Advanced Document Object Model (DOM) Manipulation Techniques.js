// TODO: Get the unordered list inside the 'special-offers' div using the query selector
let offerList = document.querySelector("#special-offers ul")

// TODO: Create a new list item element
let newItem = document.createElement('li')

// TODO: Set the text content of the new element to 'Gaming Console'
newItem.textContent = 'Gaming Console'

// TODO: Append the new element to the unordered list
offerList.appendChild(newItem)