

app.factory('LoginAPI', function ($rootScope, $http, $location) {
    console.log("Defining loginapi");

    return {
        login: function (username, password) {
            console.log("api:login:" + username + "," + password);

        }
    }
});