function confirmDelete(commentId) {
    console.log("Delete button clicked for comment ID:", commentId);
    if (confirm("Are you sure you want to delete this comment?")) {
        console.log("User confirmed delete for comment ID:", commentId);
        document.getElementById(`delete-comment-${commentId}`).submit();
    } else {
        console.log("User canceled delete for comment ID:", commentId);
    }
}
