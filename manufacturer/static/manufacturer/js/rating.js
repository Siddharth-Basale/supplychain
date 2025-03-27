document.addEventListener('DOMContentLoaded', function() {
    // Handle star rating clicks
    document.querySelectorAll('.rating-stars').forEach(container => {
        const stars = container.querySelectorAll('.star');
        const supplierId = container.dataset.supplierId;
        const currentRating = parseInt(container.dataset.currentRating) || 0;
        
        // Highlight stars based on current rating
        highlightStars(stars, currentRating);
        
        // Add click event for each star
        stars.forEach((star, index) => {
            star.addEventListener('click', () => {
                const rating = index + 1;
                submitRating(supplierId, rating, container);
            });
            
            // Add hover effect
            star.addEventListener('mouseover', () => {
                highlightStars(stars, index + 1);
            });
            
            star.addEventListener('mouseout', () => {
                highlightStars(stars, currentRating);
            });
        });
    });
});

function highlightStars(stars, rating) {
    stars.forEach((star, index) => {
        if (index < rating) {
            star.classList.add('active');
        } else {
            star.classList.remove('active');
        }
    });
}

function submitRating(supplierId, rating, container) {
    fetch(`/manufacturer/rate-supplier/${supplierId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: `rating=${rating}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            container.dataset.currentRating = data.rating;
            highlightStars(container.querySelectorAll('.star'), data.rating);
        }
    });
}

// Helper function to get CSRF token
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