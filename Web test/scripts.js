document.addEventListener('DOMContentLoaded', () => {
    // Product list
    const products = [
        { id: 1, name: '2021 BMW 4 Series M440i xDrive G22 Auto AWD   ', imageUrl : 'image/BMW.png', price: 124500, description: 'NSW, SYD' },
        { id: 2, name: '2023 Chevrolet Corvette Stingray 3LT Auto MY23', imageUrl : 'image/Chevrolet.jpeg', price: 225600, description: 'QLD, BNE' },
        { id: 3, name: '2019 Mercedes-Benz G-Class G63 AMG Auto 4MATIC', imageUrl : 'image/AMG.jpeg', price: 305200, description: 'SA, ADL' },
        { id: 4, name: '2023 Audi RS4 Auto quattro MY23               ', imageUrl : 'image/Audi.jpeg', price: 174490, description: 'VIC, MEL' },
    ];

    // Process products
    const productContainer = document.querySelector('.product-list');
    if (productContainer) {
        products.forEach(product => {
            const productElement = document.createElement('div');
            productElement.classList.add('product-item');
            productElement.innerHTML = `
                <h3>${product.name}</h3>
                <p>${product.description}</p>
                <img class="product-image" src="${product.imageUrl}" alt="${product.name}">
                <p>Price: $${product.price}</p>
                <button data-id="${product.id}">Add to cart</button>
            `;
            productContainer.appendChild(productElement);
        });
    }

    // Add to user cart
    document.querySelectorAll('.product-item button').forEach(button => {
        button.addEventListener('click', (e) => {
            const productId = e.target.getAttribute('data-id');
            const product = products.find(p => p.id == productId);
            addToCart(product);
        });
    });

    // Processing cart
    const cartContainer = document.querySelector('.cart-items');
    const cart = JSON.parse(localStorage.getItem('cart')) || [];

    if (cartContainer) {
        renderCart(cart, cartContainer);
    }

    // Press pay button
    document.getElementById('checkout')?.addEventListener('click', () => {
        alert('Payment Success!');
        localStorage.removeItem('cart');
        renderCart([], cartContainer);
    });
});

function addToCart(product) {
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    cart.push(product);
    localStorage.setItem('cart', JSON.stringify(cart));
    alert(`${product.name} Added!`);
}

function renderCart(cart, container) {
    container.innerHTML = '';
    cart.forEach(product => {
        const cartItem = document.createElement('div');
        cartItem.innerHTML = `
            <h4>${product.name}</h4>
            <p>Price: $${product.price}</p>
        `;
        container.appendChild(cartItem);
    });
}

function toggleMenu() {
    var nav = document.querySelector('.navigation ul');
    nav.classList.toggle('show');
}