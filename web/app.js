app = angular.module('IttyBittyNote', [ 'ngRoute', 'ngMaterial', 'ngMdIcons']);
api_root = 'http://127.0.0.1:9000'

app.config(function($routeProvider, $locationProvider, $mdThemingProvider) {
	$routeProvider.when("/note/list", {
		templateUrl : 'views/note_list.html',
		controller: 'noteController'
	}).when("/note/add", {
		templateUrl : 'views/note_add.html',
		controller: 'deployController',
		title: 'Deploy Controller'
	}).otherwise({
		redirectTo: '/note/list'
	})
});

angular.module('IttyBittyNote')