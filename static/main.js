$(document).ready(function () {

    // Pause the video when the modal is closed
    $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
        // Remove the src so the player itself gets removed, as this is the only
        // reliable way to ensure the video stops playing in IE
        $("#trailer-video-container").empty();
    });

    // Display a Panel containing information about a movie that was selected from the Search Results Panel.
    $(document).on('click', '.movie-search-item', function (event) {

        $('#movie-info-container').empty();
        // Retrieve Movie Information from Elements
        var movie_title = $('#searchText').val();

        var data = {
            title: $(this).attr('data-movie-title'),
            imdb_id: $(this).attr('data-movie-imdb-id'),
            poster_url: $(this).attr('data-movie-poster-url'),
            year: $(this).attr('data-movie-year')
        };

        // Send a POST request to the Server to generate the Movie Info Panel
        $.ajax({
            url: '/view',
            data: JSON.stringify(data),
            datatype: 'json',
            contentType: "application/json; charset=utf-8",
            type: 'POST',
            success: function (response) {
                $("#search").modal('hide');
                $("#movie-info-container").empty().append(response);
                $("#movieInfo").modal({
                    "backdrop": "true",
                    "keyboard": "true",
                    "show": "true"
                });
            },
            error: function (error) {
                console.log(error);
            }
        });
    });

    // The user clicks on the "Add to Favorites" button in the Movie Info View (which was created when they selected a movie from the search panel)
    $(document).on('click', '#view-add-to-favorites', function (event) {
        var data = {
            title: $(this).attr('data-title'),
            trailer_url: $(this).attr('data-trailer-url'),
            poster_url: $(this).attr('data-poster-url'),
            year: $(this).attr('data-year'),
            story: $(this).attr('data-storyline')
        }

        // Send a Request to Add the Movie to Favorites.
        $.ajax({
            url: '/add',
            data: JSON.stringify(data),
            datatype: 'json',
            contentType: "application/json; charset=utf-8",
            type: 'POST',
            success: function (response) {
                $('#view-add-to-favorites').addClass('disabled');
                $('#view-add-to-favorites').removeAttr('data-toggle');
                $('#view-add-to-favorities').val("In Favorites");
                $('#movie-list-container').empty().append(response);
            },
            error: function (error) {
                console.log(error);
            }
        });
    });

    // Show the Trailer frame when a movie tile for a favorite is clicked
    $(document).on('click', '#view-play-trailer, .movie-tile', function (event) {
        var trailerId = $(this).attr('data-trailer-url');

        $("#trailer-video-container").empty().append($("<iframe></iframe>", {
            'id': 'trailer-video',
            'type': 'text-html',
            'src': trailerId,
            'allowfullscreen': 'true',
            'webkitallowfullscreen': 'true',
            'mozallowfullscreen': 'true',
            'scrolling': 'no',
            'frameborder': 0
        }));
    });

    // Animate in the movies when the page loads
    $(document).ready(function () {
        $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
        });
    });

    // Submit a search query to find a movie by a title.
    function submitSearch() {
        var movie_title = $('#searchText').val();
        var data = {
            title: movie_title
        };

        // Post the Search query to the server
        $.ajax({
            url: '/search',
            data: JSON.stringify(data),
            datatype: 'json',
            contentType: "application/json; charset=utf-8",
            type: 'POST',
            success: function (response) {
                // Add the Generated Search Template to the Search Container
                $("#search-container").empty().append(response);

                // Enable the Modal Dialog Containing the Search Container
                $("#search").modal({
                    "backdrop": "true",
                    "keyboard": "true",
                    "show": "true"
                });
            },
            error: function (error) {
                console.log(error);
            }
        });
    }

    // Submit the Movie title contained the search Text box when enter is pressed when the text box has focus.
    $(document).on('keypress', "#searchText", function (event) {
        var keycode = (event.keyCode ? event.keyCode : event.which);

        // If the enter key was pressed
        if (keycode == '13') {
            // Submit the Search Results
            submitSearch();
        }
    });

    // or Submit the search when the submit button is clicked.
    $(document).on('click', "#search-submit", submitSearch);

});