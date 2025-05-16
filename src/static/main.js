// Main JavaScript file for OptiTreasury

document.addEventListener('DOMContentLoaded', function() {
    console.log('OptiTreasury application loaded');
    
    // Handle login form submission
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            
            // In a real application, this would make an API call to authenticate
            // For now, we'll just show an alert
            alert('تم تسجيل الدخول بنجاح! مرحباً ' + username);
            
            // Redirect to dashboard (in a real app)
            // window.location.href = '/dashboard';
        });
    }
    
    // Add animation effects to cards
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px)';
            this.style.boxShadow = '0 15px 30px rgba(0, 0, 0, 0.1)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '0 5px 15px rgba(0, 0, 0, 0.05)';
        });
    });
});
