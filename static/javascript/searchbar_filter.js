function search_participants() {
    let input = document.getElementById('searchbar').value.toLowerCase();
    let rows = document.getElementsByClassName('contacts-row'); // Changed to 'contacts-row'
    
    for (let i = 0; i < rows.length; i++) {
        let showRow = false;
        let cells = rows[i].getElementsByClassName('contact-name'); // Targeting the contact-name div
        
        for (let j = 0; j < cells.length; j++) {
            let cellText = cells[j].textContent || cells[j].innerText;
            
            if (cellText.toLowerCase().includes(input)) {
                showRow = true;
                break;
            }
        }
        
        if (showRow) {
            rows[i].style.display = "";
        } else {
            rows[i].style.display = "none";
        }
    }
}
