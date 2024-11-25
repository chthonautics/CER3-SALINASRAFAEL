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
    date:           "Fecha",
    forced:         "Asistencia obligatoria",
    event_type:     "Tipo de evento",
}

var editing = -1

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

// check if first is before last (YYYY-MM-DD)
// true if ordered/same day, false otherwise
function dateOrdered(first, last){
    split = {
        before: first.trim().split("-"),
        after:  last.trim().split("-")
    }

    let dates = {
        before: {
            year:   parseInt(split.before[0]),
            month:  parseInt(split.before[1]),
            day:    parseInt(split.before[2])
        },
        after: {
            year:   parseInt(split.after[0]),
            month:  parseInt(split.after[1]),
            day:    parseInt(split.after[2])
        }
    }

    return (
        dates.after.year >= dates.before.year
        && dates.after.month >= dates.before.month
        && dates.after.day >= dates.before.day
    )
}

function verify(){
    let button = document.getElementById("form-submit")
    let ids = ["id_date_start", "id_date_end"]
    let dates = {
        id_date_start: {},
        id_date_end:   {}
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
    button.disabled = !dateOrdered(document.getElementById(ids[0]).value, document.getElementById(ids[1]).value)
}

function renderEvents(data, admin, filter = 0){
    eventElement = document.getElementById("events")

    eventElement.innerHTML = ""
    
    for(let i = 0; i<data.length; i++){
        let event = data[i]
        let div = document.createElement("div")

        div.classList.add("event")
        div.classList.add("rounded")
        div.classList.add(event.forced ? "event-obligatory" : "event-optional")

        // create events
        for(let key in event){
            let element = document.createElement(key == "name" ? "h5" : "p")
            let newKey = key

            let content
            switch(key){
                case "id":
                    div.id = "event-" + event[key]
                    continue // skip cycle
                break;
                case "forced":
                    content = event.forced ? "Si" : "No"
                break;
                case "event_type":
                    content = eventTypes[event[key]-1] // off by one errors
                break;
                case "date_start":
                    if(event.date_start == event.date_end){
                        newKey = "date"
                    }
                    content = event[key]
                break;
                case "date_end":
                    if(event.date_start == event.date_end){
                        content = null
                    } else {
                        content = event[key]
                    }
                break;
                default:
                    content = event[key]
                break;
            }

            element.innerHTML = content ? (names[newKey] + ": " + content) : ""

            div.appendChild(element)
        }

        // additional behaviors if in manage panel
        if(admin){
            let modify = document.createElement("button")
            let remove = document.createElement("button")

            modify.innerHTML = "Modificar"
            remove.innerHTML = "Eliminar"

            modify.classList.add("btn")
            modify.classList.add("btn-primary")

            // modify button
            modify.onclick = function(){
                editing = div.id.split("-")[1]

                document.getElementById("title").innerHTML = "Editar evento"

                let form = document.getElementById("form")

                for(let key in event){
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

                    let element = document.getElementById("id_" + key)

                    if(element){
                        switch(element.nodeName.toLowerCase()){
                            case "textarea":
                                element.innerHTML = event[key]
                            break;
                            case "input":
                                switch(element.type){
                                    case "checkbox":
                                        element.checked = event[key]
                                    break;
                                    default:
                                        element.value = event[key]
                                    break;
                                }
                            break;
                            case "select":
                                element.selectedIndex = event[key]-1
                            break;
                            default:
                                console.log(element, event[key])
                            break;
                        }
                    }
                }

                verify()

                form.action = "/api/event/" + editing + "/"
                form.method = "put"
            }

            // remove button
            remove.onclick = function(){
                $.ajax({
                    type: "delete",
                    url: "/api/event/" + div.id.split("-")[1] + "/",
                    data: {
                        csrfmiddlewaretoken: '{{ csrf_token }}',
                    },
                    success: function (data) {
                        alert("Se ha eliminado el evento");
                        window.location.replace("/manage")
                    },
                    error: function(data){
                        switch(response.status){
                            default:
                                alert("Ha ocurrido un error")
                            break;
                        }
                    }
                });
            }

            remove.classList.add("btn")
            remove.classList.add("btn-danger")

            div.appendChild(modify)
            div.appendChild(remove)

        }

        if(filter == 0 || event.event_type == filter){
            eventElement.appendChild(div)
        }
    }
}

function renderHolidays(data) {
    for(let i = 0; i<data.length; i++){
        let event = data[i]
        let div = document.createElement("div")

        div.classList.add("event")
        div.classList.add("rounded")
        div.classList.add(event.irrenunciable == "1" ? "event-holiday-forced" : "event-holiday")

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

// auto generate filter
function genFilter(){
    let selector = document.getElementById("event-filter")

    if(selector){
        for(let i = 0; i<eventTypes.length; i++){
            let option = document.createElement("option")
        
            option.value = i+1
            option.innerHTML = eventTypes[i]
        
            selector.appendChild(option)
        }
    }
}