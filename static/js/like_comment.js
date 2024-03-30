/* jshint esversion: 6 */

$(document).ready(function() {
    $(".like-comment-btn").click(function() {
        var comment_id = $(this).data("comment-id");
        
        $.ajax({
            type: "POST",
            url: "/reviews/like_comment/",
            data: {
                comment_id: comment_id,
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
            },
            dataType: "json",
            success: function(response) {
                if (response.liked) {
                    alert("Comment liked!");
                } else {
                    alert("Comment unliked!");
                }
                
                $("#likes-count-" + comment_id).text(response.likes_count);
            },
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
                alert("An error occurred. Please try again.");
            }
        });
    });
});
