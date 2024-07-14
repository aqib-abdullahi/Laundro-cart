document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('.signupForm');
    const firstName = document.getElementById('firstname');
    const lastName = document.getElementById('lastname');
    const email = document.getElementById('email');
    const password1 = document.getElementById('password1');
    const password2 = document.getElementById('password2');

    form.addEventListener('submit', e => {
        e.preventDefault();
        if (validate()) {
            form.submit();
        }
    });

    const setErrorMessage = (element, message) => {
        const inputControl = element.parentElement;
        const errorDisplay = inputControl.querySelector('.error');

        if (errorDisplay) {
            errorDisplay.innerText = message;
            inputControl.classList.add('error');
            inputControl.classList.remove('success');
        }
    };

    const setSuccessMessage = element => {
        const inputControl = element.parentElement;
        const errorDisplay = inputControl.querySelector('.error');

        if (errorDisplay) {
            errorDisplay.innerText = '';
            inputControl.classList.add('success');
            inputControl.classList.remove('error');
        }
    };

    const validate = () => {
        const firstNameValue = firstName.value.trim();
        const lastNameValue = lastName.value.trim();
        const emailValue = email.value.trim();
        const password1Value = password1.value.trim();
        const password2Value = password2.value.trim();

        let isValid = true;

        if (firstNameValue === '') {
            setErrorMessage(firstName, 'First name is required');
            isValid = false;
        } else {
            setSuccessMessage(firstName);
        }
        if (lastNameValue === '') {
            setErrorMessage(lastName, 'Last name is required');
            isValid = false;
        } else {
            setSuccessMessage(lastName);
        }
        if (emailValue === '') {
            setErrorMessage(email, 'Email is required');
            isValid = false;
        } else {
            setSuccessMessage(email);
        }

        if (password1Value === '') {
            setErrorMessage(password1, 'Password is required');
            isValid = false;
        } else if (password1Value.length < 8) {
            setErrorMessage(password1, 'Password must be at least 8 characters.');
            isValid = false;
        } else {
            setSuccessMessage(password1);
        }

        if (password2Value === '') {
            setErrorMessage(password2, 'Please confirm your password');
            isValid = false;
        } else if (password2Value !== password1Value) {
            setErrorMessage(password2, 'Passwords do not match');
            isValid = false;
        } else {
            setSuccessMessage(password2);
        }

        return isValid;
    };
});
