async function showResult(q) {
    await fetch(`/search/${q}`)
    .then(response => response.json())
    .then(json => {
        // let table = document.getElementById('jobsTable')
        let tableBody = document.getElementById('jobs')
        tableBody.innerHTML = ''
        for (let i = 0; i < json.length; i++) {
            let row = tableBody.insertRow();
            let titleCell = row.insertCell();
            titleCell.innerHTML = `${json[i]['jobTitle']}`;
            let companyNameCell = row.insertCell();
            companyNameCell.innerHTML = `${json[i]['companyName']}`;

        }

    });

}




document.addEventListener('DOMContentLoaded', function() {
    let form = document.getElementById('searchForm')
    form.addEventListener('submit', function(event) {
        event.preventDefault()
        let q = document.getElementById('q').value

        showResult(q)
    })
});