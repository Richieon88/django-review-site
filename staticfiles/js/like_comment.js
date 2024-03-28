$(document).ready(function() {
    $(".like-btn").click(function() {
        var commentId = $(this).data("comment-id");
        var url = `/reviews/like_comment/${commentId}/`;

        $.ajax({
            url: url,
            type: "POST",
            data: {
                csrfmiddlewaretoken: "{{ csrf_token }}"
            },
            success: function(response) {
                if (response.liked) {
                    $("#comment-" + commentId + " .like-btn").text("Unlike");
                } else {
                    $("#comment-" + commentId + " .like-btn").text("Like");
                }
                $("#comment-" + commentId + " .like-count").text(response.likes_count);
            },
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    });
});