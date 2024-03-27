document.addEventListener('DOMContentLoaded', function () {
    // Get all delete review buttons
    const deleteReviewBtns = document.querySelectorAll('.delete-review-btn');

    // Add event listener to each delete review button
    deleteReviewBtns.forEach(button => {
        button.addEventListener('click', function (e) {
            // Prevent the default form submission
            e.preventDefault();

            // Get the review ID from the data attribute
            const reviewId = this.getAttribute('data-review-id');

            // Ask for confirmation before deleting
            const isConfirmed = confirm('Are you sure you want to delete this review?');
            if (isConfirmed) {
                // If confirmed, submit the form
                const form = this.parentElement;
                form.submit();
            }
        });
    });
});