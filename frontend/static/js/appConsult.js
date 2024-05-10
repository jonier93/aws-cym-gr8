function consult_user() {
    let id = document.getElementById("id").value
    let obj_id = {"id": id}
    fetch('/consult_user', {
        "method":"post",
        "headers":{"content-type":"application/json"},
        "body": JSON.stringify(obj_id)
    })
    .then(resp => resp.json())
    .then(data => {
        if (data.status == "ok") {
            obj_data = data.name + " " + data.lastname + " " + data.birthday
            document.getElementById("txt_data").value = obj_data
        }
        else {
            alert("The user was not found")
        }
    })
    .catch(err => alert(err))
}