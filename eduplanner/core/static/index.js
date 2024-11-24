let eventTypes = [
    "Inicio de Semestre",
    "Fin de Semestre", 
    "Inicio de Inscripción de Asignaturas", 
    "Fin de Inscripción de Asignaturas", 
    "Receso Académico", 
    "Inicio de Plazos de Solicitudes Administrativas",
    "Fin de Plazos de Solicitudes Administrativas", 
    "Inicio de Plazos para la Gestión de Beneficios", 
    "Fin de Plazos para la Gestión de Beneficios", 
    "Ceremonia de Titulación o Graduación", 
    "Reunión de Consejo Académico", 
    "Talleres y Charlas", 
    "Día de Orientación para Nuevos Estudiantes", 
    "Eventos Extracurriculares", 
    "Inicio de Clases", 
    "Último Día de Clases", 
    "Día de Puertas Abiertas", 
    "Suspensión de Actividades Completa", 
    "Suspensión de Actividades Parcial", 
]

let names = {
    name:           "Nombre",
    description:    "Descripción",
    date_start:     "Fecha de inicio",
    date_end:       "Fecha de término",
    forced:         "Asistencia obligatoria",
    event_type:     "Tipo de evento",
}

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

function renderEvents(data){
    for(let i = 0; i<data.length; i++){
        let event = data[i]
        let div = document.createElement("div")

        div.classList.add("event")
        div.classList.add("rounded")
        div.classList.add(event.forced ? "event-obligatory" : "event-optional")

        for(let key in event){
            let element = document.createElement(key == "name" ? "h5" : "p")

            let content
            switch(key){
                case "forced":
                    content = event.forced ? "Si" : "No"
                break;
                case "event_type":
                    content = eventTypes[event[key]-1] // off by one errors
                break;
                default:
                    content = event[key]
                break;
            }

            // ternary operators replace true and false with yes and no
            element.innerHTML = names[key] + ": " + content
            div.appendChild(element)
        }

        document.getElementById("events").appendChild(div)
    }
}

function renderHolidays(data) {
    for(let i = 0; i<data.length; i++){
        let event = data[i]
        let div = document.createElement("div")

        div.classList.add("event")
        div.classList.add("rounded")
        div.classList.add(event.irrenunciable == "1" ? "event-holiday-forced" : "event-holiday")

        console.log(event, event.irrenunciable)

        for(let key in event){
            let element = document.createElement(key == "nombre" ? "h5" : "p")

            // replace 0 and 1 with yes and no
            let forced = event[key] == 1 ? "Si" : "No"
            let capKey = key.charAt(0).toUpperCase() + key.slice(1)

            // ternary checks if its a number (forced holiday)
            element.innerHTML = capKey + ": " + (isNaN(event[key]) ? event[key] : forced)
            div.appendChild(element)
        }

        document.getElementById("holidays").appendChild(div)
    }
}