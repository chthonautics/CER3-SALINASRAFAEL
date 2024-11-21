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