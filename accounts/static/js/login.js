const loginForm = document.querySelector('form');
loginForm.addEventListener('submit', async(event) => {
    event.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const csrfToken = document.querySelector('meta[name="csrf-token"]').content;
    try {
        const response = await fetch('http://127.0.0.1:8000/api/v1/token/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
                'Authorization': 'Basic ' + btoa(email + ':' + password),
            },
            body: JSON.stringify({
                Email: email,
                Password: password
            }),
            credentials: 'same-origin'
        });

        const data = await response.json();

        if (response.ok) {
            const token = data.token;
            localStorage.setItem('token', token);
            if (data.SuperRole) {} else {
                window.location.href = '/dashboard/';
            }
        } else {
            console.error('Error:', data);
        }
    } catch (error) {
        console.error('Error:', error);
    }
});

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