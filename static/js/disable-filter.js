const yearSelect = document.getElementById('select-year');
const monthSelect = document.getElementById('select-month');

function toggleMonth() {
    if (yearSelect.value) {
        monthSelect.disabled = false;
        monthSelect.style.opacity = '1';
    } else {
        monthSelect.disabled = true;
        monthSelect.style.opacity = '0.5';
    }
}

// sprawdź przy załadowaniu strony (zachowanie po filtracji)
toggleMonth();

// sprawdzaj przy każdej zmianie roku
yearSelect.addEventListener('change', function() {
    if (!yearSelect.value) {
        monthSelect.value = '';
    }
    toggleMonth();
});