// Global Trust Bank - JavaScript functionality

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    initializeBank();
});

function initializeBank() {
    // Add security indicators
    addSecurityIndicators();
    
    // Initialize tooltips
    initializeTooltips();
    
    // Add loading states to forms
    addFormLoadingStates();
    
    // Simulate real-time updates
    if (window.location.pathname === '/dashboard') {
        startRealTimeUpdates();
    }
    
    // Add keyboard shortcuts
    addKeyboardShortcuts();
}

function addSecurityIndicators() {
    // Add security badges to sensitive areas
    const sensitiveElements = document.querySelectorAll('input[type="password"], input[name="account_number"], input[name="routing"]');
    
    sensitiveElements.forEach(element => {
        const parent = element.parentNode;
        if (!parent.querySelector('.security-indicator')) {
            const indicator = document.createElement('div');
            indicator.className = 'security-indicator text-success small mt-1';
            indicator.innerHTML = '<i class="fas fa-shield-alt me-1"></i>Protected with 256-bit encryption';
            parent.appendChild(indicator);
        }
    });
}

function initializeTooltips() {
    // Initialize Bootstrap tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}

function addFormLoadingStates() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn && !submitBtn.classList.contains('no-loading')) {
                addLoadingState(submitBtn);
            }
        });
    });
}

function addLoadingState(button) {
    if (button.dataset.originalText) return; // Already has loading state
    
    button.dataset.originalText = button.innerHTML;
    button.disabled = true;
    
    const spinner = '<span class="spinner-border spinner-border-sm me-2"></span>';
    const text = button.textContent.replace(/Sign In|Transfer|Send|Submit/i, function(match) {
        return match === 'Sign In' ? 'Signing In...' :
               match === 'Transfer' ? 'Processing...' :
               match === 'Send' ? 'Sending...' :
               match === 'Submit' ? 'Submitting...' : 'Processing...';
    });
    
    button.innerHTML = spinner + text;
}

function startRealTimeUpdates() {
    // Simulate real-time balance updates (for realism)
    setInterval(() => {
        updateLastActivity();
    }, 30000); // Update every 30 seconds
    
    // Add random "security checks" notifications
    setTimeout(() => {
        showSecurityNotification();
    }, Math.random() * 60000 + 30000); // Random between 30-90 seconds
}

function updateLastActivity() {
    const now = new Date();
    const timeString = now.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
    
    // Update any "last activity" displays
    const activityElements = document.querySelectorAll('.last-activity');
    activityElements.forEach(element => {
        element.textContent = `Last activity: Today at ${timeString}`;
    });
}

function showSecurityNotification() {
    const notifications = [
        'Security scan completed - No threats detected',
        'Account monitoring active - All transactions verified',
        'Login attempt verified from your location',
        'Automatic backup completed successfully'
    ];
    
    const randomNotification = notifications[Math.floor(Math.random() * notifications.length)];
    
    const toast = document.createElement('div');
    toast.className = 'toast align-items-center text-white bg-success border-0 position-fixed';
    toast.style.cssText = 'top: 20px; right: 20px; z-index: 9999;';
    toast.setAttribute('role', 'alert');
    toast.innerHTML = `
        <div class="d-flex">
            <div class="toast-body">
                <i class="fas fa-shield-check me-2"></i>${randomNotification}
            </div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
        </div>
    `;
    
    document.body.appendChild(toast);
    const bsToast = new bootstrap.Toast(toast, { delay: 5000 });
    bsToast.show();
    
    toast.addEventListener('hidden.bs.toast', function() {
        document.body.removeChild(toast);
    });
    
    // Schedule next notification
    setTimeout(() => {
        showSecurityNotification();
    }, Math.random() * 300000 + 300000); // Random between 5-10 minutes
}

function addKeyboardShortcuts() {
    document.addEventListener('keydown', function(e) {
        // Alt + D for Dashboard
        if (e.altKey && e.key === 'd') {
            e.preventDefault();
            const dashboardLink = document.querySelector('a[href*="dashboard"]');
            if (dashboardLink) dashboardLink.click();
        }
        
        // Alt + T for Transfer
        if (e.altKey && e.key === 't') {
            e.preventDefault();
            const transferLink = document.querySelector('a[href*="transfer"]');
            if (transferLink) transferLink.click();
        }
        
        // Alt + S for Statements
        if (e.altKey && e.key === 's') {
            e.preventDefault();
            const statementsLink = document.querySelector('a[href*="statements"]');
            if (statementsLink) statementsLink.click();
        }
        
        // Escape to clear forms
        if (e.key === 'Escape') {
            const activeModal = document.querySelector('.modal.show');
            if (activeModal) {
                bootstrap.Modal.getInstance(activeModal).hide();
            }
        }
    });
}

// Utility functions for enhanced realism

function formatCurrency(amount) {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD'
    }).format(amount);
}

function formatAccountNumber(accountNumber) {
    return accountNumber.replace(/(\d{4})/g, '$1-').slice(0, -1);
}

function validateAccountNumber(accountNumber) {
    // Basic validation for demo purposes
    const cleaned = accountNumber.replace(/[-\s]/g, '');
    return /^\d{10,16}$/.test(cleaned);
}

function validateRoutingNumber(routingNumber) {
    // Basic validation for demo purposes
    const cleaned = routingNumber.replace(/[-\s]/g, '');
    return /^\d{9}$/.test(cleaned);
}

function generateTransactionId() {
    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    let result = 'GTB';
    for (let i = 0; i < 8; i++) {
        result += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    return result;
}

function simulateNetworkDelay(min = 1000, max = 3000) {
    return new Promise(resolve => {
        const delay = Math.random() * (max - min) + min;
        setTimeout(resolve, delay);
    });
}

// Enhanced form validation
function enhanceFormValidation() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        const inputs = form.querySelectorAll('input[required]');
        
        inputs.forEach(input => {
            input.addEventListener('blur', function() {
                validateField(this);
            });
            
            input.addEventListener('input', function() {
                if (this.classList.contains('is-invalid')) {
                    validateField(this);
                }
            });
        });
    });
}

function validateField(field) {
    const value = field.value.trim();
    let isValid = true;
    let message = '';
    
    // Basic required validation
    if (field.hasAttribute('required') && !value) {
        isValid = false;
        message = 'This field is required';
    }
    
    // Specific validations
    if (field.name === 'account_number' && value) {
        if (!validateAccountNumber(value)) {
            isValid = false;
            message = 'Please enter a valid account number (10-16 digits)';
        }
    }
    
    if (field.name === 'routing' && value) {
        if (!validateRoutingNumber(value)) {
            isValid = false;
            message = 'Please enter a valid 9-digit routing number';
        }
    }
    
    if (field.type === 'email' && value) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(value)) {
            isValid = false;
            message = 'Please enter a valid email address';
        }
    }
    
    // Update field appearance
    if (isValid) {
        field.classList.remove('is-invalid');
        field.classList.add('is-valid');
        removeFieldError(field);
    } else {
        field.classList.remove('is-valid');
        field.classList.add('is-invalid');
        showFieldError(field, message);
    }
    
    return isValid;
}

function showFieldError(field, message) {
    removeFieldError(field);
    
    const errorDiv = document.createElement('div');
    errorDiv.className = 'invalid-feedback';
    errorDiv.textContent = message;
    
    field.parentNode.appendChild(errorDiv);
}

function removeFieldError(field) {
    const existingError = field.parentNode.querySelector('.invalid-feedback');
    if (existingError) {
        existingError.remove();
    }
}

// Initialize enhanced features when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    enhanceFormValidation();
});

// Export functions for global use
window.BankUtils = {
    formatCurrency,
    formatAccountNumber,
    validateAccountNumber,
    validateRoutingNumber,
    generateTransactionId,
    simulateNetworkDelay
};
