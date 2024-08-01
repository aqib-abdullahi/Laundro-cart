const logoutbtn = document.querySelector('.logoutbtn')
logoutbtn.addEventListener('click', function(event) {
    event.preventDefault();
    const csrfToken = document.querySelector('meta[name="csrf-token"]').content;
    const token = localStorage.getItem('token');
    fetch('http://127.0.0.1:8000/api/v1/logout', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
                'Authorization': `Token ${token}`
            },
            credentials: 'same-origin'
        })
        .then(response => {
            console.log(response);
            if (response.ok) {
                window.location.href = "/accounts/login/";
                localStorage.removeItem('token');
            }
        })
        .then(data => {})
        .catch(error => console.error('Error:', error));
})