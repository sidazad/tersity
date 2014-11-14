

'use strict';
var app = angular.module('ubernotify', ['ui.router', 'ui.bootstrap', 'ngCookies']).config(["$stateProvider", "$locationProvider", function($stateProvider, $locationProvider) {
    $stateProvider
        

.state('dashboard', {
    url: "/dashboard",
        templateUrl: '/load_template?name=dashboard.html',
        controller: "dashboardCtrl"
    })


.state('landing', {
    url: "/",
        templateUrl: '/load_template?name=landing.html',
        controller: "landingCtrl"
    })
;
    $locationProvider
            .html5Mode(true)
            .hashPrefix('!');
}]);

app.run(['$state', function ($state) {
   $state.transitionTo('landing');
}])

