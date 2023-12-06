function search_participants() {
    let input = document.getElementById('searchbar').value.toLowerCase();
    let rows = document.getElementsByClassName('participant-row');
    
    for (let i = 0; i < rows.length; i++) {
        let showRow = false;
        let cells = rows[i].getElementsByTagName('td');
        
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