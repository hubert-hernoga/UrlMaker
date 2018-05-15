$(document).ready(function() {

        function getCookie(c_name) {
        if (document.cookie.length > 0)
        {
            c_start = document.cookie.indexOf(c_name + "=");
            if (c_start != -1)
            {
                c_start = c_start + c_name.length + 1;
                c_end = document.cookie.indexOf(";", c_start);
                if (c_end == -1) c_end = document.cookie.length;
                return unescape(document.cookie.substring(c_start,c_end));
            }
        }
        return "";
    }

        $(function () {
        $.ajaxSetup({
            headers: { "X-CSRFToken": getCookie("csrftoken") }
        });
    });

    // Removing user from list
    $('.remove-user').click(function () {
        var current_user = $('.current-user');
        var user_id = this.id;

        var quantity_users = $('.quantity-users');

        // Removing user from list
        $.each( current_user, function(index, value) {
            if (user_id === value.id) {
                quantity_users.text(parseInt(quantity_users.text()) - 1);
                value.remove();
            }
        });

        $.ajax({
            type: "DELETE",
            url: "/",
            data: {
                "user_id": user_id
            }
        });
    });

    // Removing group from list
    $('.remove-group').click(function () {
        var current_group = $('.current-group');
        var group_id = this.id;

        var quantity_groups = $('.quantity-groups');

        // Removing group from list
        $.each( current_group, function(index, value) {
            if (group_id === value.id) {
                quantity_groups.text(parseInt(quantity_groups.text()) - 1);
                value.remove();
            }
        });

        $.ajax({
            type: "DELETE",
            url: "/groups_list/",
            data: {
                "group_id": group_id
            }
        });
    });



});