var tzApp = angular.module('tzApp', ['ngAnimate']);

tzApp.controller('TzController', ['$scope', '$http', function($scope, $http) {
	$http.get('js/custom.json').success(function(data) {
		$scope.tz = data;
		$scope.listOrder = 'firstName';
	});	
}]);