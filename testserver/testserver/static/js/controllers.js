
app.controller('dashboardCtrl', ["$scope", 'LoginAPI', function ($scope, LoginAPI) {

    console.log("dashboardCtrl");

    $scope.model = {

    };

    

}]);

app.controller('landingCtrl', ["$scope", 'LoginAPI', function ($scope, LoginAPI) {

    console.log("landingCtrl");

    $scope.model = {

    };

    

        
$scope.on_login = function() {
    console.log("on_login: the real deal");
    LoginAPI.login("a", "b", "/login_user", "dashboard");

}


            


}]);
