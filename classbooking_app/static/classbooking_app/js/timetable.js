document.addEventListener("DOMContentLoaded", function(){
    // Declare const variables
    const currentDate = document.getElementById("select-date")
    const form = document.getElementById("date-form")
    const cart = document.getElementById("cart")
    const remove = document.getElementById("remove")
    const dateChange = document.getElementById("date-change")
    const addBoxes = document.getElementsByClassName("add-to-cart")
    const cancelledSessBtns = document.getElementsByClassName("run-False-btn")
    const dateHeaders = document.getElementsByClassName("date-header")
    
    let dateArr = []
    for (let header of dateHeaders){
        dateArr.push(header.id)
    }
    
    document.getElementById(dateArr[0]).classList.remove("invisible")
    for (let i=1;i<dateArr.length;i++){
        if (dateArr[i].substring(1,6) != dateArr[i-1].substring(1,6)){
            document.getElementById(dateArr[i]).classList.remove("invisible")
        }

    }

    for (let button of cancelledSessBtns){
        button.value = "Class Cancelled"
    }

    let confBookings = document.getElementById("confirmed-bookings").children
    let confBookingsArr = []
    for (let booking of confBookings){
        confBookingsArr.push(booking.innerHTML)
    }

    let unconfBookings = document.getElementById("unconfirmed-bookings").children
    let unconfBookingsArr = []
    for (let booking of unconfBookings){
        unconfBookingsArr.push(booking.innerHTML)
    }
    
    // Add event listener on date input to convert date into serial number
    currentDate.addEventListener("change", () => {
        dateChange.value = "y"
        form.submit()
    })

    // Add event listener to each add to cart button
    for (let box of addBoxes){
        if (box.value != "Class Cancelled"){
            if (unconfBookingsArr.includes(box.id)){
                box.value = "Remove from Cart"
            } else if (confBookingsArr.includes(box.id)){ 
                box.value = "Booked in. Cancel?"
            } else {
                box.value = "Add to Cart"
            }
            box.addEventListener("click", () => {
                    if (confBookingsArr.includes(box.id) || unconfBookingsArr.includes(box.id)){
                        remove.value = box.id
                    } else {
                        cart.value = box.id
                    }
                    // Submit form
                    form.submit()
            })
        }
    }
})