const logoutbtn = document.querySelector('.logoutbtn')
logoutbtn.addEventListener('click', function(event) {
    event.preventDefault();
    // const csrfToken = document.querySelector('meta[name="csrf-token"]').content;
    const csrfToken = getCookie('csrftoken')
    const token = localStorage.getItem('token');
    fetch('http://127.0.0.1:8000/api/v1/logout', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
                'Authorization': `Token ${token}`
            },
            credentials: 'include'
        })
        .then(response => {
            console.log(response);
            if (response.ok) {
                window.location.href = "/accounts/login/";
            }
        })
        .then(data => {
            localStorage.removeItem('token');
            console.log("out");
        })
        .catch(error => console.error('Error:', error));
})

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}