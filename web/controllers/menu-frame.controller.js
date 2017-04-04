angular.module('IttyBittyNote').controller('menuFrameController', function($scope, $http, $interval, $mdSidenav) {
	$scope.activePage = 'Server Status';
	
	$scope.toggle = function(){
		$mdSidenav("left").toggle();
	}

});
