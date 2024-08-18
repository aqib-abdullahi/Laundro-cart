const modalOverlay = document.querySelector('.checkout-preview');
const modal = document.querySelector('.checkout-box')
const closebtn = document.querySelector('.cancel-modal');
const btns = document.querySelectorAll(".btn");
const previewCountButton = document.querySelector('.preview-count');
const cancelCheckout = document.querySelector('.cancel-pay');

closebtn.onclick = function() {
    modal.style.display = "none";
    modalOverlay.style.display = "none"
}

cancelCheckout.onclick = function() {
    modal.style.display = "none";
    modalOverlay.style.display = "none"
};

modalOverlay.onclick = function() {
    modal.style.display = "none";
    modalOverlay.style.display = "none"
}

previewCountButton.onclick = function() {
    modalOverlay.style.display = "block";
    modal.style.display = "block";
    updateModal();
}

previewCountButton.disabled = true;

function updateCheckoutCounter() {
    let total = 0;
    const counters = document.querySelectorAll('.counter');

    counters.forEach(function(counter) {
        total += parseInt(counter.textContent, 10);
        if (total === 0) {
            previewCountButton.disabled = true;
        } else {
            previewCountButton.disabled = false;
        }

    });
    previewCountButton.style.setProperty("--count", `"${total}"`);
};

btns.forEach(function(button) {
    button.addEventListener("click", function(buttons) {
        const itemId = this.getAttribute("data-id");
        const counterElement = document.querySelector(`.counter[data-id="${itemId}"]`);
        let counter = parseInt(counterElement.textContent, 10);
        if (this.classList.contains('increase')) {
            counter++;
        } else if (this.classList.contains('decrease')) {
            if (counter > 0) {
                counter--;
            }
        } else {
            counter = 0;
        }
        counterElement.textContent = counter;
        updateCheckoutCounter();
    });
});

document.getElementById("defaultOpen").click()

function openTab(event, tabName) {
    var i, tabcontent, tablinks;

    tabcontent = document.getElementsByClassName('tabcontent');
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    tablinks = document.getElementsByClassName('tablinks');
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    document.getElementById(tabName).style.display = "block";
    event.currentTarget.className += " active";
}

function updateModal() {
    const basket = document.querySelector('.basket');
    basket.innerHTML = '';
    const items = document.querySelectorAll('.item');

    items.forEach(function(item) {
        const counter = item.querySelector('.counter').textContent;
        if (parseInt(counter, 10) > 0) {
            const itemName = item.querySelector('.item-name').textContent;
            const itemDescription = item.querySelector(".item-description").textContent;
            const itemPrice = item.querySelector(".item-cost").textContent;

            const checkoutItem = `
                        <div class="checkout-item">
                            <div class="checkout-details">
                                <div class="checkout-name">${itemName}</div>
                                <div class="checkout-description">${itemDescription}</div>
                                <div class="checkout-count">${counter}</div>
                                <div class="checkout-cost">${itemPrice}</div>
                            </div>
                        </div>
                    `;
            basket.innerHTML += checkoutItem;
        }
    });
}

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
const requestOrder = document.querySelector('.proceed-pay');
requestOrder.addEventListener('click', function(event) {
    event.preventDefault();
    requestOrder.disabled = true;
    const allItems = [];
    const items = document.querySelectorAll('.item');
    items.forEach(function(item) {
        const counter = item.querySelector('.counter').textContent;
        if (parseInt(counter, 10) > 0) {
            const itemId = item.querySelector('.increase').getAttribute('data-id');
            const itemName = item.querySelector('.item-name').textContent;
            const itemDescription = item.querySelector('.item-description').textContent;
            const itemPrice = item.querySelector('.item-cost').textContent;
            const itemQuantity = parseInt(counter, 10);

            allItems.push({
                id: itemId,
                name: itemName,
                description: itemDescription,
                price: itemPrice,
                quantity: itemQuantity
            });
        }
    });

    const csrfToken = getCookie('csrftoken');
    const token = getCookie('authToken');
    fetch('http://127.0.0.1:8000/api/v1/request-pickup', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
                'Authorization': `Token ${token}`
            },
            body: JSON.stringify({
                items: allItems
            }),
            credentials: 'include'
        })
        .then(response => {
            response.text()
        })
        .then(data => {
            window.location.href = '/orders/';
        })
        .catch(error => console.error('Error:', error));
});