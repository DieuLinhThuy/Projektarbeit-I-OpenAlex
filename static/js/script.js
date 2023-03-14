var selectedRow = null;

//Show Alerts
function showAlert(message, className){
    const div = document.createElement("div");
    div.className = `alert alert-${className}`;

    div.appendChild(document.createTextNode(message));
    const container = document.querySelector(".container");
    const main = document.querySelector(".main");
    container.insertBefore(div, main);

    setTimeout(() => document.querySelector(".alert").remove(), 3000);
};

// Clear All Fields
// function clearFields(){
    // document.querySelector("#").value = "";
    //document.querySelector("#").value = "";
///}

// Add Data
document.querySelector("#campaign-form").addEventListener("submit", (e) =>{
    e.preventDefault();

    // Get Form Values
    const name = documentquerySelector("#name").value;
    const number = documentquerySelector("#number").value;
    const country = documentquerySelector("#country").value;
    const k_number = documentquerySelector("#k_number").value;
    const country_abbrev = documentquerySelector("#country_abbrev").value;
    const region = documentquerySelector("#region").value;
    const source = documentquerySelector("#source").value;
    const source_abbrev = documentquerySelector("#source_abbrev").value;

    //validate
    if(name == "" || number == "" || country == ""){
        showAlert("Please fill in all fields", "danger");
    }
    else{
        if(selectedRow == null){
            const list = document.querySelector("#campaign-list");
            const row = document.createComment("tr");

            row.innerHTML = `
                <th>${Kampagne}</th>
                <th>${Kampagnennummer}</th>
                <th>${K-Nummer}</th>
                <th>${Länderkürzel}</th>
                <th>${Region}</th>
                <th>${Quelle}</th>
                <th>${Quellenkürzel}</th>
                <td>
                    <a href="#" class="btn btn-warning btn-sm edit">Edit</a>
                    <a href="#" class="btn btn-warning btn-sm edit">Delete</a>
                `;
            list.appendChild(row);
            selectedRow = null;
            showAlert("Added", "success");

        }
    }
});

// Delete Data

document.querySelector("#campaign-list", "#utm-list").addEventListener("click", (e) =>{
    target = e.target;
    if(target.classList.contains("delete")){
        target.parentElement.parentElement.remove();
        showAlert("Data Deleted", "danger");
    }
});

document.querySelector("#utm-list").addEventListener("click", (e) =>{
    target = e.target;
    if(target.classList.contains("delete")){
        target.parentElement.parentElement.remove();
        showAlert("Data Deleted", "danger");
    }
});

document.addEventListener("DOMContentLoaded", function(){
    // make it as accordion for smaller screens
    if (window.innerWidth > 992) {

        document.querySelectorAll('.navbar .nav-item').forEach(function(everyitem){

            everyitem.addEventListener('mouseover', function(e){

                let el_link = this.querySelector('a[data-bs-toggle]');

                if(el_link != null){
                    let nextEl = el_link.nextElementSibling;
                    el_link.classList.add('show');
                    nextEl.classList.add('show');
                }

            });
            everyitem.addEventListener('mouseleave', function(e){
                let el_link = this.querySelector('a[data-bs-toggle]');

                if(el_link != null){
                    let nextEl = el_link.nextElementSibling;
                    el_link.classList.remove('show');
                    nextEl.classList.remove('show');
                }


            })
        });

    }
    // end if innerWidth
    });
