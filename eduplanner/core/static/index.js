function validatePassword(){ // just makes sure the password fields are equal. thats it
    let pass = document.getElementById("inputPassword")
    let repeat = document.getElementById("inputRepeat")

    let button = document.getElementById("register")

    button.disabled = pass.value != repeat.value
}

// i hate this function
// WHY IS IT ASYNC??????
// god damn promises man
async function SHA256(string){ // SHA256 encodes a string so i can use it to store passwords better
    const char = new TextEncoder().encode(string)
    const hashBuffer = await crypto.subtle.digest('SHA-256', char)
    const hashArray = Array.from(new Uint8Array(hashBuffer))

    const hashHex = hashArray.map((bytes) => bytes.toString(16).padStart(2, '0')).join('')

    return hashHex
}

function verify(){
    let button = document.getElementById("form-submit")
    let ids = ["inputDateStart", "inputDateEnd"]
    let dates = {
        inputDateStart: {},
        inputDateEnd:   {}
    } // id : { year: yyyy, month: mm, day: dd }
    let split = []

    for(let i = 0; i < ids.length; i++){
        dateString = document.getElementById(ids[i]).value
        split = dateString.trim().split("-") // turn date into array

        // input verification
        if(
            split.length != 3                           // if theres too many fields
            || split.indexOf("") != -1                  // if empty field is found
            || dateString.search(/[^0-9-]+/g) != -1     // if any non-number or separator char is present (regex)
        ){ 
            button.disabled = true
            return 
        }

        dates[ids[i]] = {
            year: parseInt(split[0]),
            month: parseInt(split[1]),
            day: parseInt(split[2])
        }

        // date range verification
        if(
            dates[ids[i]].month > 12
            || dates[ids[i]].day > 31 // doesnt check for what months have what days. oh well
            || dates[ids[i]].month < 1
            || dates[ids[i]].day < 1
        ){
            button.disabled = true
            return 
        }
    }

    // make sure the event cant end before it starts
    if(
        dates.inputDateStart.year > dates.inputDateEnd.year
        || dates.inputDateStart.month > dates.inputDateEnd.month
        || dates.inputDateStart.day > dates.inputDateEnd.day
    ){
        button.disabled = true
        return
    }

    button.disabled = false
}