const form = document.querySelector('form');
const firstName = document.getElementById('firstname');
const lastName = document.getElementById('lastname');
const email = document.getElementById('email');
const password1 = document.getElementById('password1');
const password2 = document.getElementById('password2');

form.addEventListener('submit', (e) => {
    e.preventDefault();
    validate();
});

const setErrorMessage = (element, message) => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = message;
    inputControl.classList.add('error');
};

const setSuccessMessage = (element) => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = '';
    inputControl.classList.add('success');
    inputControl.classList.remove('error');
};

const validate = () => {
    const firstNameValue = firstName.value.trim();
    const lastNameValue = lastName.value.trim();
    const emailValue = email.value.trim();
    const password1Value = password1.value.trim();
    const password2Value = password2.value.trim();

    if (firstNameValue === '') {
        setErrorMessage(firstName, 'First name is required');
    } else {
        setSuccessMessage(firstName);
    }
    if (lastNameValue === '') {
        setErrorMessage(lastName, 'Last name is required');
    } else {
        setSuccessMessage(lastName);
    }
    if (emailValue === '') {
        setErrorMessage(email, 'Email is required');
    } else {
        setSuccessMessage(email);
    }

    if (password1Value === '') {
        setErrorMessage(password1, 'Password is required');
    } else if (password1Value.length < 8) {
        setErrorMessage(password1, 'Password must be at least 8 characters (alphanumerics).');
    } else {
        setSuccessMessage(password1);
    }

    if (password2Value === '') {
        setErrorMessage(password2, 'Please confirm your password');
    } else if (password2Value !== password1Value) {
        setErrorMessage(password2, 'Passwords doesn\'t match');
    } else {
        setSuccessMessage(password2);
    }
};