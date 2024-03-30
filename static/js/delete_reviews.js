/* jshint esversion: 6 */

document.addEventListener('DOMContentLoaded', function () {
    const deleteReviewBtns = document.querySelectorAll('.delete-review-btn');

    deleteReviewBtns.forEach(button => {
        button.addEventListener('click', function (e) {
            e.preventDefault();

            const reviewId = this.getAttribute('data-review-id');

            const isConfirmed = confirm('Are you sure you want to delete this review?');
            if (isConfirmed) {
                const form = this.parentElement;
                form.submit();
            }
        });
    });
});