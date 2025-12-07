// Toast Notification for Pending Links
(function () {
    'use strict';

    // Create toast element
    const toast = document.createElement('div');
    toast.className = 'toast-notification';
    toast.textContent = 'This article is currently being prepared. Coming soon!';
    document.body.appendChild(toast);

    let toastTimeout;

    // Function to show toast
    function showToast() {
        clearTimeout(toastTimeout);
        toast.classList.add('show');

        toastTimeout = setTimeout(function () {
            toast.classList.remove('show');
        }, 3000);
    }

    // Add click handlers to all pending links
    document.addEventListener('click', function (e) {
        const link = e.target.closest('a[href="javascript:void(0)"]');
        if (link) {
            e.preventDefault();
            showToast();
        }
    });
})();
