

app.factory('LoginAPI', ["$rootScope", "$http", "$location", "$cookies", "$state", function ($rootScope, $http, $location, $cookies, $state) {
    console.log("Defining loginapi");

    return {
        login: function (username, password, loginurl, redirect_state) {
            console.log("api:login:" + username + "," + password);

            if(loginurl !== undefined && loginurl !== null && loginurl !== "") {
                // if a login url has been provided
                $http.defaults.headers.post['X-CSRFToken'] = $cookies['csrftoken']
                $http.post(loginurl, {username: username, password: password}).success(function(data) {
                    console.log(data);
                    if(data.status === "ok") {
                        console.log("result ok: redirecting")
                        $state.go(redirect_state);
                    }

                });

            }

        }
    }
}]);

