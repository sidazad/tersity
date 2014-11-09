

'use strict';
var app = angular.module('ubernotify', ['ui.router', 'ui.bootstrap']).config(["$stateProvider", "$locationProvider", function($stateProvider, $locationProvider) {
    $stateProvider
        

.state('dashboard', {
    url: "/dashboard",
        templateUrl: '/templates/dashboard.html',
        controller: "dashboardCtrl"
    })


.state('landing', {
    url: "/",
        templateUrl: '/templates/landing.html',
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

