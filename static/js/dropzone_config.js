
Dropzone.autoDiscover = false;

var csvDropzone = new Dropzone('#csv-dropzone', {
    paramName: 'file',
    maxFiles: 1,
    maxFilesize: 5,
    acceptedFiles: '.csv,.xlsx,.xls,.pdf',
    addRemoveLinks: true,
    dictRemoveFile: 'Usuń',
    headers: {
        'X-CSRFToken': document.querySelector('#csv-dropzone').dataset.csrf
    },
    dictDefaultMessage: 'Przeciągnij plik CSV lub Excel tutaj lub kliknij',
    dictFileTooBig: 'Plik za duży (max 5MB)',
    dictInvalidFileType: 'Dozwolone: CSV, XLSX, XLS, PDF',
    dictMaxFilesExceeded: 'Możesz wgrać tylko jeden plik',

    success: function(file, response) {
        console.log(response)
        file.previewElement.classList.add('dz-success');
        renderImportResult(response);
    },

    error: function(file, message) {
    file.previewElement.classList.add('dz-error');
    document.getElementById('import-error').style.display = 'block';
    document.getElementById('import-error-message').textContent =
        'Błąd: podczas wgrywania pliku';
}
});

function renderImportResult(response) {
    document.getElementById('import-result').style.display = 'block';
    document.getElementById('import-summary').textContent =
        'Dodano: ' + response.imported + ', pominięto: ' + response.skipped;

    const tbody = document.getElementById('import-table-body');
    tbody.innerHTML = '';

    response.transactions.forEach(function(t) {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${t.data}</td>
            <td>${t.nazwa}</td>
            <td>${t.opis}</td>
            <td>${t.kategoria}</td>
            <td>${t.kwota} zł</td>
            <td>${t.typ === 'expense' ? 'Wydatek' : 'Przychód'}</td>
        `;
        tbody.appendChild(row);
    });
}
